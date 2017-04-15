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



test: test-ch2 test-ch3 test-ch4


test-ch2: ess.pairs.Ch2.N_ABS.tsv ess.fomabin
	@cut -f 1 ess.pairs.Ch2.N_ABS.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.Ch2.N_ABS.tsv     && echo "Jacobson (2001) Chapter 2 noun vocabulary - absolutive singular, dual, & plural   - PASS" || echo "Jacobson (2001) Chapter 2 noun vocabulary - absolutive singular, dual, & plural   - FAIL"
	@cut -f 1 ess.pairs.Ch2.N_AblMod.tsv  | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.Ch2.N_AblMod.tsv  && echo "Jacobson (2001) Chapter 2 noun vocabulary - ablative-modalis unpossessed singular - PASS" || echo "Jacobson (2001) Chapter 2 noun vocabulary - ablative-modalis unpossessed singular - FAIL"


test-ch3: ess.pairs.Ch3.N_ABS.tsv ess.pairs.Ch3.N_AblMod.tsv ess.fomabin
	@cut -f 1 ess.pairs.Ch3.N_ABS.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.Ch3.N_ABS.tsv     && echo "Jacobson (2001) Chapter 3 noun vocabulary - absolutive singular, dual, & plural   - PASS" || echo "Jacobson (2001) Chapter 3 noun vocabulary - absolutive singular, dual, & plural   - FAIL"
	@cut -f 1 ess.pairs.Ch3.N_AblMod.tsv  | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.Ch3.N_AblMod.tsv  && echo "Jacobson (2001) Chapter 3 noun vocabulary - ablative-modalis unpossessed singular - PASS" || echo "Jacobson (2001) Chapter 3 noun vocabulary - ablative-modalis unpossessed singular - FAIL"
	@cut -f 1 ess.pairs.Ch3.V_IntrInd.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.Ch3.V_IntrInd.tsv && echo "Jacobson (2001) Chapter 3 verb vocabulary - intransitive indicative               - PASS" || echo "Jacobson (2001) Chapter 3 verb vocabulary - intransitive indicative               - FAIL"

test-ch4: ess.pairs.Ch4.tsv ess.fomabin
	@export  LC_ALL='C'; cut -f 2 ess.pairs.Ch4.tsv  | sort -d -f | uniq | flookup   -w "" ess.fomabin | awk '{printf("%s\t%s\n", $$2, $$1)}' | sort -d -f | uniq | diff - ess.pairs.Ch4.tsv                    && echo "Jacobson (2001) Chapter 4                 - incomplete tests                      - PASS" || echo "Jacobson (2001) Chapter 4                 - incomplete tests                      - FAIL"
	@cut -f 1 ess.pairs.Ch4.N_ABS.tsv  | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.Ch4.N_ABS.tsv                    && echo "Jacobson (2001) Chapter 4 noun vocabulary - absolutive singular, dual, & plural   - PASS" || echo "Jacobson (2001) Chapter 4 noun vocabulary - absolutive singular, dual, & plural   - FAIL"

clean:
	rm -f ess.dot ess.pdf *.pairs *.pairs.tsv *.fomabin


bases.tsv: bases.tab
	cat bases.tab | sed 's,\r,\n,g' | sed 's,\v, ,g' > bases.tsv

.PHONY: all interactive clean test test-ch2
