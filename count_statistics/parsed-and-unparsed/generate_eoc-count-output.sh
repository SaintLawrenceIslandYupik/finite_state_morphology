#!/bin/bash

# Script generates the number of analyses per word rather than the analyses themselves in the
# end of chapter sentences for Jacobson (2001)

FILES="/home/emily/Documents/Github_Repos/foma.ess/jacobson_eoc"

for file in "$FILES"/*.in; do

	# output=${file%.in}.out	# For generating *.out output files
	output=${file%.in}.count	# For generating output count files

	echo "Processing ${file} to create ${output}"
			 
	while IFS= read -r line; do
		sent=$(echo "$line" | cut -f 2- | sed 's/\.$//' | tr '[:upper:]' '[:lower:]')

		declare -a 'a=('"$sent"')'

		# printf '%s\n' "$line" | sed 's/\t/ /g'

		for word in "${a[@]}"; do

			echo "$word"
		   	echo "$word" | flookup -x ../ess.fomabin | awk ' /^$/ { print; } /./ { printf("%d ", $0); }' | awk '{print gsub(/ /, "")} '

			# printf "\n"
		done

		printf '%s\n' '------------------------'

	done <"$file" > "$output"
done
