#!/bin/bash

# TODO: Script does not account for English borrowings.
#       Instead, they are removed via preprocessing

FILES="analyzer_output/txts/txts_ess-only/dummy"

# Runs each *.in file through the analyzer and copies the output to a *.out file
for file in "$FILES"/*.in; do

	output=${file%.in}.out

	echo "Processing ${file} to create ${output}..."

	# Accounts for words that end in -s, -g (but not -ng), -gh
    sed -i.bak 's/s /t /' "$file" | sed 's/\([^n]\)g /\1k /' | sed 's/gh /q /'

	while IFS= read -r line; do

		sent=$(echo "$line" | tr -d ',;:()"!?.' | tr '[:upper:]' '[:lower:]')

		declare -a 'a=('"$sent"')'

		printf '%s\n\n' "$line" | sed 's/\t/ /g'

		for word in "${a[@]}"; do
			if [[ "$word" == *"[]"* ]]; then
				echo "FOREIGN WORD"\n
			else
				echo "${word}" | grep -q '[0-9]'

				if [[ $? = 1 ]]; then
					result=$(echo "$word" | flookup -w "" ./ess.fomabin)

					# Attempts to analyze word again without apostrophes
					if [[ "$result" == "$word	+?" ]]; then

						wordNoApostrophe=$(echo "$word" | sed "s/'//g")

						resultNoApostrophe=$(echo "$wordNoApostrophe" | flookup -w "" ./ess.fomabin | sed "s/$wordNoApostrophe/$word/")

						# Attempts to guess if the analyzer cannot find a valid parse
						if [[ "$resultNoApostrophe" == "$word	+?" ]]; then

							guess=$(echo "$word" | flookup -w "" ./guesser.fomabin)	

							echo "$guess"
						else
							echo "$resultNoApostrophe"
						fi
					else
						echo "$result"
					fi
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
		if [[ $line == *"+?" ]]; then
			echo "$filename: $line"
		fi
	done <"$file" > "$filename".errors 
done




#######
