#!/bin/bash

FILES="end-of-chapt-exercises"


# Runs each *.in file through the analyzer and copies the output to a *.out file
for file in "$FILES"/*.in; do

	output=${file%.in}.out


	echo "Processing ${file} to create ${output}..."

	while IFS= read -r line; do
		sent=$(echo "$line" | tr -d '[:punct:]' | tr '[:upper:]' '[:lower:]')

		declare -a 'a=('"$sent"')'

		printf '%s\n\n' "$line" | sed 's/\t/ /g'
		for word in "${a[@]}"; do
			echo "$word" | flookup -w "" ./ess.fomabin
			printf "\n"
		done
		printf '%s\n' '------------------------'

	done <"$file" > "$output".out
done


# Prints all words that were not successfully parsed
for file in "$FILES"/*.out; do

	filename=$(echo "$file") # | cut -d"/" -f8 | cut -d\. -f1)

	while IFS= read -r line; do
		if [[ $line == *"?" ]]; then
			echo "$filename: $line"
		fi
	done <"$file"
done




#######
