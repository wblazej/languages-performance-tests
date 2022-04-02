def get_commands(name: str, interpreters_paths: dict[str, str]):
    commands = []

    if interpreters_paths['python3'] is not None:
        commands.append({'lang': 'Python', 'command': f'{interpreters_paths["python3"]} {name}/test.py'})

    if interpreters_paths['node'] is not None:
        commands.append({'lang': 'JavaScript', 'command': f'{interpreters_paths["node"]} {name}/test.js'})

    if interpreters_paths['npx'] is not None:
        commands.append({'lang': 'TypeScript', 'command': f'{interpreters_paths["npx"]} ts-node {name}/test.ts'})

    if interpreters_paths['g++'] is not None:
        commands.append({'lang': 'C++', 'command': f'{interpreters_paths["g++"]} {name}/test.cpp -o test.out && ./test.out && rm test.out'},)

    if interpreters_paths['gcc'] is not None:
        commands.append({'lang': 'C', 'command': f'{interpreters_paths["gcc"]} {name}/test.c -o test.out && ./test.out && rm test.out'})

    if interpreters_paths['ruby'] is not None:
        commands.append({'lang': 'Ruby', 'command': f'{interpreters_paths["ruby"]} {name}/test.rb'})

    if interpreters_paths['php'] is not None:
        commands.append({'lang': 'PHP', 'command': f'{interpreters_paths["php"]} {name}/test.php'})

    if interpreters_paths['java'] is not None:
        commands.append({'lang': 'Java', 'command': f'{interpreters_paths["java"]} {name}/test.java'})

    if interpreters_paths['pypy3'] is not None:
        commands.append({'lang': 'PyPy3', 'command': f'{interpreters_paths["pypy3"]} {name}/test.py'})

    return commands