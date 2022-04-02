from colorama import Fore, Style


class Config:
    K_HELP = 'Execution attempts on every language. The result is the average of all attempts.'\
            'More attempts gives more accurate results. By default is set to 10.'
    BIN_PATH_NOT_FOUND_ERROR = f'{Fore.RED}{Style.BRIGHT}[*] {Fore.WHITE}interpreter_name {Fore.RED}'\
                                'not found. Please install it and try again.'