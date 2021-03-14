const {performance} = require('perf_hooks');
const ts = () => { return performance.now() }
const execution_time = (start, end) => { console.log(`${(end - start).toFixed(3)} ms`) }

let st = ts()
let en = ts()
execution_time(st, en)