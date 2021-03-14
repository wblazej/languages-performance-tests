const {performance} = require('perf_hooks');
const ts = () => { return performance.now() }
const execution_time = (start, end) => { console.log(`${(end - start).toFixed(3)} ms`) }

let st = ts()

let numbers = []
for (let i = 0; i < 1000000; i++)
    numbers.push(Math.floor(Math.random() * 1000000) + 1)
    
let en = ts()
execution_time(st, en)