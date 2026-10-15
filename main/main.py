"""
Auto Brightness - sets monitor brightness based on sunrise/sunset.
Runs silently in the background. Logs to %LOCALAPPDATA%\\AutoBrightness\\log.txt

Requirements:  pip install astral screen-brightness-control
Build exe:     pyinstaller --onefile --noconsole auto_brightness.py
"""

import ctypes
import logging
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from logging.handlers import RotatingFileHandler

import screen_brightness_control as sbc
from astral import Observer
from astral.sun import sun

# ======================= CONFIG =======================
LATITUDE = 47.309325                # Rüschlikon, Switzerland
LONGITUDE = 8.556292
DAY_BRIGHTNESS = 100        # %
NIGHT_BRIGHTNESS = 20       # %
DAY_OFFSET = timedelta(hours=0)     # applied to sunrise (+ = later)
NIGHT_OFFSET = timedelta(hours=-1)  # applied to sunset  (-1h = one hour before)
CHECK_INTERVAL = 60         # seconds between checks
# ======================================================

LOG_DIR = os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")), "AutoBrightness")
os.makedirs(LOG_DIR, exist_ok=True)
handler = RotatingFileHandler(os.path.join(LOG_DIR, "log.txt"), maxBytes=1_000_000, backupCount=2)
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
log = logging.getLogger("auto_brightness")
log.addHandler(handler)
log.setLevel(logging.INFO)

OBSERVER = Observer(latitude=LATITUDE, longitude=LONGITUDE)


def ensure_single_instance():
    """Exit if another instance is already running (Windows named mutex)."""
    if os.name != "nt":
        return
    ctypes.windll.kernel32.CreateMutexW(None, False, "Global\\AutoBrightnessMutex")
    if ctypes.windll.kernel32.GetLastError() == 183:  # ERROR_ALREADY_EXISTS
        sys.exit(0)


def target_brightness(now: datetime) -> int:
    """Return brightness for the most recent day/night transition before `now`."""
    events = []
    for delta in (-1, 0, 1):
        day = (now + timedelta(days=delta)).date()
        try:
            s = sun(OBSERVER, date=day, tzinfo=timezone.utc)
            events.append((s["sunrise"] + DAY_OFFSET, DAY_BRIGHTNESS))
            events.append((s["sunset"] + NIGHT_OFFSET, NIGHT_BRIGHTNESS))
        except ValueError:  # polar day/night - no sunrise/sunset that day
            continue
    past = [e for e in sorted(events) if e[0] <= now]
    return past[-1][1] if past else DAY_BRIGHTNESS


def apply(level: int) -> None:
    current = sbc.get_brightness()
    if any(c != level for c in current):
        sbc.set_brightness(level)
        log.info("Brightness set to %d%% (was %s)", level, current)


def main():
    ensure_single_instance()
    log.info("Started (lat=%s, lon=%s)", LATITUDE, LONGITUDE)
    while True:
        try:
            apply(target_brightness(datetime.now(timezone.utc)))
        except Exception:
            log.exception("Failed to update brightness")
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()