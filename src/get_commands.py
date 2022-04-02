def get_commands(name: str, interpreters_paths: dict[str, str]):
    return [
        {'lang': 'Python', 'command': f'{interpreters_paths["python3"]} {name}/test.py'},
        {'lang': 'JavaScript', 'command': f'{interpreters_paths["node"]} {name}/test.js'},
        {'lang': 'TypeScript', 'command': f'{interpreters_paths["npx"]} ts-node {name}/test.ts'},
        {'lang': 'C++', 'command': f'{interpreters_paths["g++"]} {name}/test.cpp -o test.out && ./test.out && rm test.out'},
        {'lang': 'C', 'command': f'{interpreters_paths["gcc"]} {name}/test.c -o test.out && ./test.out && rm test.out'},
        {'lang': 'Ruby', 'command': f'{interpreters_paths["ruby"]} {name}/test.rb'},
        {'lang': 'PHP', 'command': f'{interpreters_paths["php"]} {name}/test.php'},
        {'lang': 'Java', 'command': f'{interpreters_paths["java"]} {name}/test.java'}
    ]