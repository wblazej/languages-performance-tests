const {performance} = require('perf_hooks');
const ts = () => { return performance.now() }
const execution_time = (start, end) => { console.log(`${(end - start).toFixed(3)} ms`) }

const factorial = (n) => {
    if (n < 0) return Number.NaN
    if (n === 0) return 1

    return n * factorial(n - 1)
}

let st = ts()

for (let i = 0; i < 100000; i++)
    factorial(25)

let en = ts()
execution_time(st, en)