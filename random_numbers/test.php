<?php

function test() {
    $n = 1000000;
    $numbers = [];

    for ($i = 0; $i < $n; $i++)
        $numbers[] = mt_rand(1, $n);

    return $numbers;
}

$start = microtime(true);

test();

echo number_format((microtime(true) - $start) * 1000, 3);

?>