import time
from typing import Dict, Any

from parsers import GPSParser, ExifParser


class ConsoleWriter:
    
    def __init__(self, quiet_mode: bool = False, typing_enabled: bool = True):
        self.quiet_mode = quiet_mode
        self.typing_enabled = typing_enabled and not quiet_mode
        self.typing_delay = 0.015
    
    def print_section_header(self, text: str):
        if self.typing_enabled:
            self._print_slow("\n" + "=" * 70, 0.001)
            self._print_slow(text, 0.03)
            self._print_slow("=" * 70, 0.001)
        else:
            print("\n" + "=" * 70)
            print(text)
            print("=" * 70)
    
    def print_item(self, text: str):
        if self.typing_enabled:
            for char in text:
                print(char, end='', flush=True)
                time.sleep(self.typing_delay)
            print()
        else:
            print(text)
    
    def print_message(self, text: str, delay: float = 0.02):
        if self.typing_enabled:
            self._print_slow(text, delay)
        else:
            print(text)
    
    def print_metadata(self, metadata: Dict[str, Any]):
        self.print_section_header("BASIC INFORMATION")
        basic = metadata['basic_info']
        self.print_item(f"File Name                      : {basic['file_name']}")
        self.print_item(f"File Size                      : {basic['file_size']}")
        self.print_item(f"Image Format                   : {basic['format']}")
        self.print_item(f"Image Mode                     : {basic['mode']}")
        self.print_item(f"Dimensions                     : {basic['dimensions']}")
        
        if not metadata['camera_info'] and not metadata['settings_info'] and not metadata['raw_exif']:
            self.print_message("\nNo EXIF metadata found in this image", 0.03)
            return
        
        if metadata['camera_info']:
            self.print_section_header("CAMERA INFORMATION")
            for key, value in metadata['camera_info'].items():
                self.print_item(f"{key:30} : {value}")
        
        if metadata['settings_info']:
            self.print_section_header("CAMERA SETTINGS")
            for key, value in metadata['settings_info'].items():
                formatted_value = ExifParser.format_value(key, value)
                self.print_item(f"{key:30} : {formatted_value}")
        
        if metadata['gps_coords'][0] is not None:
            self.print_section_header("GPS LOCATION DATA")
            lat, lon = metadata['gps_coords']
            
            self.print_item(f"Latitude                       : {lat:.6f}°")
            self.print_item(f"Longitude                      : {lon:.6f}°")
            self.print_item(f"Coordinates                    : {lat:.6f}, {lon:.6f}")
            
            maps_link = GPSParser.get_maps_link(lat, lon)
            if maps_link:
                self.print_item(f"Google Maps                    : {maps_link}")
            
            for key, value in metadata['gps_info'].items():
                if key not in ['GPSLatitude', 'GPSLongitude', 'GPSLatitudeRef', 'GPSLongitudeRef']:
                    self.print_item(f"{key:30} : {str(value)}")
        
        if metadata['raw_exif']:
            self.print_section_header("RAW EXIF DATA (ALL TAGS)")
            
            sorted_tags = sorted(metadata['raw_exif'].items())
            
            for key, value in sorted_tags:
                formatted_value = ExifParser.format_value(key, value)
                self.print_item(f"{key:30} : {formatted_value}")
        
        total_tags = (
            len(metadata['camera_info']) +
            len(metadata['settings_info']) +
            len(metadata['raw_exif'])
        )
        
        self.print_message(f"\nExtracted {total_tags} EXIF tags", 0.02)
    
    def _print_slow(self, text: str, delay: float):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
