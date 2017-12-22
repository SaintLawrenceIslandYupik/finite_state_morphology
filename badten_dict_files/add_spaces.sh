#!/bin/bash

file="./3.txt"

while IFS= read -r line; do

	len=${#line}
	padding=$((116 - $len))

	printf '%-*s\n' 116 "$line"

done<"$file"
