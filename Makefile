all: clean test #ess.pdf



ess.fomabin: ess.foma *.lexc
	foma -l ess.foma -e "save stack ess.fomabin" -s

# ess.dot: ess.foma *.lexc
#	foma -l ess.foma -e "print dot > ess.dot" -s

ess.pairs: ess.foma *.lexc
	foma -l ess.foma -e "pairs > ess.pairs" -s

# ess.pdf: ess.dot
#	dot -Tpdf ess.dot > ess.pdf


interactive: ess.foma *.lexc
	foma -l ess.foma



test: test-ch2 test-ch3 test-ch4 test-ch5 test-ch6 test-ch7 test-ch8 test-ch9 test-ch10 test-ch11 test-ch12 test-ch13 test-ch14 test-ch15 test-ch17 test-ch18 test-filters


test-ch2: ess.pairs.gold/Ch2.N_ABS.tsv ess.pairs.gold/Ch2.In-Chapter-Examples.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch2.N_ABS.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch2.N_ABS.tsv     && echo "Jacobson (2001) Chapter 2 Noun Vocabulary - Absolutive Unpossessed                - PASS" || echo "Jacobson (2001) Chapter 2 Noun Vocabulary - Absolutive Unpossessed                - FAIL"
	@cut -f 1 ess.pairs.gold/Ch2.In-Chapter-Examples.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch2.In-Chapter-Examples.tsv     && echo "Jacobson (2001) Chapter 2 In-Chapter Examples - PASS" || echo "Jacobson (2001) Chapter 2 In-Chapter-Examples - FAIL"


test-ch3: ess.pairs.gold/Ch3.N_AblMod.tsv ess.pairs.gold/Ch3.In-Chapter-Examples.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch3.N_AblMod.tsv  | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch3.N_AblMod.tsv  && echo "Jacobson (2001) Chapter 3 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - PASS" || echo "Jacobson (2001) Chapter 3 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - FAIL"
	@cut -f 1 ess.pairs.gold/Ch3.V_IntrInd.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch3.V_IntrInd.tsv && echo "Jacobson (2001) Chapter 3 Verb Vocabulary - Intransitive Indicative               - PASS" || echo "Jacobson (2001) Chapter 3 Verb Vocabulary - Intransitive Indicative               - FAIL"
	@cut -f 1 ess.pairs.gold/Ch3.In-Chapter-Examples.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch3.In-Chapter-Examples.tsv     && echo "Jacobson (2001) Chapter 3 In-Chapter Examples - PASS" || echo "Jacobson (2001) Chapter 3 In-Chapter-Examples - FAIL"

test-ch4: ess.pairs.gold/Ch4.N_ABS.1PossPosd.tsv ess.pairs.gold/Ch4.N_ABS.2PossPosd.tsv ess.pairs.gold/Ch4.In-Chapter-Examples.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch4.N_ABS.1PossPosd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch4.N_ABS.1PossPosd.tsv     && echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 1st Person Possessor Possessed Absolutive - PASS" || echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 1st Person Possessor Possessed Absolutive - FAIL"
	@cut -f 1 ess.pairs.gold/Ch4.N_ABS.2PossPosd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch4.N_ABS.2PossPosd.tsv     && echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 2nd Person Possessor Possessed Absolutive - PASS" || echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 2nd Person Possessor Possessed Absolutive - FAIL"
	@cut -f 1 ess.pairs.gold/Ch4.In-Chapter-Examples.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch4.In-Chapter-Examples.tsv     && echo "Jacobson (2001) Chapter 4 In-Chapter Examples - PASS" || echo "Jacobson (2001) Chapter 4 In-Chapter-Examples - FAIL"

test-ch5: ess.pairs.gold/Ch5.N_EQU-LOC-TER-VIA.Unpd.tsv ess.pairs.gold/Ch5.In-Chapter-Examples.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch5.N_EQU-LOC-TER-VIA.Unpd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch5.N_EQU-LOC-TER-VIA.Unpd.tsv     && echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Equalis, Localis, Terminalis, Vialis Unpossessed - PASS" || echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Equalis, Localis, Terminalis, Vialis Unpossessed    - FAIL"
	@cut -f 1 ess.pairs.gold/Ch5.In-Chapter-Examples.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch5.In-Chapter-Examples.tsv     && echo "Jacobson (2001) Chapter 5 In-Chapter Examples - PASS" || echo "Jacobson (2001) Chapter 5 In-Chapter-Examples - FAIL"

