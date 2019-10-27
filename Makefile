all: clean test
	ls | cat lexc-files/header.txt lexc-files/particles.txt lexc-files/roots/noun/*.txt lexc-files/roots/verb/*.txt lexc-files/derivational-suffixes/noun-suffixing/*.txt lexc-files/derivational-suffixes/verb-suffixing/*.txt lexc-files/inflections/noun/*.txt lexc-files/inflections/verb/*.txt lexc-files/prs-num/*.txt > ess.lexc


ess.fomabin: ess.foma *.lexc
	foma -l ess.foma -e "push Grammar" -e "save stack ess.fomabin" -s


interactive: ess.foma *.lexc
	foma -l ess.foma -e "push Grammar"


test: test-ch2 test-ch3 test-ch4

test-ch2: tests/jacobson_examples/jacobson_ch2.tsv ess.fomabin
		@cut -f 1 tests/jacobson_examples/jacobson_ch2.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch2.tsv)' && echo "Jacobson (2001) Ch2 - PASS" || echo "Jacobson (2001) Ch2 - FAIL"

test-ch3: tests/jacobson_examples/jacobson_ch3.tsv ess.fomabin
		@cut -f 1 tests/jacobson_examples/jacobson_ch3.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch3.tsv)' && echo "Jacobson (2001) Ch3 - PASS" || echo "Jacobson (2001) Ch3 - FAIL"

test-ch4: tests/jacobson_examples/jacobson_ch4.tsv ess.fomabin
		@cut -f 1 tests/jacobson_examples/jacobson_ch4.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch4.tsv)' && echo "Jacobson (2001) Ch4 - PASS" || echo "Jacobson (2001) Ch4 - FAIL"


clean:
	rm -f ess.dot ess.pdf *.pairs *.pairs.tsv *.fomabin
