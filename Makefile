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



test: test-ch2 test-ch3 test-ch4 test-ch5 test-ch6 test-ch7 test-ch8


test-ch2: ess.pairs.gold/Ch2.N_ABS.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch2.N_ABS.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch2.N_ABS.tsv     && echo "Jacobson (2001) Chapter 2 Noun Vocabulary - Absolutive Singular, Dual, & Plural   - PASS" || echo "Jacobson (2001) Chapter 2 Noun Vocabulary - Absolutive Singular, Dual, & Plural   - FAIL"
	@cut -f 1 ess.pairs.gold/Ch2.N_AblMod.tsv  | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch2.N_AblMod.tsv  && echo "Jacobson (2001) Chapter 2 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - PASS" || echo "Jacobson (2001) Chapter 2 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - FAIL"


test-ch3: ess.pairs.gold/Ch3.N_ABS.tsv ess.pairs.gold/Ch3.N_AblMod.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch3.N_ABS.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch3.N_ABS.tsv     && echo "Jacobson (2001) Chapter 3 Noun Vocabulary - Absolutive Singular, Dual, & Plural   - PASS" || echo "Jacobson (2001) Chapter 3 Noun Vocabulary - Absolutive Singular, Dual, & Plural   - FAIL"
	@cut -f 1 ess.pairs.gold/Ch3.N_AblMod.tsv  | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch3.N_AblMod.tsv  && echo "Jacobson (2001) Chapter 3 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - PASS" || echo "Jacobson (2001) Chapter 3 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - FAIL"
	@cut -f 1 ess.pairs.gold/Ch3.V_IntrInd.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch3.V_IntrInd.tsv && echo "Jacobson (2001) Chapter 3 Verb Vocabulary - Intransitive Indicative               - PASS" || echo "Jacobson (2001) Chapter 3 Verb Vocabulary - Intransitive Indicative               - FAIL"

test-ch4: ess.pairs.gold/Ch4.N_ABS.1PossPosd.tsv ess.pairs.gold/Ch4.N_ABS.2PossPosd.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch4.N_ABS.1PossPosd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch4.N_ABS.1PossPosd.tsv     && echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 1st Person Possessor Possessed Absolutive     - PASS" || echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 1st Person Possessor Possessed Absolutive     - FAIL"
	@cut -f 1 ess.pairs.gold/Ch4.N_ABS.2PossPosd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch4.N_ABS.2PossPosd.tsv     && echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 2nd Person Possessor Possessed Absolutive     - PASS" || echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 2nd Person Possessor Possessed Absolutive     - FAIL"

test-ch5: ess.pairs.gold/Ch5.N_LOC.tsv ess.pairs.gold/Ch5.N_TER.tsv ess.pairs.gold/Ch5.N_VIA.tsv ess.pairs.gold/Ch5.N_EQU.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch5.N_LOC.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch5.N_LOC.tsv     && echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Localis Case    - PASS" || echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Localis Case    - FAIL"
	@cut -f 1 ess.pairs.gold/Ch5.N_TER.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch5.N_TER.tsv     && echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Terminalis Case - PASS" || echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Terminalis Case - FAIL"
	@cut -f 1 ess.pairs.gold/Ch5.N_VIA.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch5.N_VIA.tsv     && echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Vialis Case     - PASS" || echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Vialis Case     - FAIL"
	@cut -f 1 ess.pairs.gold/Ch5.N_EQU.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch5.N_EQU.tsv     && echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Equalis Case    - PASS" || echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Equalis Case    - FAIL"

test-ch6: ess.pairs.gold/Ch6.N_ABS.3PossPosd.tsv ess.pairs.gold/Ch6.N_REL.Unpd.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch6.N_ABS.3PossPosd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch6.N_ABS.3PossPosd.tsv     && echo "Jacobson (2001) Chapter 6 Noun Vocabulary - 3rd Person Possessor Possessed Absolutive     - PASS" || echo "Jacobson (2001) Chapter 6 Noun Vocabulary - 3rd Person Possessor Possessed Absolutive     - FAIL"
	@cut -f 1 ess.pairs.gold/Ch6.N_REL.Unpd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch6.N_REL.Unpd.tsv     && echo "Jacobson (2001) Chapter 6 Noun Vocabulary - Unpossessed Relative Case - PASS" || echo "Jacobson (2001) Chapter 6 Noun Vocabulary - Unpossessed Relative Case - FAIL"

