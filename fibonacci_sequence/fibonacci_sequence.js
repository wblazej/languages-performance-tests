const {performance} = require('perf_hooks');
const ts = () => { return performance.now() }
const execution_time = (start, end) => { console.log(`${(end - start).toFixed(3)} ms`) }

const fibonacci_sequence = (n) => {
    if (n < 0) return Number.NaN
    return n > 1 ? fibonacci_sequence(n -1) + fibonacci_sequence(n -2) : n
}

let st = ts()
fibonacci_sequence(30)
let en = ts()
execution_time(st, en)