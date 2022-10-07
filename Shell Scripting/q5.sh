#!/bin/bash

while read -ra line; 
do
    for word in "${line[@]}"
    do
        # use of sed command to read only specific lines from range 2,20 etc. This way we can regulate the number of 
        # keys to read
        # output of sed command is passed to awk command for searching for a pattern which begins
        # with $word and ends with $word, basically the $word itself. Then ORS is used to set the escape 
        # character, which is \n otherwise, is changed to space. Then we search for $word and print its
        # corresponding value for the key 
        sed -n -e 2,$3p key.txt | awk -F- -v pat="^$word$" 'BEGIN { ORS=" " };$1~pat{ print $2 }'
    done
done < $2