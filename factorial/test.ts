import { performance } from "perf_hooks";

const factorial = (n: number): number => {
    if (n < 0) return Number.NaN
    if (n == 0) return 1

    return n * factorial(n - 1)
}

const test = () => {
    for (let j = 0; j < 10 ** 4; j++)
        for (let i = 1; i <= 20; i++)
            factorial(i) 
}

let start = performance.now()

test()

console.log((performance.now() - start).toFixed(3))