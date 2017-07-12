#!/bin/bash

echo "Enter filename, e.g. 'Ch2.in': "
read filename 

file="./${filename}"

output=$(echo "$filename" | cut -d\. -f1)

while IFS= read -r line; do
	sent=$(echo "$line" | cut -f 2- | sed 's/\.$//' | tr '[:upper:]' '[:lower:]')

	declare -a 'a=('"$sent"')'

	
	printf '%s\n\n' "$line" | sed 's/\t/ /g'
	for word in "${a[@]}"; do
		echo "$word" | flookup -w "" ../ess.fomabin
		printf "\n"
	done
	printf '%s\n' '------------------------'

done <"$file" > "$output".out
