#!/bin/bash
weights=(1 1 1 1 1)
for ((i=2; i<=$#; i++)); do
    if [ "$i" -eq "7" ]; then
        break
    fi
    weights[i-2]=${!i}
done

num_students=0
total_weight=0
for i in {0..4}; do
    ((total_weight+=weights[i]))
done

score_sum=0
while IFS=',' read -ra line_array; do
    ((num_students++))
    score=0
    for i in {1..5}; do
        ((score+=line_array[i]*weights[i-1]))
    done
    result=$((score * 1000 / total_weight))
    score_sum=$((score_sum + result))
done < <(tail -n +2 "$1")
score_average=$((score_sum / num_students))
score_average_float=$(echo "scale=6; $score_average/1000" | bc)
echo $score_average_float
int_score=$(awk "BEGIN {printf \"%d\", $score_average_float}")
echo "Weighted average is $int_score"
