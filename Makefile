all: clean ess.lexc test

ess.lexc:
	cat lexc-files/header.txt lexc-files/demonstratives.txt lexc-files/emotional_roots.txt lexc-files/interrogatives.txt lexc-files/numerals.txt lexc-files/particles.txt lexc-files/positionals.txt lexc-files/postural_roots.txt lexc-files/pronouns.txt lexc-files/quantifier_qualifier.txt lexc-files/roots/noun/*.txt lexc-files/roots/verb/*.txt lexc-files/derivational-suffixes/noun-suffixing/*.txt lexc-files/derivational-suffixes/verb-suffixing/*.txt lexc-files/inflections/noun/*.txt lexc-files/verb_root_ete.txt lexc-files/inflections/verb/*.txt lexc-files/prs-num/*.txt lexc-files/postinfl-morph.txt lexc-files/enclitics.txt > ess.lexc
	cat exceptions/header-exceptions.txt exceptions/exceptions.txt lexc-files/derivational-suffixes/noun-suffixing/*.txt lexc-files/derivational-suffixes/verb-suffixing/*.txt lexc-files/inflections/noun/*.txt lexc-files/inflections/verb/*.txt lexc-files/prs-num/*.txt lexc-files/postinfl-morph.txt lexc-files/enclitics.txt > exceptions.lexc
	cat parallel/header-parallel.txt parallel/parallel-forms.txt > parallel.lexc

ess.fomabin: ess.foma ess.lexc exceptions.lexc parallel.lexc
	foma -l ess.foma -e "push Grammar" -e "save stack ess.fomabin" -s

interactive: ess.foma ess.lexc exceptions.lexc parallel.lexc
	foma -l ess.foma -e "push Grammar"


test: test-ch2 test-ch3 test-ch4 test-ch5 test-ch6 test-ch7 test-ch8 test-ch9 test-ch10 test-ch11 test-ch12 test-ch13 test-ch14 test-ch15 test-ch17 test-ch18 test-emotionalroots test-posturalroots test-enclitics

test-ch2: tests/jacobson_examples/jacobson_ch2.tsv ess.fomabin
	@cut -f 1 tests/jacobson_examples/jacobson_ch2.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch2.tsv)' && echo "Jacobson (2001) Ch2 - PASS" || echo "Jacobson (2001) Ch2 - FAIL"

test-ch3: tests/jacobson_examples/jacobson_ch3.tsv ess.fomabin
	@cut -f 1 tests/jacobson_examples/jacobson_ch3.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch3.tsv)' && echo "Jacobson (2001) Ch3 - PASS" || echo "Jacobson (2001) Ch3 - FAIL"

test-ch4: tests/jacobson_examples/jacobson_ch4.tsv ess.fomabin
	@cut -f 1 tests/jacobson_examples/jacobson_ch4.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch4.tsv)' && echo "Jacobson (2001) Ch4 - PASS" || echo "Jacobson (2001) Ch4 - FAIL"

test-ch5: tests/jacobson_examples/jacobson_ch5.tsv ess.fomabin
	@cut -f 1 tests/jacobson_examples/jacobson_ch5.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch5.tsv)' && echo "Jacobson (2001) Ch5 - PASS" || echo "Jacobson (2001) Ch5 - FAIL"

test-ch6: tests/jacobson_examples/jacobson_ch6.tsv ess.fomabin
	@cut -f 1 tests/jacobson_examples/jacobson_ch6.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch6.tsv)' && echo "Jacobson (2001) Ch6 - PASS" || echo "Jacobson (2001) Ch6 - FAIL"

test-ch7: tests/jacobson_examples/jacobson_ch7.tsv ess.fomabin
	@cut -f 1 tests/jacobson_examples/jacobson_ch7.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch7.tsv)' && echo "Jacobson (2001) Ch7 - PASS" || echo "Jacobson (2001) Ch7 - FAIL"

test-ch8: tests/jacobson_examples/jacobson_ch8.tsv ess.fomabin
	@cut -f 1 tests/jacobson_examples/jacobson_ch8.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch8.tsv)' && echo "Jacobson (2001) Ch8 - PASS" || echo "Jacobson (2001) Ch8 - FAIL"

test-ch9: tests/jacobson_examples/jacobson_ch9.tsv ess.fomabin
	@cut -f 1 tests/jacobson_examples/jacobson_ch9.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch9.tsv)' && echo "Jacobson (2001) Ch9 - PASS" || echo "Jacobson (2001) Ch9 - FAIL"

test-ch10: tests/jacobson_examples/jacobson_ch10.tsv ess.fomabin
	@cut -f 1 tests/jacobson_examples/jacobson_ch10.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch10.tsv)' && echo "Jacobson (2001) Ch10 - PASS" || echo "Jacobson (2001) Ch10 - FAIL"

test-ch11: tests/jacobson_examples/jacobson_ch11.tsv ess.fomabin
	@cut -f 1 tests/jacobson_examples/jacobson_ch11.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch11.tsv)' && echo "Jacobson (2001) Ch11 - PASS" || echo "Jacobson (2001) Ch11 - FAIL"

test-ch12: tests/jacobson_examples/jacobson_ch12.tsv ess.fomabin
	@cut -f 1 tests/jacobson_examples/jacobson_ch12.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch12.tsv)' && echo "Jacobson (2001) Ch12 - PASS" || echo "Jacobson (2001) Ch12 - FAIL"

test-ch13: tests/jacobson_examples/jacobson_ch13.tsv ess.fomabin
	@cut -f 1 tests/jacobson_examples/jacobson_ch13.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch13.tsv)' && echo "Jacobson (2001) Ch13 - PASS" || echo "Jacobson (2001) Ch13 - FAIL"

test-ch14: tests/jacobson_examples/jacobson_ch14.tsv ess.fomabin
	@cut -f 1 tests/jacobson_examples/jacobson_ch14.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch14.tsv)' && echo "Jacobson (2001) Ch14 - PASS" || echo "Jacobson (2001) Ch14 - FAIL"

test-ch15: tests/jacobson_examples/jacobson_ch15.tsv ess.fomabin
	@cut -f 1 tests/jacobson_examples/jacobson_ch15.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch15.tsv)' && echo "Jacobson (2001) Ch15 - PASS" || echo "Jacobson (2001) Ch15 - FAIL"

test-ch17: tests/jacobson_examples/jacobson_ch17.tsv ess.fomabin
	@cut -f 1 tests/jacobson_examples/jacobson_ch17.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch17.tsv)' && echo "Jacobson (2001) Ch17 - PASS" || echo "Jacobson (2001) Ch17 - FAIL"

test-ch18: tests/jacobson_examples/jacobson_ch18.tsv ess.fomabin
	@cut -f 1 tests/jacobson_examples/jacobson_ch18.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/jacobson_examples/jacobson_ch18.tsv)' && echo "Jacobson (2001) Ch18 - PASS" || echo "Jacobson (2001) Ch18 - FAIL"

test-emotionalroots: tests/badten_examples/emotional_roots.tsv ess.fomabin
	@cut -f 1 tests/badten_examples/emotional_roots.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/badten_examples/emotional_roots.tsv)' && echo "Badten (2008) Emotional Roots - PASS" || echo "Badten (2008) Emotional Roots - FAIL"

test-posturalroots: tests/badten_examples/postural_roots.tsv ess.fomabin
	@cut -f 1 tests/badten_examples/postural_roots.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/badten_examples/postural_roots.tsv)' && echo "Badten (2008) Postural Roots - PASS" || echo "Badten (2008) Postural Roots - FAIL"

test-enclitics: tests/badten_examples/enclitics.tsv ess.fomabin
	@cut -f 1 tests/badten_examples/enclitics.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/badten_examples/enclitics.tsv)' && echo "Badten (2008) Enclitics - PASS" || echo "Badten (2008) Enclitics - FAIL"


clean:
	rm -f ess.dot ess.pdf *.pairs *.pairs.tsv *.fomabin *.lexc
