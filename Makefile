all: lexc $(foreach x,asciiarrow ess f2i f2is f2s fi2s g2i g2is g2s gi2s l2i l2is l2s li2s a2s uppercase,$x.fomabin) test
# all: ess.lexc $(foreach x,asciiarrow ess l2i l2is l2s li2s lowercase uppercase,$x.fomabin) test

lexc: ess.lexc exceptions.lexc parallel.lexc foreign.lexc eng-noun.lexc eng-verb.lexc eng-other.lexc

.PHONY: all lexc interactive

ess.lexc: lexc-files/header.txt lexc-files/emotional_roots.txt lexc-files/interrogatives.txt lexc-files/demonstratives.txt lexc-files/dem-suffixes.txt lexc-files/numerals.txt lexc-files/particles.txt lexc-files/positionals.txt lexc-files/postural_roots.txt lexc-files/pronouns.txt lexc-files/quantifier_qualifier.txt lexc-files/roots/noun/*.txt lexc-files/roots/verb/*.txt lexc-files/derivational-suffixes/noun-suffixing/*.txt lexc-files/derivational-suffixes/verb-suffixing/*.txt lexc-files/inflections/noun/*.txt lexc-files/verb_root_ete.txt lexc-files/inflections/verb/*.txt lexc-files/prs-num/*.txt lexc-files/postinfl-morph.txt lexc-files/enclitics.txt lexc-files/punctuation.txt
	@cat $^ > $@

exceptions.lexc: exceptions/header.txt exceptions/exceptions.txt lexc-files/derivational-suffixes/noun-suffixing/*.txt lexc-files/derivational-suffixes/verb-suffixing/*.txt lexc-files/inflections/noun/*.txt lexc-files/inflections/verb/*.txt lexc-files/prs-num/*.txt lexc-files/dem-suffixes.txt lexc-files/postinfl-morph.txt lexc-files/enclitics.txt 
	@cat $^ > $@

parallel.lexc: parallel/header.txt parallel/parallels.txt lexc-files/derivational-suffixes/noun-suffixing/*.txt lexc-files/derivational-suffixes/verb-suffixing/*.txt lexc-files/inflections/noun/*.txt lexc-files/inflections/verb/*.txt lexc-files/prs-num/*.txt lexc-files/postinfl-morph.txt lexc-files/enclitics.txt 
	@cat $^ > $@

foreign.lexc: foreign/header.txt foreign/foreign.txt lexc-files/derivational-suffixes/noun-suffixing/*.txt lexc-files/derivational-suffixes/verb-suffixing/*.txt lexc-files/inflections/noun/*.txt lexc-files/inflections/verb/*.txt lexc-files/prs-num/*.txt lexc-files/postinfl-morph.txt lexc-files/enclitics.txt 
	@cat $^ > $@

eng-noun.lexc: foreign/header.txt foreign/noun.txt
	@cat $^ > $@

eng-verb.lexc: foreign/header.txt foreign/verb.txt
	@cat $^ > $@

eng-other.lexc: foreign/header.txt foreign/other.txt
	@cat $^ > $@


ess.fomabin: ess.foma ess.lexc exceptions.lexc parallel.lexc foreign.lexc eng-noun.lexc eng-verb.lexc eng-other.lexc
	foma -l ess.foma -e "save defined $@" -s


asciiarrow.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push FullLexicalAsciiArrowToSurfaceGrammar" -e "save stack $@" -s

# full grammar that handles foreign words in the corpus, numbers, sandhi phenomena, and additional orthography rules
l2s.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push FullLexicalToSurfaceGrammar" -e "save stack $@" -s

l2is.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push FullLexicalToIntermediateWithPhonology" -e "save stack $@" -s

li2s.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push FullIntermediateToSurfaceGrammar" -e "save stack $@" -s

l2i.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push FullLexicalToIntermediateGrammar" -e "save stack $@" -s

uppercase.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push UppercaseFullLexicalToSurfaceGrammar" -e "save stack $@" -s


l2s_ess.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push LexicalToSurfaceGrammar" -e "save stack $@" -s

l2is_ess.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push LexicalToIntermediateWithPhonology" -e "save stack $@" -s

li2s_ess.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push IntermediateToSurfaceGrammar" -e "save stack $@" -s

l2i_ess.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push LexicalToIntermediateGrammar" -e "save stack $@" -s

uppercase_ess.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push LexicalToInitialCapsSurfaceGrammar" -e "save stack $@" -s

# Guessed Yupik words
g2s.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push GuessToSurfaceGrammar" -e "save stack $@" -s

g2i.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push GuessToIntermediateGrammar" -e "save stack $@" -s

g2is.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push GuessToIntermediateWithPhonology" -e "save stack $@" -s

gi2s.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push GuessIntermediateToSurfaceGrammar" -e "save stack $@" -s


# Foreign words and names
f2s.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push ForeignToSurfaceGrammar" -e "save stack $@" -s

f2i.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push ForeignToIntermediateGrammar" -e "save stack $@" -s

f2is.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push ForeignToIntermediateWithPhonology" -e "save stack $@" -s

fi2s.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push ForeignIntermediateToSurfaceGrammar" -e "save stack $@" -s

a2s.fomabin: ess.fomabin ess.foma ess.lexc
	foma -e "load defined $<" -e "push LexicalToSurfaceGrammar" -e "re LexicalToSurfaceGrammar .o. AllowUppercase ;" -e "push ForeignToSurfaceGrammar" -e "push GuessToSurfaceGrammar" -e "save stack $@" -s


%.interactive: %.fomabin
	foma -e "load stack $<"

interactive: l2s.interactive

.PRECIOUS: %.fomabin

test: $(foreach n,2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18,test-ch$n) test-emotionalroots test-posturalroots test-enclitics test-postbases #test-dereuse

test-ch%: tests/jacobson_examples/jacobson_ch%.tsv l2s.fomabin
	@export LC_ALL=C && cut -f 1 $< | sort -d -f | uniq | flookup -i -w "" l2s.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f $<)' && echo "Jacobson (2001) Ch$*  - PASS" || echo "Jacobson (2001) Ch$* - FAIL"

test-emotionalroots: tests/badten_examples/emotional_roots.tsv l2s.fomabin
	@export LC_ALL=C && cut -f 1 tests/badten_examples/emotional_roots.tsv | sort -d -f | uniq | flookup -i -w "" l2s.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/badten_examples/emotional_roots.tsv)' && echo "Badten (2008) Emotional Roots - PASS" || echo "Badten (2008) Emotional Roots - FAIL"

test-posturalroots: tests/badten_examples/postural_roots.tsv l2s.fomabin
	@export LC_ALL=C && cut -f 1 tests/badten_examples/postural_roots.tsv | sort -d -f | uniq | flookup -i -w "" l2s.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/badten_examples/postural_roots.tsv)' && echo "Badten (2008) Postural Roots - PASS" || echo "Badten (2008) Postural Roots - FAIL"

test-enclitics: tests/badten_examples/enclitics.tsv l2s.fomabin
	@export LC_ALL=C && cut -f 1 tests/badten_examples/enclitics.tsv | sort -d -f | uniq | flookup -i -w "" l2s.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/badten_examples/enclitics.tsv)' && echo "Badten (2008) Enclitics - PASS" || echo "Badten (2008) Enclitics - FAIL"

test-postbases: $(foreach n,A E F G I K L M N P Q R S T U V Y,test-$n-postbases)

test-%-postbases: tests/badten_examples/%-postbases.tsv l2s.fomabin
	@export LC_ALL=C && cut -f 1 tests/badten_examples/$*-postbases.tsv | sort -d -f | uniq | flookup -i -w "" l2s.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f tests/badten_examples/$*-postbases.tsv)' && echo "Badten (2008) $*-Postbases - PASS" || echo "Badten (2008) $*-Postbases - FAIL"

#test-dereuse: tests/other/deReuse1994_ch2.tsv l2s.fomabin
#	@cut -f 1 $< | sort -d -f | uniq | flookup -i -w "" l2s.fomabin | sort -d -f | bash -c 'diff - <(sort -d -f $<)' && echo "de Reuse (1994) Ch2  - PASS" || echo "de Reuse (1994) Ch2 - FAIL"


clean:
	rm -f ess.dot ess.pdf *.pairs *.pairs.tsv *.fomabin *.lexc
