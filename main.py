import argparse
from src.config import Config
from src.bin_path_not_found import BinPathNotFound
from src.get_paths import get_paths
from src.run_tests import run_tests


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', help=Config.K_HELP, type=int, required=False, default=10)
    args = parser.parse_args()

    interpreters_needed = ['python3', 'node', 'npx', 'g++', 'gcc', 'ruby', 'php', 'java']
    tests = ['random_numbers', 'fibonacci_sequence', 'factorial']

    try:
        paths = get_paths(interpreters_needed)
    except BinPathNotFound as e:
        print(Config.BIN_PATH_NOT_FOUND_ERROR.replace('interpreter_name', e.interpreter_name))
        exit(1)

    results = run_tests(tests, paths, k=args.k)

    for test_name, test_results in results.items():
        print(f'\n-- Results for {test_name} --\n')
        for i, (lang, result) in enumerate(test_results.items()):
            print('{}. {:12} {} ms'.format(i + 1, lang, result))
