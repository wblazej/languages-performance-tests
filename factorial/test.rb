require 'benchmark'

def factorial(n)
  if n == 0
    1
  else
    n * factorial(n-1)
  end
end

def test
    10000.times do
        1..21.times do |i|
            factorial(i)
        end
    end
end

time = Benchmark.measure { test }
puts (time.real * 1000).round(3)