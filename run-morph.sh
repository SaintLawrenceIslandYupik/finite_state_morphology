#!/bin/bash

# TODO: Script does not account for English borrowings.
#       Instead, they are removed via preprocessing

FILES="analyzer_output/txts/original_txts/jacobson_eoc"

# Runs each *.in file through the analyzer and copies the output to a *.out file
for file in "$FILES"/*.in; do

	output=${file%.in}.out

	echo "Processing ${file} to create ${output}..."

	# Accounts for words that end in -s, -g (but not -ng), -gh
    sed -i 's/s /t /' "$file" | sed 's/\([^n]\)g /\1k /' | sed 's/gh /q /'

	while IFS= read -r line; do

		# Handles punctuation
		sent=$(echo "$line" | tr -d ',;:()"!?.=' | sed 's/ - / /g' | sed "s/'$//" | sed "s/^'//" | sed "s/ '/ /" | tr '[:upper:]' '[:lower:]')

		declare -a 'a=('"$sent"')'

		printf '%s\n\n' "$line" | sed 's/\t/ /g'

		for word in "${a[@]}"; do
			# Accounts for English borrowings that were manually replaced in the text with the phrase "FOREIGN WORD"
			if [[ "$word" == *"[]"* ]]; then
				echo -e "FOREIGN WORD\n"
			else
				# Handles inflected numbers, e.g. 1999-em
				echo "${word}" | grep -q '[0-9]'

				if [[ $? = 1 ]]; then
					result=$(echo "$word" | flookup -w "" ./ess.fomabin)

					# Attempts to analyze word again without apostrophes IF it contains apostrophes
					if [[ "$result" == "$word	+?" ]] && [[ "$result" == *"'"* ]]; then

						wordNoApostrophe=$(echo "$word" | sed "s/'//g")

						resultNoApostrophe=$(echo "$wordNoApostrophe" | flookup -w "" ./ess.fomabin | sed "s/$wordNoApostrophe/$word/")

						echo "$resultNoApostrophe"

						# Attempts to guess if the analyzer cannot find a valid parse, even with the apostrophes removed
						# Not yet implemented, since the guesser does not guess for words with apostrophes
						# if [[ "$resultNoApostrophe" == "$word	+?" ]]; then
						#	guess=$(echo "$word" | flookup -w "" ./guesser.fomabin)	
						#	echo "$guess"
						# else
						#	echo "$resultNoApostrophe"
						# fi

					# Attempts to guess if the analyzer cannot find a valid parse
					# elif [[ "$result" == "$word	+?" ]]; then 
						# guess=$(echo "$word" | flookup -w "" ./guesser.fomabin)	

						# echo "$guess"

					# Otherwise, prints the parses that were found
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
