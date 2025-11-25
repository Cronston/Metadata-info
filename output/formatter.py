from colorama import Fore, Style


class OutputFormatter:
    
    def __init__(self):
        self.output_lines = []
    
    def print_header(self, text):
        line = "=" * 70
        self.output_lines.append(line)
        self.output_lines.append(text)
        self.output_lines.append(line)
        
        if not self.typing_effect:
            print(f"\n{Fore.CYAN}{Style.BRIGHT}{line}")
            print(f"{Fore.CYAN}{Style.BRIGHT}{text}")
            print(f"{Fore.CYAN}{Style.BRIGHT}{line}{Style.RESET_ALL}")
    
    def print_section(self, title):
        self.output_lines.append(f"\n{title}")
        self.output_lines.append("-" * 70)
        
        print()
        self._print_slow(title, f"{Fore.YELLOW}{Style.BRIGHT}")
        self._print_slow("-" * 70, f"{Fore.YELLOW}")
    
    def print_item(self, key, value, highlight=False):
        self.output_lines.append(f"{key:30} : {value}")
        
        if highlight:
            self._print_slow(f"{key:30} : {value}", f"{Fore.GREEN}{Style.BRIGHT}")
        else:
            self._print_slow(f"{key:30} : {value}", f"{Fore.WHITE}")
    
    def print_warning(self, text):
        self.output_lines.append(f"{text}")
        self._print_slow(f"{text}", f"{Fore.YELLOW}")
    
    def print_error(self, text):
        self.output_lines.append(f" {text}")
        self._print_slow(f" {text}", f"{Fore.RED}")
    
    def print_success(self, text):
        self.output_lines.append(f" {text}")
        self._print_slow(f" {text}", f"{Fore.GREEN}")
    
    def get_output_lines(self):

        return self.output_lines
    
    def clear(self):
        self.output_lines = []
