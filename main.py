#!/usr/bin/env python3

import sys
import time
from pathlib import Path

from extractors import ImageExtractor
from parsers import GPSParser, ExifParser
from output import OutputFormatter, FileSaver


def print_slow(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


class MetadataAnalyzer:
    
    def __init__(self, file_path, save_dir="./save"):
        self.file_path = Path(file_path)
        self.formatter = OutputFormatter()
        self.saver = FileSaver(save_dir)
        self.typing_delay = 0.015
    
    def print_slow_item(self, text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(self.typing_delay)
        print()
    
    def analyze(self):
        if not self.file_path.exists():
            print(f"\nFile not found: {self.file_path}")
            return
        
        file_ext = self.file_path.suffix.lower()
        
        try:
            if file_ext in ['.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.gif']:
                self._analyze_image()
            else:
                print(f"\nUnsupported file type: {file_ext}")
                print(f"Supported formats: JPEG, PNG, TIFF, BMP, GIF")
                return
        except Exception as e:
            print(f"\nError: {e}")
            return
        
        print()
        output_file = self.saver.save(
            self.formatter.get_output_lines(),
            self.file_path.name
        )
        
        if output_file:
            print_slow(f"Results saved to: {output_file}", 0.02)
    
    def _analyze_image(self):
        extractor = ImageExtractor(self.file_path)
        metadata = extractor.extract()
        
        print_slow("\n" + "="*70, 0.001)
        print_slow("BASIC INFORMATION", 0.03)
        print_slow("="*70, 0.001)
        
        basic = metadata['basic_info']
        self.print_slow_item(f"File Name                      : {basic['file_name']}")
        self.print_slow_item(f"File Size                      : {basic['file_size']}")
        self.print_slow_item(f"Image Format                   : {basic['format']}")
        self.print_slow_item(f"Image Mode                     : {basic['mode']}")
        self.print_slow_item(f"Dimensions                     : {basic['dimensions']}")
        
        if not metadata['camera_info'] and not metadata['settings_info'] and not metadata['raw_exif']:
            print_slow("\nNo EXIF metadata found in this image", 0.03)
            return
        
        if metadata['camera_info']:
            print_slow("\n" + "="*70, 0.001)
            print_slow("CAMERA INFORMATION", 0.03)
            print_slow("="*70, 0.001)
            for key, value in metadata['camera_info'].items():
                self.print_slow_item(f"{key:30} : {value}")
        
        if metadata['settings_info']:
            print_slow("\n" + "="*70, 0.001)
            print_slow("CAMERA SETTINGS", 0.03)
            print_slow("="*70, 0.001)
            for key, value in metadata['settings_info'].items():
                formatted_value = ExifParser.format_value(key, value)
                self.print_slow_item(f"{key:30} : {formatted_value}")
        
        if metadata['gps_coords'][0] is not None:
            print_slow("\n" + "="*70, 0.001)
            print_slow("GPS LOCATION DATA", 0.03)
            print_slow("="*70, 0.001)
            lat, lon = metadata['gps_coords']
            
            self.print_slow_item(f"Latitude                       : {lat:.6f}°")
            self.print_slow_item(f"Longitude                      : {lon:.6f}°")
            self.print_slow_item(f"Coordinates                    : {lat:.6f}, {lon:.6f}")
            
            maps_link = GPSParser.get_maps_link(lat, lon)
            if maps_link:
                self.print_slow_item(f"Google Maps                    : {maps_link}")
            
            for key, value in metadata['gps_info'].items():
                if key not in ['GPSLatitude', 'GPSLongitude', 'GPSLatitudeRef', 'GPSLongitudeRef']:
                    self.print_slow_item(f"{key:30} : {str(value)}")
        
        if metadata['raw_exif']:
            print_slow("\n" + "="*70, 0.001)
            print_slow("RAW EXIF DATA (ALL TAGS)", 0.03)
            print_slow("="*70, 0.001)
            
            sorted_tags = sorted(metadata['raw_exif'].items())
            
            for key, value in sorted_tags:
                formatted_value = ExifParser.format_value(key, value)
                self.print_slow_item(f"{key:30} : {formatted_value}")
        
        total_tags = (len(metadata['camera_info']) + 
                     len(metadata['settings_info']) + 
                     len(metadata['raw_exif']))
        
        print_slow(f"\n✅ Extracted {total_tags} EXIF tags", 0.02)


def print_banner():
    banner = """
╔═══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║   ███╗   ███╗███████╗████████╗ █████╗ ██████╗  █████╗ ████████╗  ║
║   ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝  ║
║   ██╔████╔██║█████╗     ██║   ███████║██║  ██║███████║   ██║     ║
║   ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║  ██║██╔══██║   ██║     ║
║   ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║██████╔╝██║  ██║   ██║     ║
║   ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝     ║
║                                                                   ║
║        ██╗███╗   ██╗███████╗ ██████╗                             ║
║        ██║████╗  ██║██╔════╝██╔═══██╗                            ║
║        ██║██╔██╗ ██║█████╗  ██║   ██║                            ║
║        ██║██║╚██╗██║██╔══╝  ██║   ██║                            ║
║        ██║██║ ╚████║██║     ╚██████╔╝                            ║
║        ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝                             ║
║                                                                   ║
║              OSINT Metadata Extraction Tool                       ║
║                   Image Analysis                                  ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
"""
    print_slow(banner, delay=0.001)
    print()


def main():
    print_banner()
    
    print_slow("Welcome to Metadata Info Extractor!", delay=0.03)
    print()
    
    file_path = input("Enter the path to image file: ").strip()
    
    if not file_path:
        print("\nNo file path provided!")
        sys.exit(1)
    
    file_path = file_path.strip('"').strip("'")
    
    print()
    print_slow("Analyzing image...", delay=0.03)
    time.sleep(0.5)
    
    analyzer = MetadataAnalyzer(file_path)
    analyzer.analyze()


if __name__ == "__main__":
    main()