test-ch6: ess.pairs.gold/Ch6.N_ABS.3PossPosd.tsv ess.pairs.gold/Ch6.N_REL.Unpd.tsv ess.pairs.gold/Ch6.In-Chapter-Examples.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch6.N_ABS.3PossPosd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch6.N_ABS.3PossPosd.tsv     && echo "Jacobson (2001) Chapter 6 Noun Vocabulary - 3rd Person Possessor Possessed Absolutive - PASS" || echo "Jacobson (2001) Chapter 6 Noun Vocabulary - 3rd Person Possessor Possessed Absolutive - FAIL"
	@cut -f 1 ess.pairs.gold/Ch6.N_REL.Unpd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch6.N_REL.Unpd.tsv     && echo "Jacobson (2001) Chapter 6 Noun Vocabulary - Relative Unpossessed                      - PASS" || echo "Jacobson (2001) Chapter 6 Noun Vocabulary - Relative Unpossessed                      - FAIL"
	@cut -f 1 ess.pairs.gold/Ch6.In-Chapter-Examples.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch6.In-Chapter-Examples.tsv     && echo "Jacobson (2001) Chapter 6 In-Chapter Examples - PASS" || echo "Jacobson (2001) Chapter 6 In-Chapter-Examples - FAIL"

test-ch7: ess.pairs.gold/Ch7.N_REL.Posd.tsv ess.pairs.gold/Ch7.V_TrnsInd.tsv ess.pairs.gold/Ch7.N_EQU-LOC-TER-VIA.SgPosd.tsv ess.pairs.gold/Ch7.N_AblMod.SgPoss.tsv ess.pairs.gold/Ch7.In-Chapter-Examples.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch7.N_REL.Posd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch7.N_REL.Posd.tsv     && echo "Jacobson (2001) Chapter 7 Noun Vocabulary - 1st/2nd Person Possessor Possessed Relative - PASS" || echo "Jacobson (2001) Chapter 7 Noun Vocabulary - 1st/2nd Person Possessor Possessed Relative - FAIL"
	@cut -f 1 ess.pairs.gold/Ch7.V_TrnsInd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch7.V_TrnsInd.tsv     && echo "Jacobson (2001) Chapter 7 Verb Vocabulary - Transitive Indicative                       - PASS" || echo "Jacobson (2001) Chapter 7 Verb Vocabulary - Transitive Indicative                     - FAIL"
	@cut -f 1 ess.pairs.gold/Ch7.N_EQU-LOC-TER-VIA.SgPosd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch7.N_EQU-LOC-TER-VIA.SgPosd.tsv     && echo "Jacobson (2001) Chapter 7 Noun Vocabulary - 1st/2nd/3rd Person Possessor Possessed EQU, LOC, TER, VIA - PASS" || echo "Jacobson (2001) Chapter 7 Noun Vocabulary - 1st/2nd/3rd Person Possessor Possessed EQU, LOC, TER, VIA - FAIL"
	@cut -f 1 ess.pairs.gold/Ch7.N_AblMod.SgPoss.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch7.N_AblMod.SgPoss.tsv     && echo "Jacobson (2001) Chapter 7 Noun Vocabulary - 1st/2nd/3rd Person Possessor Possessed Ablative-Modalis   - PASS" || echo "Jacobson (2001) Chapter 7 Noun Vocabulary - 1st/2nd/3rd Person Possessor Possessed Ablative-Modalis   - FAIL"
	@cut -f 1 ess.pairs.gold/Ch7.In-Chapter-Examples.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch7.In-Chapter-Examples.tsv     && echo "Jacobson (2001) Chapter 7 In-Chapter Examples - PASS" || echo "Jacobson (2001) Chapter 7 In-Chapter-Examples - FAIL"

