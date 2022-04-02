import subprocess
from src.bin_path_not_found import BinPathNotFound

def get_bin_path(interpreter: str):
    out = subprocess.run(f'which {interpreter}', capture_output=True, shell=True)

    path = out.stdout.decode().strip()

    if not path:
        raise BinPathNotFound(interpreter_name=interpreter)

    return path

def get_paths(interpreters: list[str]):
    paths = {}

    for interpreter in interpreters:
        paths[interpreter] = get_bin_path(interpreter)

    return paths