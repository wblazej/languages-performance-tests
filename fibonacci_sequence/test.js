const {performance} = require('perf_hooks');

const fibonacci_sequence = (n) =>
    n > 1 ? fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2) : n

const test = () => fibonacci_sequence(30)

let start = performance.now()

test()

console.log((performance.now() - start).toFixed(3))