test-ch8: ess.pairs.gold/Ch8.V_Intrg.1-2Intr.tsv ess.pairs.gold/Ch8.V_Intrg.2SgTrns.tsv ess.pairs.gold/Ch8.N_ABS.4PossPosd.tsv ess.pairs.gold/Ch8.In-Chapter-Examples.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch8.V_Intrg.1-2Intr.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch8.V_Intrg.1-2Intr.tsv     && echo "Jacobson (2001) Chapter 8 Verb Vocabulary - 1st/2nd Person Subject Interrogatives for Intransitive Verbs - PASS" || echo "Jacobson (2001) Chapter 8 Verb Vocabulary - 1st/2nd Person Subject Interrogatives for Intransitive Verbs - FAIL"
	@cut -f 1 ess.pairs.gold/Ch8.V_Intrg.2SgTrns.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch8.V_Intrg.2SgTrns.tsv     && echo "Jacobson (2001) Chapter 8 Verb Vocabulary - 2nd Person Subject Interrogatives for Transitive Verbs   - PASS" || echo "Jacobson (2001) Chapter 8 Verb Vocabulary - 2nd Person Subject Interrogatives for Transitive Verbs   - FAIL"
	@cut -f 1 ess.pairs.gold/Ch8.N_ABS.4PossPosd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch8.N_ABS.4PossPosd.tsv     && echo "Jacobson (2001) Chapter 8 Noun Vocabulary - 4th Person Possessor Possessed Absolutive                - PASS" || echo "Jacobson (2001) Chapter 8 Noun Vocabulary - 4th Person Possessor Possessed Absolutive                - FAIL"
	@cut -f 1 ess.pairs.gold/Ch8.In-Chapter-Examples.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch8.In-Chapter-Examples.tsv     && echo "Jacobson (2001) Chapter 8 In-Chapter Examples - PASS" || echo "Jacobson (2001) Chapter 8 In-Chapter-Examples - FAIL"


test-ch9: ess.pairs.gold/Ch9.V_ImprsAgnt.tsv ess.pairs.gold/Ch9.V_Intrg.3Intr.tsv ess.pairs.gold/Ch9.V_Intrg.3Trns.tsv ess.pairs.gold/Ch9.In-Chapter-Examples.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch9.V_ImprsAgnt.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch9.V_ImprsAgnt.tsv     && echo "Jacobson (2001) Chapter 9 Verb Vocabulary - Optional Impersonal Agent Verbs                          - PASS" || echo "Jacobson (2001) Chapter 9 Verb Vocabulary - Optional Impersonal Agent Verbs                          - FAIL"
	@cut -f 1 ess.pairs.gold/Ch9.V_Intrg.3Intr.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch9.V_Intrg.3Intr.tsv     && echo "Jacobson (2001) Chapter 9 Verb Vocabulary - 3rd Person Subject Interrogatives for Intransitive Verbs - PASS" || echo "Jacobson (2001) Chapter 9 Verb Vocabulary - 3rd Person Subject Interrogatives for Intransitive Verbs - FAIL"
	@cut -f 1 ess.pairs.gold/Ch9.V_Intrg.3Trns.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch9.V_Intrg.3Trns.tsv     && echo "Jacobson (2001) Chapter 9 Verb Vocabulary - 3rd Person Subject Interrogatives for Transitive Verbs   - PASS" || echo "Jacobson (2001) Chapter 9 Verb Vocabulary - 3rd Person Subject Interrogatives for Transitive Verbs   - FAIL"
	@cut -f 1 ess.pairs.gold/Ch9.In-Chapter-Examples.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch9.In-Chapter-Examples.tsv     && echo "Jacobson (2001) Chapter 9 In-Chapter Examples - PASS" || echo "Jacobson (2001) Chapter 9 In-Chapter-Examples - FAIL"

