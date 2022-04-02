<?php

function fibonacci_sequence($n) {
    if ($n <= 1)
        return 1;

    return fibonacci_sequence($n - 1) + fibonacci_sequence($n - 2);    
}

function test() {
    fibonacci_sequence(30);
}

$start = microtime(true);

test();

echo number_format((microtime(true) - $start) * 1000, 3);

?>