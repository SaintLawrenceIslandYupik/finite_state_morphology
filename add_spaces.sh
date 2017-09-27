#!/bin/bash

file="./just_nouns.txt"

while IFS= read -r line; do

	len=${#line}
	padding=$((23 - $len))

	printf '%-*s\n' 23 "$line"

done<"$file"
