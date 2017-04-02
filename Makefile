all: clean ess.pdf test 



ess.fomabin: ess.foma *.lexc
	foma -l ess.foma -e "save stack ess.fomabin" -s

ess.dot: ess.foma *.lexc
	foma -l ess.foma -e "print dot > ess.dot" -s

ess.pairs: ess.foma *.lexc
	foma -l ess.foma -e "pairs > ess.pairs" -s

ess.pdf: ess.dot
	dot -Tpdf ess.dot > ess.pdf


interactive: ess.foma *.lexc
	foma -l ess.foma



test: test-ch2 test-ch3


test-ch2: ess.pairs.ch2_nouns.gold.tsv ess.fomabin
	@cut -f 1 ess.pairs.ch2_nouns.gold.tsv | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.ch2_nouns.gold.tsv && echo "Jacobson (2001) Chapter 2 noun vocabulary - absolutive singular, dual, & plural - PASS"

test-ch3: ess.pairs.ch3_nouns.gold.tsv ess.fomabin
	@cut -f 1 ess.pairs.ch3_nouns.gold.tsv | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.ch3_nouns.gold.tsv && echo "Jacobson (2001) Chapter 3 noun vocabulary - absolutive singular, dual, & plural - PASS"


clean:
	rm -f ess.dot ess.pdf *.pairs *.pairs.tsv *.fomabin




.PHONY: all interactive clean test test-ch2
