# Metadata Extractor - OSINT CLI Tool

A command-line tool for extracting and analyzing metadata from images.

## Features

- Complete EXIF data extraction - all tags, including hidden ones
- GPS coordinates - automatic location detection with Google Maps link
- Camera information - manufacturer, model, lens
- Shooting settings - ISO, shutter speed, aperture, focal length
- Auto-save - results are saved to ./save/

## Installation

### 1. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Interactive mode
```bash
./venv/bin/python3 main.py
```

The program will prompt for the image file path.

## Example Output

```
======================================================================
METADATA EXTRACTOR - OSINT TOOL
======================================================================

----------------------------------------------------------------------
BASIC INFORMATION
----------------------------------------------------------------------
File Name                      : IMG_1234.jpg
File Size                      : 2.45 MB
Image Format                   : JPEG
Dimensions                     : 4032 x 3024 pixels

----------------------------------------------------------------------
CAMERA INFORMATION
----------------------------------------------------------------------
Make                           : Apple
Model                          : iPhone 13 Pro
Software                       : 15.6.1

----------------------------------------------------------------------
CAMERA SETTINGS
----------------------------------------------------------------------
DateTime                       : 2024:03:15 14:23:45
ExposureTime                   : 1/120 sec
FNumber                        : f/1.8
ISO                            : 100
FocalLength                    : 5.7 mm

----------------------------------------------------------------------
GPS LOCATION DATA
----------------------------------------------------------------------
Latitude                       : 55.751244°
Longitude                      : 37.618423°
Coordinates                    : 55.751244, 37.618423
Google Maps                    : https://www.google.com/maps?q=55.751244,37.618423

----------------------------------------------------------------------
RAW EXIF DATA (ALL TAGS)
----------------------------------------------------------------------
[... all other EXIF tags ...]

Extracted 87 EXIF tags
Results saved to: ./save/metadata_IMG_1234_20241125_170530.txt
```

## Project Structure

```
githubber/
├── main.py                      # Entry point
├── extractors/                  # Metadata extraction modules
│   ├── image_extractor.py
│   └── __init__.py
├── parsers/                     # Data parsing modules
│   ├── gps_parser.py
│   ├── exif_parser.py
│   └── __init__.py
├── output/                      # Output modules
│   ├── formatter.py
│   ├── file_saver.py
│   └── __init__.py
├── utils/                       # Utilities
│   ├── helpers.py
│   └── __init__.py
├── requirements.txt
└── save/                        # Saved results
```

## Technical Details

### Dependencies
- Pillow - Image processing and EXIF extraction
- colorama - Colored terminal output

### Supported Formats
- Images: JPEG, PNG, TIFF, BMP, GIF

### Extractable Data

#### Images
- Basic information (size, format, resolution)
- Camera (manufacturer, model, lens)
- Shooting settings (ISO, shutter speed, aperture, focal length)
- GPS coordinates (latitude, longitude, altitude)
- Date and time of capture
- All technical EXIF tags

## OSINT Applications

### Digital Forensics
- Verifying image authenticity
- Identifying photo sources
- Analyzing timestamps

### Geolocation
- Determining shooting location
- Building routes from photos
- Location verification

### Security Audit
- Checking for metadata leaks
- Demonstrating privacy risks
- Security training

## Ethical Use

IMPORTANT: This tool is intended only for:
- Authorized security testing
- OSINT research
- Educational purposes
- Analyzing your own files

Always comply with privacy laws and obtain necessary permissions.

## Troubleshooting

### Error: "No module named 'PIL'"
```bash
pip install Pillow
```

### Error: "externally-managed-environment"
Use a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### No EXIF data
Some images may not contain metadata:
- Screenshots usually don't have EXIF
- Images from the internet are often cleaned
- Edited photos may lose metadata


Created for OSINT research and cybersecurity education
