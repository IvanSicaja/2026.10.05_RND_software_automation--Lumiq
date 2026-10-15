📌 **Project Title:** **AUTO BRIGHTNESS – SUNRISE/SUNSET MONITOR CONTROL**  
📅 **Project Timeline:** **To be added**  
🎥 YouTube Demo: To be added  
📦 GitHub Source Code: To be added  

---

📍 My Personal Profiles ⬇︎  
🎥 Video Portfolio: To be added  
📦 GitHub Profile: <https://github.com/IvanSicaja>  
👔 LinkedIn: <https://www.linkedin.com/in/ivan-si%C4%8Daja-832682222>  
🎥 YouTube: <https://www.youtube.com/@ivan_sicaja>  

---

### 💡 Core Challenge This Project Resolves:

Automatically adjusting **Windows monitor brightness** according to calculated **sunrise/sunset times**, avoiding repetitive manual brightness changes while running quietly in the background.

---

### 🔧 Core Skills Tree Used To Build The Project - Skills and Tech Stack:
*(Project-Specific Structured Overview)*
```
│
├── Software Engineering
│ ├── Software / Frameworks / Libraries
│ │ ├── Python
│ │ ├── astral (astronomical sunrise/sunset calculation)
│ │ ├── screen-brightness-control (monitor brightness control)
│ │ ├── datetime / timezone (time-based scheduling)
│ │ ├── logging / RotatingFileHandler (rotating log files)
│ │ ├── ctypes (Windows mutex / single-instance check)
│ │ ├── os / sys / time (paths, process control, periodic checks)
│ │ └── PyInstaller (optional Windows executable packaging)
│ │
│ ├── Hardware
│ │ ├── Windows PC
│ │ └── Brightness-controllable internal or external display
│ │
│ └── Skills
│   ├── Background process development
│   ├── Time-based application logic
│   ├── Astronomical event calculations
│   ├── Windows API integration
│   ├── Single-instance process control
│   ├── Monitor brightness automation
│   ├── Exception handling and diagnostic logging
│   └── Application packaging
│
├── Mechanical Engineering
│ ├── Software / Frameworks / Libraries
│ │ └── Not applicable (software-only project)
│ │
│ ├── Hardware / Hardware Tools
│ │ └── Not applicable (no mechanical components)
│ │
│ └── Skills
│   └── Not applicable (no mechanical design or fabrication)
│
├── Electrical Engineering
│ ├── Software / Frameworks / Libraries
│ │ └── screen-brightness-control
│ │
│ ├── Hardware Components
│ │ ├── Windows computer
│ │ └── Compatible display / monitor
│ │
│ ├── Hardware Tools
│ │ └── No additional hardware tools required
│ │
│ ├── Communication Protocols
│ │ └── Monitor control via supported system/display interfaces
│ │
│ └── Skills
│   ├── Software-controlled display brightness
│   ├── Display compatibility assessment
│   └── Hardware/software interaction troubleshooting
│
├── Data Science & Artificial Intelligence
│ ├── Software / Frameworks / Libraries
│ │ └── astral (deterministic astronomy calculations; not AI)
│ │
│ ├── Hardware
│ │ └── No specialized AI/data-science hardware
│ │
│ └── Skills
│   ├── Time and coordinate-based calculations
│   └── No machine-learning or AI features implemented
│
└── Research & Development Engineering
  ├── Software / Frameworks / Libraries
  │ └── Integrated within sections above
  │
  ├── Hardware / Hardware Tools
  │ └── Integrated within sections above
  │
  └── Skills
    ├── Configurable time offsets and brightness levels
    ├── Event-based day/night state calculation
    ├── Repeatable 60-second control-loop execution
    ├── Fault-tolerant operation through exception handling
    └── Structured diagnostics and application iteration
```

---

### 📋 Core System Capabilities - List Only:

- **Automatically calculates sunrise and sunset** from configured coordinates and date
- **Sets daytime and nighttime monitor brightness** (default: 100% / 20%)
- **Supports sunrise/sunset offsets** (default: sunrise +0 h; sunset −1 h)
- **Rechecks brightness every 60 seconds** while running
- **Avoids unnecessary brightness updates** when already at the target level
- **Runs without a graphical interface** (background operation)
- **Prevents duplicate instances on Windows** using a named mutex
- **Logs changes and errors** to a rotating log file
- **Can be packaged as a Windows executable** using PyInstaller

---

### 🧠️ How It Works - Core System Capabilities Workflow:

The application reads configured **latitude/longitude**, calculates daily **sunrise and sunset** with **astral**, selects a **day/night brightness target**, and updates the display when necessary. The calculation runs locally; **automatic location detection is not implemented**.  
The core is a **Python background loop** using **astral** and **screen-brightness-control**.

The application also includes:

- **Day/night brightness settings:** `DAY_BRIGHTNESS = 100`, `NIGHT_BRIGHTNESS = 20`
- **Time offsets:** `DAY_OFFSET = 0 h`, `NIGHT_OFFSET = −1 h`
- **Check interval:** `CHECK_INTERVAL = 60` seconds
- **Log location:** `%LOCALAPPDATA%\AutoBrightness\log.txt`

**Sunrise/sunset calculation:**  
The `astral` library computes sunrise and sunset from the configured coordinates, date, and UTC-aware timestamps. The code considers yesterday, today, and tomorrow to identify the **most recent brightness transition**. No online sunrise/sunset API is required.

**Day/night target selection:**  
At sunrise plus `DAY_OFFSET`, the target becomes **day brightness**. At sunset plus `NIGHT_OFFSET`, it becomes **night brightness**. With the current settings, night mode begins **one hour before sunset**. This is **two-level switching**, not a smooth brightness transition.

