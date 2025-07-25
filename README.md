# 🛡️ P8GP-G01: Advanced Object Detection System with GUI

<div align="center">

![Version](https://img.shields.io/badge/version-2.1-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20MacOS-lightgrey.svg)
![License](https://img.shields.io/badge/license-Non--Commercial-red.svg)

*A real-time safety monitoring system powered by AI and deep learning*

</div>

## 📄 Project Files & Documentation

### 📚 Essential Files Overview

| File | Purpose | Description |
|---|---|---|
| 📄 **LICENSE** | Legal Protection | Non-commercial use license preventing unauthorized commercial usage |
| 📄 **.gitignore** | Version Control | Comprehensive exclusion rules for Python, AI models, and temporary files |
| 📄 **README.md** | Documentation | Complete project guide, setup instructions, and feature overview |
| 📁 **Project_Picture/** | Visual Assets | Application screenshots and interface previews for documentation |
| 📁 **UI/** | Main Application | Core application code, models, and resources |

### 🔒 License Information
This project is protected under a **Non-Commercial License** which:
- ✅ **Permits**: Personal use, educational purposes, research, and open-source contributions
- ❌ **Prohibits**: Commercial use, business applications, revenue generation, and corporate deployment
- 📋 **Requires**: Attribution to original authors and license inclusion in distributions

### 🚫 Git Exclusions (.gitignore)
The comprehensive .gitignore file excludes:
- Python cache files and virtual environments
- AI model files (*.pt, *.pth) to prevent large file commits
- Generated detection images and temporary files
- IDE-specific files and OS-generated files
- Sensitive configuration and log files

---

## 🎨 Visual Gallery & Screenshots

<div align="center">

### 📱 Application Interface Preview

The P8GP-G01 system features a modern, intuitive interface designed for seamless safety monitoring:

![Main Interface](Project_Picture/amin1.png)

*Screenshot showcasing the main application interface with real-time detection capabilities*

### 🔍 Key Interface Elements Highlighted:
- **Live Video Feed**: Real-time camera stream with detection overlays
- **Detection Status Panel**: Visual indicators for safety equipment monitoring  
- **Control Dashboard**: Comprehensive monitoring and statistics display
- **Interactive Elements**: User-friendly buttons and navigation controls

> **📸 More Screenshots**: Additional project images and interface previews are available in the `Project_Picture/` directory

</div>

---

## 📸 Project Showcase

<div align="center">

### 🎯 Main Application Interface

![P8GP-G01 Application](Project_Picture/amin2.png)

*Real-time object detection in action - showcasing helmet, mask, and smoking detection capabilities*

</div>

---

## 📖 Project Overview

**P8GP-G01** is a cutting-edge real-time object detection system engineered for safety monitoring applications. Leveraging state-of-the-art YOLO models (YOLOv5n and custom-trained variants), the system provides intelligent detection capabilities for critical safety equipment and hazardous situations including **Helmets**, **Smoking**, **Fire**, **Smoke**, and **Face Masks**.

The system features an intuitive PyQt6-powered graphical user interface that delivers seamless user experience with real-time monitoring, automated image saving, and comprehensive detection analytics. Built for cross-platform compatibility, it supports multiple camera sources and includes an elegant animated welcome interface.

### ✨ Key Features

<table>
<tr>
<td width="50%">

🔍 **Real-Time Detection**
- Advanced safety equipment recognition
- Multi-class object detection (Helmets, Masks, Smoking, Fire, Smoke)
- High-accuracy YOLO model implementation
- Real-time confidence scoring

🖥️ **Intelligent GUI**
- Modern welcome screen with animations
- Live video feed with detection overlays
- Comprehensive control dashboard
- Interactive image gallery system

</td>
<td width="50%">

📹 **Camera Management**
- Universal camera detection (Windows/Linux/macOS)
- Multiple video source support
- Automatic device enumeration
- Platform-optimized camera handling

💾 **Smart Data Management**
- Automated image categorization and saving
- Organized folder structure by detection type
- Gallery preview with thumbnail generation
- Detection statistics and analytics

</td>
</tr>
</table>

### 🎯 Monitoring Capabilities

| Detection Type | Description | Use Case |
|---|---|---|
| 🦺 **Safety Helmets** | Hard hat and protective headgear detection | Construction sites, industrial facilities |
| 😷 **Face Masks** | Medical and protective mask identification | Healthcare, public safety compliance |
| 🚬 **Smoking Detection** | Cigarette and smoking activity recognition | No-smoking zone enforcement |
| 🔥 **Fire Detection** | Flame and fire hazard identification | Emergency response, safety monitoring |
| 💨 **Smoke Detection** | Smoke plume and vapor detection | Early warning systems |

---

## 🛠️ Prerequisites & System Requirements

### System Requirements

| Component | Minimum Requirement | Recommended |
|---|---|---|
| **Operating System** | Windows 10, Linux (Ubuntu 18.04+), macOS 10.15+ | Latest stable versions |
| **Python Version** | Python 3.10+ | Python 3.11+ |
| **RAM** | 4 GB | 8 GB+ |
| **Storage** | 2 GB free space | 5 GB+ |
| **Camera** | USB 2.0 webcam | USB 3.0 HD webcam |
| **CPU** | Dual-core 2.0 GHz | Quad-core 2.5 GHz+ |

### Required Software

- **Python 3.10+** (Tested extensively with Python 3.10; compatible with newer versions including 3.12.4)
- **pip** (Python package manager)
- Compatible webcam or video capture device
- (Optional) **Raspberry Pi** for embedded deployment

### 📚 Dependencies

All dependencies are precisely defined in `UI/requirements.txt` with tested version compatibility:

#### Core Libraries
```
torch==2.3.1              # PyTorch deep learning framework
opencv-python==4.9.0.80   # Computer vision and image processing
numpy==1.26.4             # Numerical computing foundation
ultralytics==8.1.0        # YOLOv5/YOLOv8 implementation
PyQt6==6.6.1              # Modern GUI framework (stable as of March 2025)
pygrabber==0.2            # Enhanced Windows camera detection (DirectShow)
```

#### Built-in Python Modules
*These are included with Python standard library - no installation required:*
- `platform` - System platform detection
- `os` - Operating system interface
- `subprocess` - Process management
- `sys` - System-specific parameters
- `time` - Time-related functions

---

## 📦 Installation & Setup Guide

### Step 1: Repository Setup
```bash
# Clone the repository (if applicable)
git clone <repository-url>
cd P8GP_G01
```

### Step 2: Virtual Environment (Recommended)
```bash
# Create isolated environment
python -m venv venv

# Activate environment
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Verify activation (prompt should show (venv))
```

### Step 3: Navigate to Project Directory
```bash
cd UI
```

### Step 4: Install Dependencies
```bash
# Install all required packages
pip install -r requirements.txt

# Verify installation
pip list
```

### Step 5: Model Verification
Ensure all pre-trained models are present in `UI/Models/`:

| Model File | Purpose | Status |
|---|---|---|
| `Fire_Detection.pt` | Fire and flame detection | ✅ Required |
| `Helmet_Detection.pt` | Safety helmet identification | ✅ Required |
| `Mask_Detection.pt` | Face mask detection | ✅ Required |
| `Smoking_Detection.pt` | Smoking activity detection | ⚠️ Optional (testing) |

> **Note**: If model files are missing, contact the development team or download from the official model repository.

### Step 6: Directory Structure Verification
Confirm the following structure exists within your project:

```
P8GP_G01/
├── 📄 LICENSE                        # Non-commercial license file
├── 📄 .gitignore                     # Git exclusion rules
├── 📄 README.md                      # Main documentation
├── 📁 Project_Picture/               # Project screenshots
│   └── amin1.png                    # Application interface screenshot
└── 📁 UI/                           # Main application directory
    ├── 📁 Codes/                    # Python source code
    ├── 📁 Imgs/                     # Application assets
    │   ├── P1.png                  # Welcome background
    │   └── icon.png                # App icon
    ├── 📁 Images/                   # Detection output storage
    │   ├── 📁 masks/               # Mask detection saves
    │   ├── 📁 Helmets/             # Helmet detection saves
    │   ├── 📁 smoke/               # Smoke detection saves
    │   ├── 📁 Fire/                # Fire detection saves
    │   ├── 📁 Cigarettes/          # Cigarette detection saves
    │   └── 📁 smoking/             # Smoking activity saves
    ├── 📁 Models/                   # AI model files
    ├── requirements.txt             # Dependencies
    └── README.md                    # UI-specific documentation
```

> **📋 Important**: Ensure the `Project_Picture/` folder contains your application screenshots for proper documentation display.

---

## 🚀 Usage Instructions

### Launch Application
```bash
# Ensure you're in the UI directory
cd UI

# Start the application
python Codes/Application.py
```

### 1. Welcome Screen Interaction
- **Startup**: Application begins with an animated welcome screen displaying "P8GP-G01"
- **Navigation**: Click **"Get Started"** to proceed to the main detection interface
- **Animation**: Enjoy the smooth transition effects and professional branding

### 2. Main Interface Navigation

#### 📺 Video Display Panel
- **Live Feed**: Real-time camera stream with AI-powered object detection
- **Detection Overlays**: Colored bounding boxes around detected objects
- **Confidence Scores**: Percentage accuracy displayed for each detection
- **Multi-object Support**: Simultaneous detection of multiple object types

#### 🎛️ Control Panel Features
- **Real-time Status**: Live detection monitoring with visual indicators
- **Object Counters**: Dynamic count of detected objects by category
- **Statistics Table**: Comprehensive "Have" vs "Don't Have" metrics
- **Future Plans**: Expandable table for additional monitoring features

#### 📷 Camera Management
- **Active Cameras**: Click to browse and select from detected camera devices
- **Multi-platform Detection**: Automatic recognition across different operating systems
- **Hot-swapping**: Switch between cameras without restarting the application

#### 🖼️ Image Management System
- **Save Toggle**: Enable/disable "Save Detected Images" functionality
- **Gallery Access**: Browse categorized galleries (Masks, Safety Hats, Smoking, Fire, Smoke)
- **Preview Mode**: Click any saved image for full-size preview
- **Organized Storage**: Automatic categorization by detection type

### 3. Video Feed Controls
```
▶️ Play    - Start/resume video feed
⏸️ Pause   - Temporarily pause detection
⏹️ Stop    - Completely stop video feed and detection
```

### 4. Detection Monitoring
- **Status Indicators**: Real-time visual feedback for each detection type
- **Alert System**: Notifications for new detections
- **Statistics Dashboard**: Comprehensive detection analytics
- **Historical Data**: Track detection patterns over time

### 5. Image Saving & Gallery
- **Automatic Saving**: Enable in "Member's Images" dialog
- **Categorized Storage**: Images automatically sorted by detection type
- **Gallery Browser**: Intuitive interface for viewing saved detections
- **Preview System**: Click thumbnails for enlarged preview

---

## 📂 Detailed Project Architecture

```
P8GP_G01/
│
├── 🗂️ venv/                          # Virtual environment (optional)
├── 📄 LICENSE                        # 🔒 Non-commercial use license
├── 📄 .gitignore                     # 🚫 Git exclusion rules
├── 📄 README.md                      # 📚 Main project documentation
│
├── 🗂️ Project_Picture/               # 📸 Project Screenshots & Media
│   ├── amin1.png                    # Main application interface
│   └── [additional screenshots]     # Other project images
│
└── 🗂️ UI/                            # 🏠 Main Project Hub
    │
    ├── 📁 Codes/                      # 🧠 Core Application Logic
    │   ├── __init__.py               # Package initialization
    │   ├── Application.py            # 🚀 Entry point & app launcher
    │   ├── MainWindow.py             # 🏢 Main application window
    │   ├── WelcomeScreen.py          # 👋 Animated welcome interface
    │   ├── Dashboard.py              # 📊 Central monitoring dashboard
    │   ├── VideoPlayer.py            # 📹 Video feed & playback controls
    │   ├── ControlPanel.py           # 🎛️ Detection monitoring panel
    │   ├── Notification.py           # 🔔 Alert & notification system
    │   ├── Dialogs.py                # 💬 Dialog windows & modals
    │   ├── DetectionEngine.py        # 🤖 AI detection core logic
    │   ├── CameraManager.py          # 📷 Camera handling & management
    │   └── Utilities.py              # 🛠️ Helper functions & utilities
    │
    ├── 📁 Imgs/                       # 🎨 Visual Assets
    │   ├── P1.png                    # Welcome screen background
    │   └── icon.png                  # Application icon
    │
    ├── 📁 Images/                     # 💾 Detection Output Storage
    │   ├── 📁 Masks/                 # Saved face mask detections
    │   ├── 📁 Safety_hats/           # Saved helmet detections
    │   ├── 📁 Smoking/               # Saved smoking detections
    │   ├── 📁 Fire/                  # Saved fire detections
    │   ├── 📁 smoke/                 # Saved smoke detections
    │   └── 📁 Cigarettes/            # Saved cigarette detections
    │
    ├── 📁 Models/                     # 🧠 AI Model Repository
    │   ├── Mask_Detection.pt         # Face mask detection model
    │   ├── Smoking_Detection.pt      # Smoking activity model
    │   ├── Fire_Detection.pt         # Fire detection model
    │   └── Helmet_Detection.pt       # Safety helmet model
    │
    ├── 📄 README.md                   # 📚 UI-specific documentation
    └── 📄 requirements.txt            # 📦 Python dependencies
```

---

## 👥 Development Team & Credits

<table>
<tr>
<td align="center" width="50%">
<h3>🎨 Lead Developer & UI Designer</h3>
<b>Amin Moniry</b><br>
<i>Full-Stack Development, Programming & User Interface Design</i><br>
<br>
<em>Responsible for:</em><br>
• Core application architecture<br>
• AI model integration<br>
• GUI design & implementation<br>
• Cross-platform compatibility<br>
• User experience optimization
</td>
<td align="center" width="50%">
<h3>🎓 Project Supervisor & Technical Advisor</h3>
<b>Saeed Shokraneh</b><br>
<i>Academic Supervision & Technical Guidance</i><br>
<br>
<em>Responsible for:</em><br>
• Project oversight & guidance<br>
• Technical review & validation<br>
• Academic supervision<br>
• Quality assurance<br>
• Strategic direction
</td>
</tr>
</table>

---

## ℹ️ Project Information

<div align="center">

| **Attribute** | **Value** |
|---|---|
| **Version** | `2.1` |
| **Release Date** | April 25, 2025 |
| **Development Location** | Tabriz, Iran 🇮🇷 |
| **Project Type** | Open Source Safety Monitoring System |
| **Primary Language** | Python |
| **GUI Framework** | PyQt6 |
| **AI Framework** | YOLO (Ultralytics) |

</div>

---

## 📝 Important Notes & Tips

### 🔧 Technical Considerations
- **Camera Connection**: Ensure your webcam is properly connected and accessible before launching
- **Windows Users**: Install `pygrabber` for enhanced DirectShow camera detection capabilities
- **Linux Users**: Optional `v4l2-ctl` installation for advanced camera detection (generic detection available as fallback)
- **Raspberry Pi**: Additional GPIO and hardware setup may be required for embedded deployment

### ⚡ Performance Optimization
- **CPU Usage**: Monitor system resources during detection operations
- **Memory Management**: Close unused applications for optimal performance
- **Camera Resolution**: Higher resolutions improve detection accuracy but increase processing load
- **Model Selection**: Different models have varying computational requirements

### 🔒 Security & Privacy
- **Local Processing**: All detection occurs locally - no data transmitted externally
- **Image Storage**: Saved images remain on local device storage
- **Camera Access**: Application requests camera permissions as needed

---

## 🤝 Contributing to P8GP-G01

We welcome contributions from the community! Here's how you can help improve the project:

### 📋 Contribution Guidelines
1. **Fork** the repository to your GitHub account
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request with detailed description

### 🐛 Bug Reports
- Use the GitHub Issues template
- Include system information and error logs
- Provide steps to reproduce the issue
- Attach relevant screenshots if applicable

### 💡 Feature Requests
- Describe the proposed feature in detail
- Explain the use case and benefits
- Consider implementation complexity
- Discuss potential impacts on existing functionality

---

## 📧 Support & Contact

<div align="center">

### 📞 Get in Touch

For questions, support, or collaboration opportunities:

**🌐 GitHub Repository**: [https://github.com/Amin-moniry-pr7](https://github.com/Amin-moniry-pr7)

**📧 Email Support**: Available through GitHub profile

**🐛 Issue Tracker**: Use GitHub Issues for bug reports and feature requests

**💬 Discussions**: Join project discussions on GitHub

</div>

---

<div align="center">

### 🙏 Thank You

Thank you for choosing P8GP-G01 for your safety monitoring needs!

*Built with ❤️ in Tabriz, Iran*

---

![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
![Powered by AI](https://img.shields.io/badge/Powered%20by-AI-blue.svg)
![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red.svg)

</div>