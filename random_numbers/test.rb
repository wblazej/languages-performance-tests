require 'benchmark'

def test
    n = 1000000
    Array.new(n) { rand(1..n) }
end

time = Benchmark.measure { test }
puts (time.real * 1000).round(3)