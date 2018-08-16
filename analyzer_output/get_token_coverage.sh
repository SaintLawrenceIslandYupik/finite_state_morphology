#!/bin/bash

DIR="./all_2018-08-10"	# TODO: Change directory path here

for d in $DIR/*; do

	curr_dir="$(basename "$d")"

	# TODO: Toggle *.in files and count total as needed

	# IN_FILES="./txts/original_txts/$curr_dir"		# Original texts with foreign borrowings included 
	IN_FILES="./txts/txts_ess-only/$curr_dir.ess"	# Preprocessed texts with foreign borrowings removed

	ERR_FILES="$DIR/$curr_dir"

	sum_errors=$(find "$ERR_FILES"/*.errors -type f | xargs wc -l | tail -1 | awk '{print $1}') 

	# total=$(find "$IN_FILES"/*.in -type f | xargs wc -w | tail -1 | awk '{print $1}')	# Includes foreign borrowings in count
	total=$(cat "$IN_FILES"/*.in | tr -d "\[\]" | wc -w | tail -1 | awk '{print $1}')	# Counts Yupik words only

	let sum_correct=$( echo $((total - sum_errors)) )

	echo -ne "$curr_dir:\t"
	awk -v sum_errors="$sum_errors" -v total="$total" 'BEGIN{printf "%0.2f\n", (total-sum_errors)/total * 100}'
done
