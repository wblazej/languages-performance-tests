import subprocess
from src.get_commands import get_commands
import sys
from colorama import Fore


def write_dots(count: int):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write('.' * count)
    sys.stdout.flush()

def run_tests(tests: list[str], interpreters_paths: list[str], k: int):
    tests_results = {}

    for test_name in tests:
        print(f'\n\n\n{Fore.CYAN}> Running tests for {test_name}{Fore.RESET}')
        results = {}

        for c in get_commands(test_name, interpreters_paths):
            print(f'\n\nTesting {c["lang"]}')
            attempts = []

            for i in range(k):
                out = subprocess.run(c['command'], capture_output=True, shell=True)
                attempts.append(float(out.stdout.decode().strip()))
                write_dots(i + 1)

            results[c['lang']] = round(sum(attempts) / len(attempts), 3)

        tests_results[test_name] = {k: v for k, v in sorted(results.items(), key=lambda item: item[1])}

    return tests_results