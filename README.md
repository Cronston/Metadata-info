<div align="center">

# Metadata Extractor - OSINT CLI Tool

**Professional metadata extraction and analysis for OSINT investigations, digital forensics, and security research**

[![Python Version](https://img.shields.io/badge/Python-3.13%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Language](https://img.shields.io/github/languages/top/Cronston/Metadata-info)](https://github.com/Cronston/Metadata-info)
[![GitHub Stars](https://img.shields.io/github/stars/Cronston/Metadata-info?style=social)](https://github.com/Cronston/Metadata-info/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Cronston/Metadata-info?style=social)](https://github.com/Cronston/Metadata-info/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/Cronston/Metadata-info)](https://github.com/Cronston/Metadata-info/issues)

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Use Cases](#use-cases) • [Releases](#releases)

</div>

---

## Features

- **Complete EXIF Extraction** - Extract all metadata tags, including hidden and proprietary fields
- **GPS Intelligence** - Automatic geolocation detection with Google Maps integration
- **Camera Profiling** - Identify manufacturer, model, lens, and firmware details
- **Technical Analysis** - ISO, shutter speed, aperture, focal length, and more
- **Auto-Save Results** - All extractions automatically saved to `./save/` with timestamps
- **Colored Output** - Beautiful, organized terminal display for easy analysis
- **Privacy-Focused** - Offline processing, no data transmission

---

## Installation

### Prerequisites
- Python 3.13 or higher
- pip package manager

### Quick Start

#### 1. Clone the repository
```bash
git clone https://github.com/Cronston/Metadata-info.git
cd Metadata-info
```

#### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

The tool supports both **CLI argument mode** (for automation and scripting) and **interactive mode** (for manual use).

### CLI Argument Mode

```bash
# Basic usage
python main.py -i image.jpg

# Batch processing (process all images in a folder)
python main.py --folder /path/to/images/

# Custom output file
python main.py -i image.jpg -o results/metadata.txt

# Don't save to file (display only)
python main.py -i image.jpg --no-save

# Quiet mode (minimal output, no banner, no typing effect)
python main.py -i image.jpg --quiet

# Disable typing effect (faster output)
python main.py -i image.jpg --no-typing

# Skip ASCII banner
python main.py -i image.jpg --no-banner

# Combine options
python main.py -i image.jpg --no-typing --no-save
```

### Interactive Mode

To run in interactive mode, use the `--interactive` flag:

```bash
python main.py --interactive
```

The program will prompt you to enter the image file path.

### Help and Version

Running the program without arguments will display the help message.

```bash
# Show help
python main.py --help
# OR
python main.py

# Show version
python main.py --version
```

### Demo
<!-- TODO: Add GIF demonstration here -->
<!-- ![Demo](assets/demo.gif) -->

**Coming soon:** Animated GIF showing the tool in action

---

## Use Cases

### OSINT Investigations

**Scenario:** Verifying the authenticity and origin of images in open-source intelligence gathering.

**Applications:**
- **Geolocation Verification** - Confirm claimed locations using GPS coordinates
- **Timeline Analysis** - Establish chronological sequences of events
- **Device Attribution** - Identify cameras/phones used across multiple images
- **Source Verification** - Determine if images are original or downloaded/edited

**Example Workflow:**
1. Collect images from social media, websites, or public sources
2. Extract metadata to verify location claims
3. Cross-reference timestamps with known events
4. Identify patterns in device usage

---

### Digital Forensics

**Scenario:** Investigating digital evidence in legal or security contexts.

**Applications:**
- **Evidence Authentication** - Verify image integrity and originality
- **Tampering Detection** - Identify edited or manipulated photos
- **Chain of Custody** - Document original capture details
- **Device Forensics** - Profile equipment used in investigations

**Example Workflow:**
1. Receive digital evidence (photos, documents)
2. Extract complete metadata including hidden tags
3. Document camera settings, timestamps, and GPS data
4. Generate timestamped reports for legal proceedings

---

### Security & Privacy Audits

**Scenario:** Assessing metadata leakage risks in organizational workflows.

**Applications:**
- **Privacy Risk Assessment** - Identify sensitive data in image metadata
- **Data Leak Prevention** - Audit images before public release
- **Security Training** - Demonstrate metadata risks to staff
- **Compliance Verification** - Ensure metadata removal policies are followed

**Example Workflow:**
1. Scan organizational image repositories
2. Identify images with GPS, device, or personal data
3. Generate reports on metadata exposure
4. Implement metadata stripping procedures

---

### Cybersecurity Research

**Scenario:** Analyzing threat actor techniques and attribution.

**Applications:**
- **Threat Attribution** - Profile devices used by threat actors
- **Campaign Analysis** - Link related images across campaigns
- **Operational Security** - Identify OPSEC failures in adversary images
- **Intelligence Gathering** - Extract technical details from leaked images

**Example Workflow:**
1. Collect images from threat actor communications
2. Extract device fingerprints and settings
3. Correlate metadata across multiple sources
4. Build attribution profiles

---

### Photography & Media Analysis

**Scenario:** Analyzing professional photography workflows and equipment.

**Applications:**
- **Equipment Research** - Study camera settings used by professionals
- **Workflow Analysis** - Understand post-processing pipelines
- **Copyright Verification** - Identify original photographers
- **Technical Learning** - Analyze shooting techniques

---

## Project Structure

```
Metadata-info/
├── main.py                      # Entry point and CLI interface
├── extractors/                  # Metadata extraction modules
│   ├── image_extractor.py       # Image EXIF extraction logic
│   └── __init__.py
├── parsers/                     # Data parsing modules
│   ├── gps_parser.py            # GPS coordinate parsing
│   ├── exif_parser.py           # EXIF tag interpretation
│   └── __init__.py
├── output/                      # Output formatting modules
│   ├── formatter.py             # Terminal output formatting
│   ├── file_saver.py            # File saving logic
│   └── __init__.py
├── utils/                       # Utility functions
│   ├── helpers.py               # Helper functions
│   └── __init__.py
├── requirements.txt             # Python dependencies
├── LICENSE                      # MIT License
├── README.md                    # This file
└── save/                        # Auto-saved extraction results
```

---

## Technical Details

### Dependencies
- **Pillow** (10.0.0+) - Image processing and EXIF extraction
- **colorama** (0.4.6+) - Cross-platform colored terminal output

### Supported Formats
- **Images:** JPEG, PNG, TIFF, BMP, GIF
- **RAW Formats:** Limited support (depends on Pillow capabilities)

### Extractable Metadata

#### Image Information
- File name, size, format
- Dimensions (width × height)
- Color space and bit depth

#### Camera Data
- Manufacturer (Make)
- Model
- Firmware version (Software)
- Lens make and model
- Serial numbers (if available)

#### Shooting Settings
- ISO sensitivity
- Shutter speed (ExposureTime)
- Aperture (FNumber)
- Focal length
- Exposure program
- Metering mode
- Flash status
- White balance

#### GPS Data
- Latitude and longitude
- Altitude
- GPS timestamp
- Direction (if available)
- Direct Google Maps link

#### Timestamps
- DateTime (file modification)
- DateTimeOriginal (capture time)
- DateTimeDigitized (digitization time)
- GPS timestamp

#### Advanced Tags
- Color space
- Compression type
- Orientation
- Resolution (DPI)
- Software used for editing
- Copyright information
- Artist/Author
- All proprietary manufacturer tags

---

## Releases

### Latest Release
Check the [Releases page](https://github.com/Cronston/Metadata-info/releases) for the latest version.

### Version History
- **[v1.0.0](https://github.com/Cronston/Metadata-info/releases/tag/v1.0.0)** - Initial release with core functionality
- **Future releases** - Check [GitHub Releases](https://github.com/Cronston/Metadata-info/releases) for updates

### Download
```bash
# Clone the latest release
git clone --branch v1.0.0 https://github.com/Cronston/Metadata-info.git

# Or download a specific release
wget https://github.com/Cronston/Metadata-info/archive/refs/tags/v1.0.0.zip
```

---

## Ethical Use & Legal Disclaimer

> [!CAUTION]
> This tool is designed for **authorized and ethical use only**. Misuse may violate privacy laws and regulations.

### Permitted Use
- Analyzing your own files and images
- Authorized security testing and audits
- OSINT research within legal boundaries
- Educational and academic purposes
- Digital forensics with proper authorization
- Privacy awareness training

### Prohibited Use
- Unauthorized surveillance or stalking
- Privacy violations
- Harassment or doxxing
- Any illegal activities

### Legal Compliance
Always ensure compliance with:
- **GDPR** (General Data Protection Regulation)
- **CCPA** (California Consumer Privacy Act)
- **Local privacy and data protection laws**
- **Computer Fraud and Abuse Act (CFAA)**

**By using this tool, you agree to use it responsibly and ethically.**

---

## Troubleshooting

### Error: "No module named 'PIL'"
**Solution:**
```bash
pip install Pillow
```

### Error: "externally-managed-environment"
**Solution:** Use a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### No EXIF Data Found
**Common Reasons:**
- Screenshots don't contain EXIF data
- Images from social media are often stripped
- Edited photos may lose metadata
- PNG and GIF formats rarely contain EXIF

**Solution:** Try with original, unedited JPEG images from cameras or smartphones.

### Permission Denied
**Solution:**
```bash
chmod +x main.py
# Or run with python explicitly
python3 main.py
```

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Built with [Pillow](https://python-pillow.org/) for image processing
- Inspired by the OSINT and cybersecurity community
- Created for educational and research purposes

---

## Contact

**Project Link:** [https://github.com/Cronston/Metadata-info](https://github.com/Cronston/Metadata-info)

**Issues:** [https://github.com/Cronston/Metadata-info/issues](https://github.com/Cronston/Metadata-info/issues)

---

<div align="center">

**Star this repository if you find it useful!**

Created with for OSINT research and cybersecurity education

</div>