test-ch7: ess.pairs.gold/Ch7.N_REL.Posd.tsv ess.pairs.gold/Ch7.V_TrnsInd.tsv ess.pairs.gold/Ch7.N_LOC.Posd.tsv ess.pairs.gold/Ch7.N_TER.Posd.tsv ess.pairs.gold/Ch7.N_VIA.Posd.tsv ess.pairs.gold/Ch7.N_EQU.Posd.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch7.N_REL.Posd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch7.N_REL.Posd.tsv     && echo "Jacobson (2001) Chapter 7 Noun Vocabulary - Possessed Relative Case     - PASS" || echo "Jacobson (2001) Chapter 7 Noun Vocabulary - Possessed Relative Case     - FAIL"
	@cut -f 1 ess.pairs.gold/Ch7.V_TrnsInd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch7.V_TrnsInd.tsv     && echo "Jacobson (2001) Chapter 7 Verb Vocabulary - Transitive Indicative         - PASS" || echo "Jacobson (2001) Chapter 7 Verb Vocabulary - Transitive Indicative       - FAIL"
	@cut -f 1 ess.pairs.gold/Ch7.N_LOC.Posd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch7.N_LOC.Posd.tsv     && echo "Jacobson (2001) Chapter 7 Noun Vocabulary - Localis Case with Singular Possessor    - PASS" || echo "Jacobson (2001) Chapter 7 Noun Vocabulary - Localis Case with Singular Possessor    - FAIL"
	@cut -f 1 ess.pairs.gold/Ch7.N_TER.Posd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch7.N_TER.Posd.tsv     && echo "Jacobson (2001) Chapter 7 Noun Vocabulary - Terminalis Case with Singular Possessor - PASS" || echo "Jacobson (2001) Chapter 7 Noun Vocabulary - Terminalis Case with Singular Possessor - FAIL"
	@cut -f 1 ess.pairs.gold/Ch7.N_VIA.Posd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch7.N_VIA.Posd.tsv     && echo "Jacobson (2001) Chapter 7 Noun Vocabulary - Vialis Case with Singular Possessor     - PASS" || echo "Jacobson (2001) Chapter 7 Noun Vocabulary - Vialis Case with Singular Possessor     - FAIL"
	@cut -f 1 ess.pairs.gold/Ch7.N_EQU.Posd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch7.N_EQU.Posd.tsv     && echo "Jacobson (2001) Chapter 7 Noun Vocabulary - Equalis Case with Singular Possessor    - PASS" || echo "Jacobson (2001) Chapter 7 Noun Vocabulary - Equalis Case with Singular Possessor    - FAIL"

test-ch8: ess.pairs.gold/Ch8.V_Intrg.Intr.tsv ess.pairs.gold/Ch8.V_Intrg.Trns.tsv ess.pairs.gold/Ch8.N_ABS.4PossPosd.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch8.V_Intrg.Intr.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch8.V_Intrg.Intr.tsv     && echo "Jacobson (2001) Chapter 8 Verb Vocabulary - 2nd Person Subject Interrogatives for Intransitive Verbs - PASS" || echo "Jacobson (2001) Chapter 8 Verb Vocabulary - 2nd Person Subject Interrogatives for Intransitive Verbs - FAIL"
	@cut -f 1 ess.pairs.gold/Ch8.V_Intrg.Trns.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch8.V_Intrg.Trns.tsv     && echo "Jacobson (2001) Chapter 8 Verb Vocabulary - 2nd Person Subject Interrogatives for Transitive Verbs - PASS" || echo "Jacobson (2001) Chapter 8 Verb Vocabulary - 2nd Person Subject Interrogatives for Transitive Verbs - FAIL"
	@cut -f 1 ess.pairs.gold/Ch8.N_ABS.4PossPosd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch8.N_ABS.4PossPosd.tsv     && echo "Jacobson (2001) Chapter 8 Noun Vocabulary - 4th Person Possessor Possessed Absolutive - PASS" || echo "Jacobson (2001) Chapter 8 Noun Vocabulary - 4th Person Possessor Possessed Absolutive - FAIL"

clean:
	rm -f ess.dot ess.pdf *.pairs *.pairs.tsv *.fomabin


bases.tsv: bases.tab
	cat bases.tab | sed 's,\r,\n,g' | sed 's,\v, ,g' > bases.tsv

.PHONY: all interactive clean test test-ch2
