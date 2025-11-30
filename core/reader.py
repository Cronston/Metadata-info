from pathlib import Path
from typing import Tuple, Optional


class FileReader:
    
    SUPPORTED_FORMATS = ['.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.gif']
    
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
    
    def validate(self) -> Tuple[bool, Optional[str]]:
        if not self.file_path.exists():
            return False, f"File not found: {self.file_path}"
        
        if not self.is_supported_format():
            ext = self.file_path.suffix.lower()
            supported = ', '.join(self.SUPPORTED_FORMATS)
            return False, f"Unsupported file type: {ext}\nSupported formats: {supported}"
        
        return True, None
    
    def is_supported_format(self) -> bool:
        return self.file_path.suffix.lower() in self.SUPPORTED_FORMATS
    
    def get_file_info(self) -> dict:
        return {
            'path': str(self.file_path),
            'name': self.file_path.name,
            'extension': self.file_path.suffix.lower(),
            'size': self.file_path.stat().st_size if self.file_path.exists() else 0
        }

    @classmethod
    def get_supported_files(cls, folder_path: str) -> list[Path]:
        path = Path(folder_path)
        if not path.exists() or not path.is_dir():
            return []
            
        files = []
        for file_path in path.iterdir():
            if file_path.is_file() and file_path.suffix.lower() in cls.SUPPORTED_FORMATS:
                files.append(file_path)
        
        return sorted(files)
