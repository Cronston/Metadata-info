from pathlib import Path
from typing import Dict, Any, Tuple, Optional

from extractors import ImageExtractor
from parsers import GPSParser, ExifParser


class ExifService:
    
    def __init__(self):
        self.gps_parser = GPSParser
        self.exif_parser = ExifParser
    
    def extract_metadata(self, file_path: Path) -> Dict[str, Any]:
        extractor = ImageExtractor(file_path)
        metadata = extractor.extract()
        return metadata
    
    def extract_gps_coordinates(self, metadata: Dict[str, Any]) -> Tuple[Optional[float], Optional[float]]:
        return metadata.get('gps_coords', (None, None))
    
    def has_metadata(self, metadata: Dict[str, Any]) -> bool:
        return bool(
            metadata.get('camera_info') or 
            metadata.get('settings_info') or 
            metadata.get('raw_exif')
        )
    
    def count_tags(self, metadata: Dict[str, Any]) -> int:
        return (
            len(metadata.get('camera_info', {})) +
            len(metadata.get('settings_info', {})) +
            len(metadata.get('raw_exif', {}))
        )
