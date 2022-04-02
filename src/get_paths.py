import subprocess
from src.bin_path_not_found import BinPathNotFound

def get_bin_path(interpreter: str, ignore_missing: bool):
    out = subprocess.run(f'which {interpreter}', capture_output=True, shell=True)

    path = out.stdout.decode().strip()

    if not path and not ignore_missing:
        raise BinPathNotFound(interpreter_name=interpreter)

    return path if path else None

def get_paths(interpreters: list[str], ignore_missing: bool):
    paths = {}

    for interpreter in interpreters:
        paths[interpreter] = get_bin_path(interpreter, ignore_missing)

    return paths