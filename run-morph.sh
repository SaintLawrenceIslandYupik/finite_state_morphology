#!/bin/bash


FILES="analyzer_output/txts/lore_volume1/toy"

# Runs each *.in file through the analyzer and copies the output to a *.out file
for file in "$FILES"/*.in; do

	output=${file%.in}.out


	echo "Processing ${file} to create ${output}..."

	while IFS= read -r line; do

		# TODO: Does not account for English borrowings
		sent=$(echo "$line" | tr -d ',;:()"!?.' | tr '[:upper:]' '[:lower:]')

		declare -a 'a=('"$sent"')'

		printf '%s\n\n' "$line" | sed 's/\t/ /g'

		for word in "${a[@]}"; do
			echo "${word}" | grep -q '[0-9]'

			if [[ $? = 1 ]]; then
				# Accounts for words that end in -s, -g, -gh
				wordOriginalEnding=$(echo "$word" | sed 's/s$/t/' | sed 's/g$/k/' | sed 's/gh$/q/')

				result=$(echo "$wordOriginalEnding" | flookup -w "" ./ess.fomabin)

				# Attempts to analyze word again without apostrophes
				if [[ "$result" == "$wordOriginalEnding	+?" ]]; then
					wordNoApostrophe=$(echo "$wordOriginalEnding" | sed "s/'//g")

					resultNoApostrophe=$(echo "$wordNoApostrophe" | flookup -w "" ./ess.fomabin | sed "s/$wordNoApostrophe/$word/")

					echo "$resultNoApostrophe"
				else
					echo "$result"
				fi

				printf "\n"
			fi
		done

		printf '%s\n' '------------------------'

	done <"$file" > "$output"
done


# Prints all words that were not successfully parsed
for file in "$FILES"/*.out; do

	filename=${file%.out}

	while IFS= read -r line; do
		if [[ $line == *"?" ]]; then
			echo "$filename: $line"
		fi
	done <"$file" > "$filename".errors 
done




#######
