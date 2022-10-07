#!/bin/bash
while read -ra line; 
do
    for word in "${line[@]}";
    do

        record="$(echo $word | awk -F, '{ print $3 }')"
        
        if [[ $record == "Timestamp" ]]
        then
            echo "FirstName, LastName, Date, Time" > final.csv
        else
            first_name="$(echo $word | awk -F, '{ print $1 }')"
            second_name="$(echo $word | awk -F, '{ print $2 }')"

            booking_date="$(echo $record | awk -F_ '{ print $1 }')"
            booking_time="$(echo $record | awk -F_ '{ print $2 }')"
            day="$(echo $booking_date | awk -F/ '{ print $3 }')"
            month="$(echo $booking_date | awk -F/ '{ print $2 }')"
            year="$(echo $booking_date | awk -F/ '{ print $1 }')"
            hour="$(echo $booking_time | awk -F: '{ print $1 }')"
            minute="$(echo $booking_time | awk -F: '{ print $2 }')"
            second="$(echo $booking_time | awk -F: '{ print $3 }')"
            
            if [[ $month == "01" ]]
            then
                month_text="January"
            elif [[ $month == "02" ]]
            then
                month_text="February"
            elif [[ $month == "03" ]]
            then
                month_text="March"
            elif [[ $month == "04" ]]
            then
                month_text="April"
            elif [[ $month == "05" ]]
            then
                month_text="May"
            elif [[ $month == "06" ]]
            then
                month_text="June"
            elif [[ $month == "07" ]]
            then
                month_text="July"
            elif [[ $month == "08" ]]
            then
                month_text="August"
            elif [[ $month == "09" ]]
            then
                month_text="September"
            elif [[ $month == "10" ]]
            then
                month_text="October"
            elif [[ $month == "11" ]]
            then
                month_text="November"
            elif [[ $month == "12" ]]
            then
                month_text="December"
            fi

            if [[ $hour == "00" || $hour == "01" || $hour == "02" || $hour == "03" || $hour == "04" || $hour == "05" || $hour == "06" || $hour == "07" || $hour == "08" || $hour == "09" || $hour == "10" || $hour == "11" ]]
            then
                echo "$first_name,$second_name,$day $month_text $year,$hour:$minute" >> final.csv
            else
                echo "$first_name,$second_name,$day $month_text $year,$(($hour-12)):$minute" >> final.csv
            fi
        fi
    done;
done < guests.csv