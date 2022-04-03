# Languages performance tests
Python script that runs performance tests for few programming languages. All the tests are based on the same problems solved in different programming languages. The scripts runs few attepmts of particular solutions, takes execution time and calculates the average execution time for specific languages.

## Run tests
Before running tests you need to install all the interpreters and compilers for used languages. The following interpreters/compilers are required: `g++`, `gcc`, `node`, `npx ts-node`, `ruby`, `php`, `java`, `python3`, `pypy3`. Example installation for Ubunutu:
```
sudo apt update -y
sudo apt install g++ gcc nodejs npm ruby php default-jre pypy3 -y
npm install @types/node typescript ts-node perf_hooks --save-dev
```

To run tests you need `pip3` and `python3` with version at least `v3.9`. Example installation for Ubuntu:
```
sudo apt update -y
sudo apt install python3.9 python3-pip -y
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9
python3 -V
pip3 --version
```

With that being said, just run tests:
```
git clone https://github.com/wblazej/languages-performance-tests
cd languages-performance-tests
pip3 install -r requirements.txt
python3 main.py
```

## Current problems
- `random_numbers` - generates `1 mln` random numbers from range `1` to `1 mln`
- `fibonacci_sequence` - calculates [Fibonacci Sequence](https://en.wikipedia.org/wiki/Fibonacci_number) for `30`
- `factorial` - calculates [Factorial](https://en.wikipedia.org/wiki/Factorial) `10 000` times for range of numbers from `1` to `20`

## Usage
See help page
```
python3 main.py --help
```

## Example output
Tests performed on Apple M1 CPU
```
-- Results for random_numbers --

1. C            7.406 ms
2. TypeScript   18.212 ms
3. JavaScript   19.667 ms
4. C++          25.936 ms
5. PHP          32.485 ms
6. Java         57.1 ms
7. Ruby         107.886 ms
8. Python       411.12 ms


-- Results for fibonacci_sequence --

1. Java         2.6 ms
2. C            4.453 ms
3. C++          4.523 ms
4. TypeScript   8.923 ms
5. JavaScript   9.079 ms
6. Ruby         56.912 ms
7. PHP          61.481 ms
8. Python       150.601 ms


-- Results for factorial --

1. C            3.262 ms
2. Java         4.0 ms
3. C++          4.063 ms
4. JavaScript   16.368 ms
5. TypeScript   18.235 ms
6. PHP          49.862 ms
7. Ruby         63.57 ms
8. Python       192.094 ms
```
