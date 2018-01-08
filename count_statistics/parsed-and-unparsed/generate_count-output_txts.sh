#!/bin/bash

# Script prints the number of analyses per word rather than the analyses themselves

FILES="./ungipaghaghlanga"

for file in "$FILES"/*.in; do

	# output=${file%.in}.out	# For generating *.out output files
	output=${file%.in}.count	# For generating output count files

	echo "Processing ${file} to create ${output}..."

	while IFS= read -r line; do
		sent=$(echo "$line" | tr -d '[:punct:]' | tr '[:upper:]' '[:lower:]')

		declare -a 'a=('"$sent"')'

		# printf '%s\n\n' "$line" | sed 's/\t/ /g'
		for word in "${a[@]}"; do
			echo "$word"
			echo "$word" | flookup -x ./ess.fomabin | awk ' /^$/ { print; } /./ { printf("%d ", $0); }' | awk '{print gsub(/ /, "")} '
			# printf "\n"
		done
		printf '%s\n' '------------------------'

	done <"$file" > "$output"
done
