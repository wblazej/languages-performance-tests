import subprocess
from src.get_commands import get_commands


def run_tests(tests: list[str], interpreters_paths: list[str], k: int):
    tests_results = {}

    for test_name in tests:
        print(f'\n> Running tests for {test_name}')
        results = {}

        for c in get_commands(test_name, interpreters_paths):
            print(f'\nTesting {c["lang"]}')
            attempts = []

            for i in range(k):
                out = subprocess.run(c['command'], capture_output=True, shell=True)
                exec_time = float(out.stdout.decode().strip())
                attempts.append(exec_time)
                print(f'Test {i + 1}: {exec_time} ms')

            results[c['lang']] = round(sum(attempts) / len(attempts), 3)

        tests_results[test_name] = {k: v for k, v in sorted(results.items(), key=lambda item: item[1])}

    return tests_results