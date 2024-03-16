cat sample.txt | awk '{sum+=$2} END {print sum}'

