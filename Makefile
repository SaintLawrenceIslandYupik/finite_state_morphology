all: clean
	cat lexc-files/header.txt lexc-files/roots/noun/*.txt lexc-files/roots/verb/*.txt lexc-files/inflections/noun/*.txt lexc-files/inflections/verb/*.txt lexc-files/prs-num/*.txt > ess.lexc
	hfst-lexc --Werror ess.lexc -o ess.lexc.hfst
	hfst-twolc ess.twol -o ess.twol.hfst
	hfst-compose-intersect -1 ess.lexc.hfst -2 ess.twol.hfst -o ess.gen.hfst
	hfst-invert ess.gen.hfst -o ess.mor.hfst
	hfst-compose-intersect -1 ess.lexc.hfst -2 ess.twol.hfst -o tests/ess.gen.hfst

clean:
	rm -f *.hfst
