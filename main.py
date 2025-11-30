import sys
import time
import argparse

from config import AnalysisConfig
from core import MetadataAnalyzer
from utils.banner import print_banner, print_slow

__version__ = "1.0.0"


def setup_argument_parser():
    parser = argparse.ArgumentParser(
        description='Metadata Extractor - OSINT CLI Tool for extracting metadata from images',
        epilog='''
Examples:
  %(prog)s -i photo.jpg                    # Extract metadata from photo.jpg
  %(prog)s --folder images/                # Batch process all images in folder
  %(prog)s -i photo.jpg -o result.txt      # Save to custom output file
  %(prog)s -i photo.jpg --no-save          # Don't save results to file
  %(prog)s -i photo.jpg --quiet            # Minimal output (no banner, no typing)
  %(prog)s -i photo.jpg --no-typing        # Disable typing effect
  %(prog)s -i photo.jpg --no-banner        # Skip ASCII banner
  %(prog)s --interactive                   # Interactive mode (prompts for input)

For more information, visit: https://github.com/Cronston/Metadata-info
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '-i', '--input',
        type=str,
        metavar='FILE',
        help='Path to the image file to analyze'
    )
    
    parser.add_argument(
        '-f', '--folder',
        type=str,
        metavar='DIR',
        help='Path to folder containing images to analyze'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        metavar='FILE',
        help='Custom output file path (default: auto-generated in ./save/)'
    )
    
    parser.add_argument(
        '--no-save',
        action='store_true',
        help='Don\'t save results to file (only display on screen)'
    )
    
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Minimal output mode (no banner, no typing effect)'
    )
    
    parser.add_argument(
        '--no-typing',
        action='store_true',
        help='Disable typing effect (but keep banner)'
    )
    
    parser.add_argument(
        '--no-banner',
        action='store_true',
        help='Skip ASCII art banner'
    )
    
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'%(prog)s {__version__}'
    )

    parser.add_argument(
        '--interactive',
        action='store_true',
        help='Run in interactive mode'
    )
    
    return parser


def main():
    parser = setup_argument_parser()
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
        
    args = parser.parse_args()
    
    if args.input or args.folder:
        config = AnalysisConfig.from_args(args)
        
        if config.show_banner:
            print_banner(config.typing_enabled)
        
        analyzer = MetadataAnalyzer(config)
        
        if config.folder_path:
            analyzer.analyze_folder()
        else:
            if not config.quiet_mode and config.typing_enabled:
                print_slow("Analyzing image...", delay=0.03)
                time.sleep(0.3)
            analyzer.analyze()
    
    elif args.interactive:
        print_banner(typing_enabled=True)
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
        
        config = AnalysisConfig.interactive(file_path)
        analyzer = MetadataAnalyzer(config)
        analyzer.analyze()
        
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