test-ch10: ess.pairs.gold/Ch10.V_Opt.PRS.2Intr.tsv ess.pairs.gold/Ch10.V_Opt.PRS.2SgTrns.tsv ess.pairs.gold/Ch10.V_Opt.NEG.2Intr.tsv ess.pairs.gold/Ch10.V_Opt.NEG.2Trns.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch10.V_Opt.PRS.2Intr.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch10.V_Opt.PRS.2Intr.tsv     && echo "Jacobson (2001) Chapter 10 Verb Vocabulary - 2nd Person Subject Intransitive Optative (PRS Tense)        - PASS" || echo "Jacobson (2001) Chapter 10 Verb Vocabulary - 2nd Person Subject Intransitive Optative (PRS Tense)        - FAIL"
	@cut -f 1 ess.pairs.gold/Ch10.V_Opt.PRS.2SgTrns.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch10.V_Opt.PRS.2SgTrns.tsv     && echo "Jacobson (2001) Chapter 10 Verb Vocabulary - 2nd Person Singular Subject Transitive Optative (PRS Tense) - PASS" || echo "Jacobson (2001) Chapter 10 Verb Vocabulary - 2nd Person Singular Subject Transitive Optative (PRS Tense) - FAIL"
	@cut -f 1 ess.pairs.gold/Ch10.V_Opt.NEG.2Intr.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch10.V_Opt.NEG.2Intr.tsv     && echo "Jacobson (2001) Chapter 10 Verb Vocabulary - 2nd Person Subject Intransitive Optative (NEG)              - PASS" || echo "Jacobson (2001) Chapter 10 Verb Vocabulary - 2nd Person Subject Intransitive Optative (NEG)              - FAIL"
	@cut -f 1 ess.pairs.gold/Ch10.V_Opt.NEG.2Trns.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch10.V_Opt.NEG.2Trns.tsv     && echo "Jacobson (2001) Chapter 10 Verb Vocabulary - 2nd Person Subject Transitive Optative (NEG)                - PASS" || echo "Jacobson (2001) Chapter 10 Verb Vocabulary - 2nd Person Subject Transitive Optative (NEG)                - FAIL"
	
test-ch11: ess.pairs.gold/Ch11.In-Chapter-Examples.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch11.In-Chapter-Examples.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch11.In-Chapter-Examples.tsv     && echo "Jacobson (2001) Chapter 11 In-Chapter Examples - PASS" || echo "Jacobson (2001) Chapter 11 In-Chapter Examples - FAIL"
	
test-ch12: ess.pairs.gold/Ch12.In-Chapter-Examples.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch12.In-Chapter-Examples.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch12.In-Chapter-Examples.tsv     && echo "Jacobson (2001) Chapter 12 In-Chapter Examples - PASS" || echo "Jacobson (2001) Chapter 12 In-Chapter Examples - FAIL"

test-ch13: ess.pairs.gold/Ch13.In-Chapter-Examples.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch13.In-Chapter-Examples.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch13.In-Chapter-Examples.tsv     && echo "Jacobson (2001) Chapter 13 In-Chapter Examples - PASS" || echo "Jacobson (2001) Chapter 13 In-Chapter Examples - FAIL"
	
test-ch14: ess.pairs.gold/Ch14.In-Chapter-Examples.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch14.In-Chapter-Examples.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch14.In-Chapter-Examples.tsv     && echo "Jacobson (2001) Chapter 14 In-Chapter Examples - PASS" || echo "Jacobson (2001) Chapter 14 In-Chapter Examples - FAIL"

test-ch15: ess.pairs.gold/Ch15.In-Chapter-Examples.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch15.In-Chapter-Examples.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch15.In-Chapter-Examples.tsv     && echo "Jacobson (2001) Chapter 15 In-Chapter Examples - PASS" || echo "Jacobson (2001) Chapter 15 In-Chapter Examples - FAIL"

test-ch17: ess.pairs.gold/Ch17.In-Chapter-Examples.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch17.In-Chapter-Examples.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch17.In-Chapter-Examples.tsv     && echo "Jacobson (2001) Chapter 17 In-Chapter Examples - PASS" || echo "Jacobson (2001) Chapter 17 In-Chapter Examples - FAIL"

test-ch18: ess.pairs.gold/Ch18.In-Chapter-Examples.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch18.In-Chapter-Examples.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch18.In-Chapter-Examples.tsv     && echo "Jacobson (2001) Chapter 18 In-Chapter Examples - PASS" || echo "Jacobson (2001) Chapter 18 In-Chapter Examples - FAIL"

test-filters: ess.pairs.gold/Filtered-Strings.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Filtered-Strings.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Filtered-Strings.tsv     && echo "Filtered Strings - PASS" || echo "Filtered-Strings - FAIL"
clean:
	rm -f ess.dot ess.pdf *.pairs *.pairs.tsv *.fomabin


bases.tsv: bases.tab
	cat bases.tab | sed 's,\r,\n,g' | sed 's,\v, ,g' > bases.tsv

.PHONY: all interactive clean test test-ch2
