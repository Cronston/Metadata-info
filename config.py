from dataclasses import dataclass
from typing import Optional
from argparse import Namespace


@dataclass
class AnalysisConfig:
    
    file_path: str
    folder_path: Optional[str] = None
    save_dir: str = "./save"
    custom_output: Optional[str] = None
    quiet_mode: bool = False
    typing_enabled: bool = True
    save_enabled: bool = True
    show_banner: bool = True
    
    @classmethod
    def from_args(cls, args: Namespace) -> 'AnalysisConfig':
        quiet_mode = args.quiet
        typing_enabled = not args.no_typing and not args.quiet
        save_enabled = not args.no_save
        show_banner = not args.no_banner and not args.quiet
        
        return cls(
            file_path=args.input if args.input else "",
            folder_path=args.folder if hasattr(args, 'folder') and args.folder else None,
            save_dir="./save",
            custom_output=args.output if hasattr(args, 'output') and args.output else None,
            quiet_mode=quiet_mode,
            typing_enabled=typing_enabled,
            save_enabled=save_enabled,
            show_banner=show_banner
        )
    
    @classmethod
    def interactive(cls, file_path: str) -> 'AnalysisConfig':
        return cls(
            file_path=file_path,
            save_dir="./save",
            custom_output=None,
            quiet_mode=False,
            typing_enabled=True,
            save_enabled=True,
            show_banner=True
        )
