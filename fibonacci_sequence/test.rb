require 'benchmark'

def fibonacci_sequence(n)
  return n if n <= 1
  fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)
end

def test
    fibonacci_sequence(30)
end

time = Benchmark.measure { test }
puts (time.real * 1000).round(3)