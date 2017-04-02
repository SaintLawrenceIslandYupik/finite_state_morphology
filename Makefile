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


test-ch2: ess.pairs.Ch2.N_ABS.tsv ess.fomabin
	@cut -f 1 ess.pairs.Ch2.N_ABS.tsv     | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.Ch2.N_ABS.tsv     && echo "Jacobson (2001) Chapter 2 noun vocabulary - absolutive singular, dual, & plural   - PASS"
	@cut -f 1 ess.pairs.Ch2.N_AblMod.tsv  | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.Ch2.N_AblMod.tsv  && echo "Jacobson (2001) Chapter 2 noun vocabulary - ablative-modalis unpossessed singular - PASS"


test-ch3: ess.pairs.Ch3.N_ABS.tsv ess.pairs.Ch3.N_AblMod.tsv ess.fomabin
	@cut -f 1 ess.pairs.Ch3.N_ABS.tsv     | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.Ch3.N_ABS.tsv     && echo "Jacobson (2001) Chapter 3 noun vocabulary - absolutive singular, dual, & plural   - PASS"
	@cut -f 1 ess.pairs.Ch3.N_AblMod.tsv  | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.Ch3.N_AblMod.tsv  && echo "Jacobson (2001) Chapter 3 noun vocabulary - ablative-modalis unpossessed singular - PASS"
	@cut -f 1 ess.pairs.Ch3.V_IntrInd.tsv | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.Ch3.V_IntrInd.tsv && echo "Jacobson (2001) Chapter 3 verb vocabulary - intransitive indicative               - PASS"


clean:
	rm -f ess.dot ess.pdf *.pairs *.pairs.tsv *.fomabin




.PHONY: all interactive clean test test-ch2
