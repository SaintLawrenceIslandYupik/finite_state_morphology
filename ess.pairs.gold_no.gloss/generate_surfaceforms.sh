#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 \"inputToSurface.tsv &> ess.pairs.*\""
  exit 1
fi

while read line; do
    echo "$line" | flookup -i ../ess.fomabin | grep -v '^ *$'
done < "$1"
