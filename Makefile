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
	@cut -f 1 ess.pairs.gold/Ch2.N_AblMod.tsv  | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch2.N_AblMod.tsv  && echo "Jacobson (2001) Chapter 2 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - PASS" || echo "Jacobson (2001) Chapter 2 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - FAIL"


test-ch3: ess.pairs.gold/Ch3.N_ABS.tsv ess.pairs.gold/Ch3.N_AblMod.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch3.N_ABS.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch3.N_ABS.tsv     && echo "Jacobson (2001) Chapter 3 Noun Vocabulary - Absolutive Singular, Dual, & Plural   - PASS" || echo "Jacobson (2001) Chapter 3 Noun Vocabulary - Absolutive Singular, Dual, & Plural   - FAIL"
	@cut -f 1 ess.pairs.gold/Ch3.N_AblMod.tsv  | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch3.N_AblMod.tsv  && echo "Jacobson (2001) Chapter 3 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - PASS" || echo "Jacobson (2001) Chapter 3 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - FAIL"
	@cut -f 1 ess.pairs.gold/Ch3.V_IntrInd.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch3.V_IntrInd.tsv && echo "Jacobson (2001) Chapter 3 Verb Vocabulary - Intransitive Indicative               - PASS" || echo "Jacobson (2001) Chapter 3 Verb Vocabulary - Intransitive Indicative               - FAIL"

test-ch4: ess.pairs.gold/Ch4.N_ABS.1SgPoss.tsv ess.pairs.gold/Ch4.N_ABS.1PlPoss.tsv ess.pairs.gold/Ch4.N_ABS.2SgPoss.tsv ess.pairs.gold/Ch4.N_ABS.2PlPoss.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch4.N_ABS.1SgPoss.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch4.N_ABS.1SgPoss.tsv     && echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 1st Person Singular Possessor Absolutive - PASS" || echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 1st Person Singular Possessor Absolutive - FAIL"
	@cut -f 1 ess.pairs.gold/Ch4.N_ABS.1PlPoss.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch4.N_ABS.1PlPoss.tsv     && echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 1st Person Plural Possessor Absolutive   - PASS" || echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 1st Person Plural Possessor Absolutive   - FAIL"
	@cut -f 1 ess.pairs.gold/Ch4.N_ABS.2SgPoss.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch4.N_ABS.2SgPoss.tsv     && echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 2nd Person Singular Possessor Absolutive - PASS" || echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 2nd Person Singular Possessor Absolutive - FAIL"
	@cut -f 1 ess.pairs.gold/Ch4.N_ABS.2PlPoss.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch4.N_ABS.2PlPoss.tsv     && echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 2nd Person Plural Possessor Absolutive   - PASS" || echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 2nd Person Plural Possessor Absolutive   - FAIL"

test-ch5: ess.pairs.gold/Ch5.N_LOC.tsv ess.pairs.gold/Ch5.N_TER.tsv ess.pairs.gold/Ch5.N_VIA.tsv ess.pairs.gold/Ch5.N_EQU.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch5.N_LOC.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch5.N_LOC.tsv     && echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Localis Case    - PASS" || echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Localis Case    - FAIL"
	@cut -f 1 ess.pairs.gold/Ch5.N_TER.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch5.N_TER.tsv     && echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Terminalis Case - PASS" || echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Terminalis Case - FAIL"
	@cut -f 1 ess.pairs.gold/Ch5.N_VIA.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch5.N_VIA.tsv     && echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Vialis Case     - PASS" || echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Vialis Case     - FAIL"
	@cut -f 1 ess.pairs.gold/Ch5.N_EQU.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch5.N_EQU.tsv     && echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Equalis Case    - PASS" || echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Equalis Case    - FAIL"


clean:
	rm -f ess.dot ess.pdf *.pairs *.pairs.tsv *.fomabin


bases.tsv: bases.tab
	cat bases.tab | sed 's,\r,\n,g' | sed 's,\v, ,g' > bases.tsv

.PHONY: all interactive clean test test-ch2
