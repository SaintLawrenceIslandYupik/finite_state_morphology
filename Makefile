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



test: test-ch2 test-ch3 test-ch4 test-ch5


test-ch2: ess.pairs.gold/Ch2.N_ABS.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch2.N_ABS.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch2.N_ABS.tsv     && echo "Jacobson (2001) Chapter 2 Noun Vocabulary - Absolutive Singular, Dual, & Plural   - PASS" || echo "Jacobson (2001) Chapter 2 Noun Vocabulary - Absolutive Singular, Dual, & Plural   - FAIL"
	@cut -f 1 ess.pairs.gold/Ch2.N_AblMod.tsv    | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch2.N_AblMod.tsv    && echo "Jacobson (2001) Chapter 2 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - PASS" || echo "Jacobson (2001) Chapter 2 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - FAIL"


test-ch3: ess.pairs.gold/Ch3.N_ABS.tsv ess.pairs.gold/Ch3.N_AblMod.tsv ess.pairs.gold/Ch3.V_IntrInd.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch3.N_ABS.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch3.N_ABS.tsv     && echo "Jacobson (2001) Chapter 3 Noun Vocabulary - Absolutive Singular, Dual, & Plural   - PASS" || echo "Jacobson (2001) Chapter 3 Noun Vocabulary - Absolutive Singular, Dual, & Plural   - FAIL"
	@cut -f 1 ess.pairs.gold/Ch3.N_AblMod.tsv  | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch3.N_AblMod.tsv     && echo "Jacobson (2001) Chapter 3 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - PASS" || echo "Jacobson (2001) Chapter 3 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - FAIL"
	@cut -f 1 ess.pairs.gold/Ch3.V_IntrInd.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch3.V_IntrInd.tsv     && echo "Jacobson (2001) Chapter 3 Verb Vocabulary - Intransitive Indicative               - PASS" || echo "Jacobson (2001) Chapter 3 Verb Vocabulary - Intransitive Indicative               - FAIL"

test-ch4: ess.pairs.gold/Ch4.N_ABS.tsv ess.pairs.gold/Ch4.N_AblMod.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch4.N_ABS.tsv    | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch4.N_ABS.tsv     && echo "Jacobson (2001) Chapter 4 Noun Vocabulary - Absolutive Singular, Dual, & Plural   - PASS" || echo "Jacobson (2001) Chapter 4 Noun Vocabulary - Absolutive Singular, Dual, & Plural   - FAIL"
	@cut -f 1 ess.pairs.gold/Ch4.N_AblMod.tsv    | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch4.N_AblMod.tsv    && echo "Jacobson (2001) Chapter 4 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - PASS" || echo "Jacobson (2001) Chapter 4 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - FAIL"

test-ch5: ess.pairs.gold/Ch5.N_ABS.tsv ess.pairs.gold/Ch5.N_AblMod.tsv ess.pairs.gold/Ch5.V_IntrInd.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch5.N_ABS.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch5.N_ABS.tsv     && echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Absolutive Singular, Dual, & Plural   - PASS" || echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Absolutive Singular, Dual, & Plural   - FAIL"
	@cut -f 1 ess.pairs.gold/Ch5.N_AblMod.tsv    | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch5.N_AblMod.tsv | cat -A    && echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - PASS" || echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - FAIL"
	@cut -f 1 ess.pairs.gold/Ch5.V_IntrInd.tsv    | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch5.V_IntrInd.tsv     && echo "Jacobson (2001) Chapter 5 Verb Vocabulary - Intransitive Indicative               - PASS" || echo "Jacobson (2001) Chapter 5 Verb Vocabulary - Intransitive Indicative               - FAIL"

clean:
	rm -f ess.dot ess.pdf *.pairs *.pairs.tsv *.fomabin

bases.tsv: bases.tab
	cat bases.tab | sed 's,\r,\n,g' | sed 's,\v, ,g' > bases.tsv

.PHONY: all interactive clean test test-ch2


# Output for incomplete tests
	#@export  LC_ALL='C'; cut -f 2 ess.pairs.Ch4.tsv  | sort -d -f | uniq | flookup   -w "" ess.fomabin | awk '{printf("%s\t%s\n", $$2, $$1)}' | sort -d -f | uniq | diff - ess.pairs.Ch4.tsv                    && echo "Jacobson (2001) Chapter 4                 - incomplete tests                      - PASS" || echo "Jacobson (2001) Chapter 4                 - incomplete tests                      - FAIL"
