sed -nr '/^[^@]+@[^.^@]+\.\w+$/p' emails.txt > valid1.txt
sed -nr '/^[^@]+@[^.^@]+\.\w+\.\w+$/p' emails.txt >> valid1.txt
sed '/\.\./d' valid1.txt >> valid.txt
