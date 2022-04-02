<?php

function factorial($number) {
    if ($number <= 1) 
        return 1;

    return $number * factorial($number - 1);  
}

function test() {
    for ($j = 0; $j < 10000; $j++)
        for ($i = 1; $i <= 20; $i++)
            factorial($i);
}

$start = microtime(true);

test();

echo number_format((microtime(true) - $start) * 1000, 3);

?>