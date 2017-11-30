#!/bin/bash

file="./verb_bases.txt"

while IFS= read -r line; do

	len=${#line}
	padding=$((22 - $len))

	printf '%-*s\n' 22 "$line"

done<"$file"
