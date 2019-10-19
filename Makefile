all: clean 
	cat lexc-files/header.txt lexc-files/roots/noun/*.txt lexc-files/roots/verb/*.txt lexc-files/inflections/noun/*.txt lexc-files/inflections/verb/*.txt lexc-files/prs-num/*.txt > ess.lexc

ess.fomabin: ess.foma *.lexc
	foma -l ess.foma -e "push Grammar" -e "save stack ess.fomabin" -s

clean:
	rm -f ess.dot ess.pdf *.pairs *.pairs.tsv *.fomabin

