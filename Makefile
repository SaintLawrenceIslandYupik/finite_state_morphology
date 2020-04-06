all: clean test

ess.fomabin: ess.foma *.lexc
	foma -l ess.foma -e "push Grammar" -e "save stack ess.fomabin" -s

#ess.lex.fomabin: ess.foma *.lexc
#	foma -l ess.foma -e "push IntermediateGrammar" -e "save stack ess.lex.fomabin" -s

interactive: ess.foma *.lexc
	foma -l ess.foma -e "push Grammar"

test: $(foreach n,2 3 4 5 6 7 8 9 10 11 12 13 14 15 17 18,test-ch$n) test-emotionalroots test-posturalroots test-enclitics test-postbases

test-ch%: tests/jacobson_examples/jacobson_ch%.tsv ess.fomabin
	@cut -f 1 $< | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f $<)' && echo "Jacobson (2001) Ch$*  - PASS" || echo "Jacobson (2001) Ch$* - FAIL"

test-emotionalroots: tests/badten_examples/emotional_roots.tsv ess.fomabin
	@cut -f 1 tests/badten_examples/emotional_roots.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/badten_examples/emotional_roots.tsv)' && echo "Badten (2008) Emotional Roots - PASS" || echo "Badten (2008) Emotional Roots - FAIL"

test-posturalroots: tests/badten_examples/postural_roots.tsv ess.fomabin
	@cut -f 1 tests/badten_examples/postural_roots.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/badten_examples/postural_roots.tsv)' && echo "Badten (2008) Postural Roots - PASS" || echo "Badten (2008) Postural Roots - FAIL"

test-enclitics: tests/badten_examples/enclitics.tsv ess.fomabin
	@cut -f 1 tests/badten_examples/enclitics.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/badten_examples/enclitics.tsv)' && echo "Badten (2008) Enclitics - PASS" || echo "Badten (2008) Enclitics - FAIL"

test-postbases: $(foreach n,A E F G I K L M N P Q R S T U V Y,test-$n-postbases)

test-%-postbases: tests/badten_examples/%-postbases.tsv ess.fomabin
	@cut -f 1 tests/badten_examples/$*-postbases.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/badten_examples/$*-postbases.tsv)' && echo "Badten (2008) $*-Postbases - PASS" || echo "Badten (2008) $*-Postbases - FAIL"

clean:
	rm -f ess.dot ess.pdf *.pairs *.pairs.tsv *.fomabin
