
#!/bin/bash

if [[ $2 == "-paras" ]]
then
    awk 'BEGIN { ORS=" " } {p=1} //{p++} END{print p, " paragraphs"}' RS="[[\n]]" $1
elif [[ $2 == "-words" ]]
then
    awk ' BEGIN { ORS=" " } {i=0; count=0; while (i<NR) { count+=NF; i++;}} 
    END {print count " words"}' $1
elif [[ $2 == "-characters" ]]
then
    space=$(expr length "$1" - length `echo "$1" | sed "s/ //g"`)
    total_char=$(awk '{t+=length($0)}END{print t}' $1 )
    echo -n "$total_char characters"
elif [[ $2 == "-lines" ]]
then    
    awk 'BEGIN { ORS=" " }END{print NR " lines"}' $1
else
    space=$(expr length "$1" - length `echo "$1" | sed "s/ //g"`)
    total_char=$(awk '{t+=length($0)}END{print t}' $1 )
    echo -n "$total_char characters, "

    awk 'BEGIN { ORS=" " }END{print NR " lines,"}' $1
    awk 'BEGIN { ORS=" " } {p=1} //{p++} END{print p, " paragraphs,"}' RS="[[\n]]" $1

    awk ' BEGIN { ORS=" " } {i=0; count=0; while (i<NR) { count+=NF; i++;}} 
    END {print count " words "}' $1
fi