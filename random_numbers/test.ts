import { performance } from "perf_hooks";

const test = () => {
    let n = 10 ** 6
    let numbers = []

    for (let i = 0; i < n; i++)
        numbers.push(Math.floor(Math.random() * n) + 1)
}

let start = performance.now()

test()

console.log((performance.now() - start).toFixed(3))