**Monitor brightness adjustment:**  
`screen-brightness-control` reads the current brightness and sets the target only when a returned monitor level differs. Actual support depends on the monitor, Windows driver, and display-control capabilities.

**Hardware choosing and connecting:**  
Use a **Windows PC** and a monitor supported by the brightness-control library. Some external monitors require **DDC/CI** to be enabled; compatibility is not guaranteed. No additional electronics or physical modifications are required.

**Frame design and 3D printing:**  
**Not applicable:** the project contains no mechanical design, CAD modelling, or 3D-printed parts.

**Developing mechatronic code:**  
**Not applicable to physical actuators:** the Python application controls supported monitor brightness through system-level software interfaces.

**Installation and execution:**  
Install **Python 3** and then the external dependencies:

```powershell
pip install astral screen-brightness-control
```

Set `LATITUDE`, `LONGITUDE`, and the brightness/offset values in `auto_brightness.py`, then launch:

```powershell
python auto_brightness.py
```

For an optional silent Windows `.exe` build:

```powershell
pip install pyinstaller
pyinstaller --onefile --noconsole auto_brightness.py
```

The program continues running **until its process is stopped or Windows ends the session**. It does **not** automatically restart after reboot; configure **Task Scheduler** or Windows startup separately if needed. The current code does **not** provide a GUI, a schedule based on manually entered clock times, or automatic geographic location detection.

---

### ⚠️ Note:

**Replace the example coordinates** before use. The original code specifies `48.1486, 17.1077` (Bratislava area), which is not Rüschlikon. For Rüschlikon, use appropriately checked local coordinates; exact residential coordinates are unnecessary.  
**Display compatibility varies**; test on your actual hardware. Running `python auto_brightness.py` in a terminal normally ties the process to that terminal. A console-free PyInstaller build hides the console but still requires startup configuration for automatic launch.  
**No public project screenshots, demo video, or repository URL were supplied** for this application; the media positions below are retained as placeholders rather than showing unrelated material.

---

### 📸 Project Snapshots:

<p align="center">
  <!-- Screenshot 1: Application overview / intended workflow; replace placeholder path when image is available. -->
  <!-- <img src="publish/2.0_Thumbnail_1.png" 
       alt="Auto Brightness Preview 1: Application overview / intended workflow" 
       width="640" 
       height="360"> -->
  <em>Screenshot 1 — Application overview / intended workflow: To be added</em>
</p>

<p align="center">
  <!-- Screenshot 2: Configuration parameters; replace placeholder path when image is available. -->
  <!-- <img src="publish/2.0_Thumbnail_2.png" 
       alt="Auto Brightness Preview 2: Configuration parameters" 
       width="640" 
       height="360"> -->
  <em>Screenshot 2 — Configuration parameters: To be added</em>
</p>

<p align="center">
  <!-- Screenshot 3: Sunrise and sunset scheduling; replace placeholder path when image is available. -->
  <!-- <img src="publish/2.0_Thumbnail_3.png" 
       alt="Auto Brightness Preview 3: Sunrise and sunset scheduling" 
       width="640" 
       height="360"> -->
  <em>Screenshot 3 — Sunrise and sunset scheduling: To be added</em>
</p>

<p align="center">
  <!-- Screenshot 4: Daytime brightness behaviour; replace placeholder path when image is available. -->
  <!-- <img src="publish/2.0_Thumbnail_4.png" 
       alt="Auto Brightness Preview 4: Daytime brightness behaviour" 
       width="640" 
       height="360"> -->
  <em>Screenshot 4 — Daytime brightness behaviour: To be added</em>
</p>

<p align="center">
  <!-- Screenshot 5: Nighttime brightness behaviour; replace placeholder path when image is available. -->
  <!-- <img src="publish/2.0_Thumbnail_5.png" 
       alt="Auto Brightness Preview 5: Nighttime brightness behaviour" 
       width="640" 
       height="360"> -->
  <em>Screenshot 5 — Nighttime brightness behaviour: To be added</em>
</p>

<p align="center">
  <!-- Screenshot 6: Log output example; replace placeholder path when image is available. -->
  <!-- <img src="publish/2.0_Thumbnail_6.png" 
       alt="Auto Brightness Preview 6: Log output example" 
       width="640" 
       height="360"> -->
  <em>Screenshot 6 — Log output example: To be added</em>
</p>

<p align="center">
  <!-- Screenshot 7: Windows startup setup (optional); replace placeholder path when image is available. -->
  <!-- <img src="publish/2.0_Thumbnail_7.png" 
       alt="Auto Brightness Preview 7: Windows startup setup (optional)" 
       width="640" 
       height="360"> -->
  <em>Screenshot 7 — Windows startup setup (optional): To be added</em>
</p>

---

### 🎥 Video Demonstration:

<p align="center">
  <!-- Add the Auto Brightness demo URL and thumbnail when available. -->
  <!-- <a href="YOUR_AUTO_BRIGHTNESS_DEMO_URL">
    <img src="YOUR_AUTO_BRIGHTNESS_VIDEO_THUMBNAIL_URL"
         alt="Watch the Auto Brightness demo"
         width="640"
         height="1000">
  </a> -->
  <em>Auto Brightness video demonstration: To be added</em>
</p>

---

### 📣 Hashtags Section:

**#AutoBrightness #MonitorBrightness #BrightnessControl #Python #WindowsAutomation #SunriseSunset #Astral #ScreenBrightnessControl #BackgroundService #Automation #TimeBasedAutomation #DisplayControl #PyInstaller #SoftwareEngineering**
