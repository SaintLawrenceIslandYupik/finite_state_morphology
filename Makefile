all: clean
	cat lexc-files/header.txt lexc-files/roots/noun/*.txt lexc-files/roots/verb/*.txt lexc-files/inflections/noun/*.txt lexc-files/inflections/verb/*.txt lexc-files/prs-num/*.txt > ess.lexc
	hfst-lexc --Werror ess.lexc -o ess.lexc.hfst
	hfst-twolc ess.twol -o ess.twol.hfst
	hfst-compose-intersect -1 ess.lexc.hfst -2 ess.twol.hfst -o ess.gen.hfst
	hfst-invert ess.gen.hfst -o ess.mor.hfst
	hfst-compose-intersect -1 ess.lexc.hfst -2 ess.twol.hfst -o tests/ess.gen.hfst


test: test-ch2 test-ch3 test-ch4

test-ch2: tests/jacobson_examples/jacobson_ch2.tsv ess.fomabin
		@cut -f 1 tests/jacobson_examples/jacobson_ch2.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - tests/jacobson_examples/jacobson_ch2.tsv && echo "Jacobson (2001) Ch2 - PASS" || echo "Jacobson (2001) Ch2 - FAIL"

test-ch3: tests/jacobson_examples/jacobson_ch3.tsv ess.fomabin
		@cut -f 1 tests/jacobson_examples/jacobson_ch3.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - tests/jacobson_examples/jacobson_ch3.tsv && echo "Jacobson (3001) Ch3 - PASS" || echo "Jacobson (3001) Ch3 - FAIL"

test-ch4: tests/jacobson_examples/jacobson_ch4.tsv ess.fomabin
		@cut -f 1 tests/jacobson_examples/jacobson_ch4.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - tests/jacobson_examples/jacobson_ch4.tsv && echo "Jacobson (4001) Ch4 - PASS" || echo "Jacobson (4001) Ch4 - FAIL"


clean:
	rm -f *.hfst
