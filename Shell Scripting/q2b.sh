
#!/bin/bash

file_names=$(ls ./images_folder)

while read -ra line; 
do
    for word in "${line[@]}"
    do
        # echo "word is $word"
        timestamp="$(echo $word | awk -F_ '{ print $2 }')"
        # echo "timestamp is $timestamp"
        suffix="$(echo $word | awk -F_ '{ print $3 }')"
        imageNumber="$(echo $suffix | awk -F. '{ print $1 }')"
        # echo "imageNumber is $imageNumber"

        record="$(echo $word | awk -F_ '{ print $2 }')"
        year="$(echo $record | awk -F- '{ print $1 }')"
        day="$(echo $record | awk -F- '{ print $2 }')"
        month="$(echo $record | awk -F- '{ print $3 }')"
        
        imageName="$day-$month-20$year""_""$imageNumber.jpg"
        
        mv ./images_folder/$word "./images_folder/$imageName"

    done
done <<< "$file_names"