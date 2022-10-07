# #!/bin/bash

# pattern=''
# word=''
# flag=0
# while read -ra line; 
# do
#     for word in "${line[@]}"
#     do
#         if [[ $word == "#@$" ]]
#         then
#             flag=1
#             echo "inside inside inside"
#         fi
#         if [[ flag == 1 ]]
#         then
#             pattern1=$word
#             echo "pattern1 is $pattern1"
#         fi
#         echo "$word"
#     done;
# done < sample.txt
# #make word1 to store value
# #if flag!=1 and word1 !=start, - 6 ifs 1st word and pattern 2 ifs  
# echo "Last Word found: $word"
# echo "Last Pattern found: $pattern"
#!/bin/sh

flag1=0
word1="word"
word3="word"
word5="word"
pattern1="pattern"
stage=0

while read -ra line; 
do
    for word in "${line[@]}"
    do
        # word and pattern number 1
        if [[ $word == "#@$" ]]
        then
            flag1=1
            pattern1=$word
           # echo "pattern1 is $pattern1"
            stage=1
        fi
        if [[ $word != $pattern1 && $flag1 == 1 ]]
        then
            flag1=0
            word1=$word
           # echo "word1 is $word1"
            stage=2
        fi

        if [[ $stage == 9 ]] && [[ $word =~ ^"!".* || $word =~ ^"@".* || $word =~ ^"#".* || $word =~ ^"$".* || $word =~ ^"%".* || $word =~ ^"^".* || $word =~ ^"&".* || $word =~ ^"*".* ]]
        then
            pattern4=$word
            #echo "pattern4 is $pattern4"
            echo "Last Pattern found: $pattern4"
        fi

        if [[ $stage == 8 && $word == $word5 ]]
        then
            word6=$word
            #echo "word6 is $word6"
            echo "Last Word found: $word6"
            stage=9
        fi
        if [[ $stage == 7 && $word5 == "word" ]]
        then
            word5=$word
           # echo "word5 is $word5"
            stage=8
        fi

        if [[ $stage == 6 ]] && [[ $word =~ ^"!".* || $word =~ ^"@".* || $word =~ ^"#".* || $word =~ ^"$".* || $word =~ ^"%".* || $word =~ ^"^".* || $word =~ ^"&".* || $word =~ ^"*".* ]]
        then
            pattern3=$word
           # echo "pattern3 is $pattern3"
            stage=7
        fi

        if [[ $stage == 5 && $word == $word3 ]]
        then
            word4=$word
           # echo "word4 is $word4"
            stage=6
        fi
        if [[ $stage == 4 && $word3 == "word" ]]
        then
            word3=$word
           # echo "word3 is $word3"
            stage=5
        fi
        
        if [[ $stage == 2 && $word == $word1 ]] 
        then
            stage=3
            word2=$word
            #echo "word2 is $word2"
        fi
        if [[ $stage == 3 ]] && [[ $word =~ ^"!".* || $word =~ ^"@".* || $word =~ ^"#".* || $word =~ ^"$".* || $word =~ ^"%".* || $word =~ ^"^".* || $word =~ ^"&".* || $word =~ ^"*".* ]]
        then
            pattern2=$word
           # echo "pattern2 is $pattern2"
            stage=4
        fi
    done;
done < q2-sample.txt
