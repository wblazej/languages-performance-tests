import { performance } from "perf_hooks"

const fibonacci_sequence = (n: number): number =>
    n > 1 ? fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2) : n

const test = () => fibonacci_sequence(30)

let start = performance.now()

test()

console.log((performance.now() - start).toFixed(3))