from pathlib import Path
from datetime import datetime


class FileSaver:
    
    def __init__(self, save_dir="./save"):
        self.save_dir = Path(save_dir)
        self.ensure_directory()
    
    def ensure_directory(self):
        self.save_dir.mkdir(exist_ok=True)
    
    def generate_filename(self, original_filename):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        stem = Path(original_filename).stem
        filename = f"metadata_{stem}_{timestamp}.txt"
        return self.save_dir / filename
    
    def save(self, output_lines, original_filename):
        try:
            output_file = self.generate_filename(original_filename)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(output_lines))
            
            return output_file
        except Exception as e:
            print(f"Error saving file: {e}")
            return None
    
    def save_to_custom_path(self, output_lines, custom_path):
        try:
            output_file = Path(custom_path)
            
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(output_lines))
            
            return output_file
        except Exception as e:
            print(f"Error saving file: {e}")
            return None
