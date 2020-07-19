#!/bin/bash

# Properly labels POS of each vocabulary word

paste left.txt right.txt > joined.txt

awk '{ if ($0 ~ /intransitive only/)
         {print $1 "      VerbIntr; ! "}
       else if ($0 ~ /transitive only/)
         {print $1 "      VerbTrans; ! "}
       else if ($0 ~ /transitive or intransitive/)
         {print $1 "      Verb; ! "}
       else if ($0 ~ /particle/)
         {print $1 "      ???; ! "}
       else
         {print $1 "      Noun; ! "}
     }' joined.txt > hasPOS.txt

paste -d'\0' hasPOS.txt right.txt | sed -e 's/-/ /g' > unsortedPOS.txt


# Sorts vocabulary list by POS

sort -k2 unsortedPOS.txt > finalList.txt
