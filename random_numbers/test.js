const {performance} = require('perf_hooks');

const test = () => {
    let n = 1000000
    let numbers = []

    for (let i = 0; i < n; i++)
        numbers.push(Math.floor(Math.random() * n) + 1)
}

let start = performance.now()

test()

console.log((performance.now() - start).toFixed(3))