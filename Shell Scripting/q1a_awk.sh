#!/bin/awk
$awk '{for(i = 1; i <= NF; i++) {a[$i]++}} END {for(k in a) if(a[k] == 1){counter++} print counter}' $1