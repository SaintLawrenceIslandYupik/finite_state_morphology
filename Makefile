all: clean ess.lexc lower.fomabin ess.fomabin test

ess.lexc: lexc-files/header.txt lexc-files/demonstratives.txt lexc-files/emotional_roots.txt lexc-files/interrogatives.txt lexc-files/numerals.txt lexc-files/particles.txt lexc-files/positionals.txt lexc-files/postural_roots.txt lexc-files/pronouns.txt lexc-files/quantifier_qualifier.txt lexc-files/roots/noun/*.txt lexc-files/roots/verb/*.txt lexc-files/derivational-suffixes/noun-suffixing/*.txt lexc-files/derivational-suffixes/verb-suffixing/*.txt lexc-files/inflections/noun/*.txt lexc-files/verb_root_ete.txt lexc-files/inflections/verb/*.txt lexc-files/prs-num/*.txt lexc-files/postinfl-morph.txt lexc-files/enclitics.txt
	cat $^ > $@

exceptions.lexc: exceptions/exceptions-header.txt exceptions/exceptions.txt lexc-files/derivational-suffixes/noun-suffixing/*.txt lexc-files/derivational-suffixes/verb-suffixing/*.txt lexc-files/inflections/noun/*.txt lexc-files/inflections/verb/*.txt lexc-files/prs-num/*.txt lexc-files/postinfl-morph.txt lexc-files/enclitics.txt 
	cat $^ > $@

parallel.lexc: parallel/parallel-header.txt parallel/parallel-forms.txt
	cat $^ > $@

lower.fomabin: ess.foma ess.lexc exceptions.lexc parallel.lexc
	foma -l ess.foma -e "push GrammarLower" -e "save stack lower.fomabin" -s

ess.fomabin: ess.foma ess.lexc exceptions.lexc parallel.lexc
	foma -l ess.foma -e "push GrammarUpper" -e "save stack ess.fomabin" -s


interactive: ess.foma ess.lexc exceptions.lexc parallel.lexc
	foma -l ess.foma -e "push GrammarUpper"


test: $(foreach n,2 3 4 5 6 7 8 9 10 11 12 13 14 15 17 18,test-ch$n) test-emotionalroots test-posturalroots test-enclitics test-postbases

test-ch%: tests/jacobson_examples/jacobson_ch%.tsv lower.fomabin
	@cut -f 1 $< | sort -d -f | uniq | flookup -i -w "" lower.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f $<)' && echo "Jacobson (2001) Ch$*  - PASS" || echo "Jacobson (2001) Ch$* - FAIL"

test-emotionalroots: tests/badten_examples/emotional_roots.tsv lower.fomabin
	@cut -f 1 tests/badten_examples/emotional_roots.tsv | sort -d -f | uniq | flookup -i -w "" lower.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/badten_examples/emotional_roots.tsv)' && echo "Badten (2008) Emotional Roots - PASS" || echo "Badten (2008) Emotional Roots - FAIL"

test-posturalroots: tests/badten_examples/postural_roots.tsv lower.fomabin
	@cut -f 1 tests/badten_examples/postural_roots.tsv | sort -d -f | uniq | flookup -i -w "" lower.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/badten_examples/postural_roots.tsv)' && echo "Badten (2008) Postural Roots - PASS" || echo "Badten (2008) Postural Roots - FAIL"

test-enclitics: tests/badten_examples/enclitics.tsv lower.fomabin
	@cut -f 1 tests/badten_examples/enclitics.tsv | sort -d -f | uniq | flookup -i -w "" lower.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/badten_examples/enclitics.tsv)' && echo "Badten (2008) Enclitics - PASS" || echo "Badten (2008) Enclitics - FAIL"

test-postbases: $(foreach n,A E F G I,test-$n-postbases)

test-%-postbases: tests/badten_examples/%-postbases.tsv lower.fomabin
	@cut -f 1 tests/badten_examples/$*-postbases.tsv | sort -d -f | uniq | flookup -i -w "" lower.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/badten_examples/$*-postbases.tsv)' && echo "Badten (2008) $*-Postbases - PASS" || echo "Badten (2008) $*-Postbases - FAIL"

clean:
	rm -f ess.dot ess.pdf *.pairs *.pairs.tsv *.fomabin *.lexc
