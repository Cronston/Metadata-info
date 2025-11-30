import time
from pathlib import Path

from PIL import UnidentifiedImageError

from config import AnalysisConfig
from core.reader import FileReader
from core.exif_service import ExifService
from output import OutputFormatter, FileSaver, ConsoleWriter


class MetadataAnalyzer:    
    def __init__(self, config: AnalysisConfig):
        self.config = config
        self.reader = FileReader(config.file_path)
        self.service = ExifService()
        self.console_writer = ConsoleWriter(
            quiet_mode=config.quiet_mode,
            typing_enabled=config.typing_enabled
        )
        self.formatter = OutputFormatter()
        self.file_saver = FileSaver(config.save_dir)
    
    def analyze(self):
        self._analyze_single_file(Path(self.config.file_path))

    def analyze_folder(self):
        folder_path = self.config.folder_path
        if not folder_path:
            print("\nNo folder path provided")
            return

        files = FileReader.get_supported_files(folder_path)
        
        if not files:
            print(f"\nNo supported images found in: {folder_path}")
            return
            
        print(f"\nFound {len(files)} images in {folder_path}")
        print("=" * 60)
        
        for i, file_path in enumerate(files, 1):
            print(f"\n[{i}/{len(files)}] Processing: {file_path.name}")
            self._analyze_single_file(file_path)
            print("-" * 60)
            
    def _analyze_single_file(self, file_path: Path):
        reader = FileReader(str(file_path))
        is_valid, error_message = reader.validate()
        
        if not is_valid:
            print(f"\n{error_message}")
            return
        
        try:
            metadata = self.service.extract_metadata(file_path)
        except FileNotFoundError:
            print("\nFile not found")
            return
        except UnidentifiedImageError:
            print("\nInvalid or corrupted image")
            return
        except Exception as e:
            print(f"\nError extracting metadata: {e}")
            return
        
        self.console_writer.print_metadata(metadata)
        
        if self.config.save_enabled:
            self._save_results(metadata, file_path)
    
    def _save_results(self, metadata: dict, file_path: Path):
        print()
        
        if self.config.custom_output:
            output_file = self.file_saver.save_to_custom_path(
                self.formatter.get_output_lines(),
                self.config.custom_output
            )
        else:
            output_file = self.file_saver.save(
                self.formatter.get_output_lines(),
                file_path.name
            )
        
        if output_file:
            if self.config.typing_enabled:
                self._print_slow(f"Results saved to: {output_file}", 0.02)
            else:
                print(f"Results saved to: {output_file}")
    
    def _print_slow(self, text: str, delay: float):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
