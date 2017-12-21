#!/bin/bash

file="./nominalizing_formatted.txt"

while IFS= read -r line; do

	len=${#line}
	padding=$((77 - $len))

	printf '%-*s\n' 77 "$line"

done<"$file"
