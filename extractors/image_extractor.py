from PIL import Image, UnidentifiedImageError
from PIL.ExifTags import TAGS, GPSTAGS
from pathlib import Path

from parsers import GPSParser, ExifParser
from utils import format_file_size


class ImageExtractor:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.image = None
        self.exif_data = None
    
    def extract(self):
        try:
            self.image = Image.open(self.file_path)
            self.exif_data = self.image._getexif()
            
            metadata = {
                'basic_info': self._get_basic_info(),
                'camera_info': {},
                'settings_info': {},
                'gps_info': {},
                'gps_coords': (None, None),
                'raw_exif': {}
            }
            
            if self.exif_data:
                self._parse_exif(metadata)
            
            return metadata
            
        except FileNotFoundError:
            raise
        except UnidentifiedImageError:
            raise
        except Exception as e:
            raise Exception(f"Error extracting image metadata: {e}")
    
    def _get_basic_info(self):
        return {
            'file_name': self.file_path.name,
            'file_size': format_file_size(self.file_path.stat().st_size),
            'format': self.image.format,
            'mode': self.image.mode,
            'width': self.image.width,
            'height': self.image.height,
            'dimensions': f"{self.image.width} x {self.image.height}"
        }
    
    def _parse_exif(self, metadata):
        exif_dict = {}
        gps_data = None
        
        for tag_id, value in self.exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            
            if tag == "GPSInfo":
                gps_data = value
            else:
                exif_dict[tag] = value
        
        camera_info, settings_info, raw_exif = ExifParser.categorize_tags(exif_dict)
        
        metadata['camera_info'] = camera_info
        metadata['settings_info'] = settings_info
        metadata['raw_exif'] = raw_exif
        
        if gps_data:
            gps_info, lat, lon = GPSParser.parse(gps_data, GPSTAGS)
            metadata['gps_info'] = gps_info
            metadata['gps_coords'] = (lat, lon)
