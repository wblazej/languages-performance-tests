## Programming languages execution time test
Five tests performed on one computer with three different programming languages Python, C++, JavaScript and alternative implementation of Python - PyPy.<br><br>
PyPy features - https://www.pypy.org/features.html <br><br>
All test has been performed on CPU: `Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz`

### Results
| Test name | Python | PyPy (python) | C++ | JavaScript (node)
| :---: | :---: | :---: | :---: | :---: |
| Empty file | 0.004 ms | 0.321 ms | 0.001 ms | 0.013 ms |
| Factorial | 253.755 ms | 35.812 ms | 7.38 ms | 19.276 ms |
| Fibbonacci sequance | 217.62 ms | 27.165 ms | 5.973 ms | 10.764 ms |
| Outputting | 27.071 ms | 40.638 ms | 18.182 ms | 135.018 ms |
| Random numbers | 520.865 ms | 71.071 ms | 26.019 ms | 27.188 ms |

For more details about each test, see folder with test name.
