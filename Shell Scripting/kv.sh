#!/bin/bash
storeInfo(){
    current_time=$(date "+%d/%m/%Y-%H:%M:%S")
    echo "$1_$current_time $2" >> store.txt
}
displayInfo(){
    echo "Name OrderID"
    cat store.txt
}
getOrderID(){
    echo "OrderID's found are"
    userName=$1
    cat store.txt | awk "/^$userName/ "' { print $2 }'

    echo -n "$1 ordered "
    grep $1 file.txt -o | wc -l | tr -d '\n'
    echo -n " times"
    }
if [[ $1 = storeInfo ]]
then
    storeInfo $2 $3
elif [[ $1 = displayInfo ]]
then
    displayInfo $2 $3
else
    getOrderID $2
fi