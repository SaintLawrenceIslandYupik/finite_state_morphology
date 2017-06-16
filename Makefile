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



test: test-ch2 test-ch3 test-ch4 test-ch5 test-ch6 test-ch7 test-ch8 test-ch9 test-ch10


test-ch2: ess.pairs.gold/Ch2.N_ABS.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch2.N_ABS.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch2.N_ABS.tsv     && echo "Jacobson (2001) Chapter 2 Noun Vocabulary - Absolutive Singular, Dual, & Plural   - PASS" || echo "Jacobson (2001) Chapter 2 Noun Vocabulary - Absolutive Singular, Dual, & Plural   - FAIL"
	@cut -f 1 ess.pairs.gold/Ch2.N_AblMod.tsv  | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch2.N_AblMod.tsv  && echo "Jacobson (2001) Chapter 2 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - PASS" || echo "Jacobson (2001) Chapter 2 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - FAIL"


test-ch3: ess.pairs.gold/Ch3.N_ABS.tsv ess.pairs.gold/Ch3.N_AblMod.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch3.N_ABS.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch3.N_ABS.tsv     && echo "Jacobson (2001) Chapter 3 Noun Vocabulary - Absolutive Singular, Dual, & Plural   - PASS" || echo "Jacobson (2001) Chapter 3 Noun Vocabulary - Absolutive Singular, Dual, & Plural   - FAIL"
	@cut -f 1 ess.pairs.gold/Ch3.N_AblMod.tsv  | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch3.N_AblMod.tsv  && echo "Jacobson (2001) Chapter 3 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - PASS" || echo "Jacobson (2001) Chapter 3 Noun Vocabulary - Ablative-Modalis Unpossessed Singular - FAIL"
	@cut -f 1 ess.pairs.gold/Ch3.V_IntrInd.tsv | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch3.V_IntrInd.tsv && echo "Jacobson (2001) Chapter 3 Verb Vocabulary - Intransitive Indicative               - PASS" || echo "Jacobson (2001) Chapter 3 Verb Vocabulary - Intransitive Indicative               - FAIL"

test-ch4: ess.pairs.gold/Ch4.N_ABS.1PossPosd.tsv ess.pairs.gold/Ch4.N_ABS.2PossPosd.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch4.N_ABS.1PossPosd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch4.N_ABS.1PossPosd.tsv     && echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 1st Person Possessor Possessed Absolutive - PASS" || echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 1st Person Possessor Possessed Absolutive - FAIL"
	@cut -f 1 ess.pairs.gold/Ch4.N_ABS.2PossPosd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch4.N_ABS.2PossPosd.tsv     && echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 2nd Person Possessor Possessed Absolutive - PASS" || echo "Jacobson (2001) Chapter 4 Noun Vocabulary - 2nd Person Possessor Possessed Absolutive - FAIL"

test-ch5: ess.pairs.gold/Ch5.N_EQU-LOC-TER-VIA.Unpd.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch5.N_EQU-LOC-TER-VIA.Unpd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch5.N_EQU-LOC-TER-VIA.Unpd.tsv     && echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Unpossessed Equalis, Localis, Terminalis, Vialis - PASS" || echo "Jacobson (2001) Chapter 5 Noun Vocabulary - Unpossessed Equalis, Localis, Terminalis, Vialis    - FAIL"

test-ch6: ess.pairs.gold/Ch6.N_ABS.3PossPosd.tsv ess.pairs.gold/Ch6.N_REL.Unpd.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch6.N_ABS.3PossPosd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch6.N_ABS.3PossPosd.tsv     && echo "Jacobson (2001) Chapter 6 Noun Vocabulary - 3rd Person Possessor Possessed Absolutive - PASS" || echo "Jacobson (2001) Chapter 6 Noun Vocabulary - 3rd Person Possessor Possessed Absolutive - FAIL"
	@cut -f 1 ess.pairs.gold/Ch6.N_REL.Unpd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch6.N_REL.Unpd.tsv     && echo "Jacobson (2001) Chapter 6 Noun Vocabulary - Unpossessed Relative Case - PASS" || echo "Jacobson (2001) Chapter 6 Noun Vocabulary - Unpossessed Relative Case - FAIL"

test-ch7: ess.pairs.gold/Ch7.N_REL.Posd.tsv ess.pairs.gold/Ch7.V_TrnsInd.tsv ess.pairs.gold/Ch7.N_EQU-LOC-TER-VIA.SgPosd.tsv ess.pairs.gold/Ch7.N_AblMod.SgPoss.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch7.N_REL.Posd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch7.N_REL.Posd.tsv     && echo "Jacobson (2001) Chapter 7 Noun Vocabulary - Possessed Relative Case   - PASS" || echo "Jacobson (2001) Chapter 7 Noun Vocabulary - Possessed Relative Case   - FAIL"
	@cut -f 1 ess.pairs.gold/Ch7.V_TrnsInd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch7.V_TrnsInd.tsv     && echo "Jacobson (2001) Chapter 7 Verb Vocabulary - Transitive Indicative     - PASS" || echo "Jacobson (2001) Chapter 7 Verb Vocabulary - Transitive Indicative   - FAIL"
	@cut -f 1 ess.pairs.gold/Ch7.N_EQU-LOC-TER-VIA.SgPosd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch7.N_EQU-LOC-TER-VIA.SgPosd.tsv     && echo "Jacobson (2001) Chapter 7 Noun Vocabulary - Singular Possessed Equalis, Localis, Terminalis, Vialis    - PASS" || echo "Jacobson (2001) Chapter 7 Noun Vocabulary - Singular Possessed Equalis, Localis, Terminalis, Vialis    - FAIL"
	@cut -f 1 ess.pairs.gold/Ch7.N_AblMod.SgPoss.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch7.N_AblMod.SgPoss.tsv     && echo "Jacobson (2001) Chapter 7 Noun Vocabulary - Ablative-Modalis Possessed Singular - PASS" || echo "Jacobson (2001) Chapter 7 Noun Vocabulary - Ablative-Modalis Possessed Singular - FAIL"

test-ch8: ess.pairs.gold/Ch8.V_Intrg.2Intr.tsv ess.pairs.gold/Ch8.V_Intrg.2SgTrns.tsv ess.pairs.gold/Ch8.N_ABS.4PossPosd.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch8.V_Intrg.2Intr.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch8.V_Intrg.2Intr.tsv     && echo "Jacobson (2001) Chapter 8 Verb Vocabulary - 2nd Person Subject Interrogatives for Intransitive Verbs - PASS" || echo "Jacobson (2001) Chapter 8 Verb Vocabulary - 2nd Person Subject Interrogatives for Intransitive Verbs - FAIL"
	@cut -f 1 ess.pairs.gold/Ch8.V_Intrg.2SgTrns.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch8.V_Intrg.2SgTrns.tsv     && echo "Jacobson (2001) Chapter 8 Verb Vocabulary - 2nd Person Subject Interrogatives for Transitive Verbs   - PASS" || echo "Jacobson (2001) Chapter 8 Verb Vocabulary - 2nd Person Subject Interrogatives for Transitive Verbs   - FAIL"
	@cut -f 1 ess.pairs.gold/Ch8.N_ABS.4PossPosd.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch8.N_ABS.4PossPosd.tsv     && echo "Jacobson (2001) Chapter 8 Noun Vocabulary - 4th Person Possessor Possessed Absolutive                - PASS" || echo "Jacobson (2001) Chapter 8 Noun Vocabulary - 4th Person Possessor Possessed Absolutive                - FAIL"

test-ch9: ess.pairs.gold/Ch9.V_ImprsAgnt.tsv ess.pairs.gold/Ch9.V_Intrg.3Intr.tsv ess.pairs.gold/Ch9.V_Intrg.3Trns.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch9.V_ImprsAgnt.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch9.V_ImprsAgnt.tsv     && echo "Jacobson (2001) Chapter 9 Verb Vocabulary - Optional Impersonal Agent Verbs                          - PASS" || echo "Jacobson (2001) Chapter 9 Verb Vocabulary - Optional Impersonal Agent Verbs                          - FAIL"
	@cut -f 1 ess.pairs.gold/Ch9.V_Intrg.3Intr.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch9.V_Intrg.3Intr.tsv     && echo "Jacobson (2001) Chapter 9 Verb Vocabulary - 3rd Person Subject Interrogatives for Intransitive Verbs - PASS" || echo "Jacobson (2001) Chapter 9 Verb Vocabulary - 3rd Person Subject Interrogatives for Intransitive Verbs - FAIL"
	@cut -f 1 ess.pairs.gold/Ch9.V_Intrg.3Trns.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch9.V_Intrg.3Trns.tsv     && echo "Jacobson (2001) Chapter 9 Verb Vocabulary - 3rd Person Subject Interrogatives for Intransitive Verbs - PASS" || echo "Jacobson (2001) Chapter 9 Verb Vocabulary - 3rd Person Subject Interrogatives for Intransitive Verbs - FAIL"

test-ch10: ess.pairs.gold/Ch10.V_Opt.PRS.2Intr.tsv ess.pairs.gold/Ch10.V_Opt.PRS.2SgTrns.tsv ess.pairs.gold/Ch10.V_Opt.NEG.2Intr.tsv ess.pairs.gold/Ch10.V_Opt.NEG.2Trns.tsv ess.fomabin
	@cut -f 1 ess.pairs.gold/Ch10.V_Opt.PRS.2Intr.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch10.V_Opt.PRS.2Intr.tsv     && echo "Jacobson (2001) Chapter 10 Verb Vocabulary - 2nd Person Subject Intransitive Optative (PRS Tense) - PASS" || echo "Jacobson (2001) Chapter 10 Verb Vocabulary - 2nd Person Subject Intransitive Optative (PRS Tense) - FAIL"
	@cut -f 1 ess.pairs.gold/Ch10.V_Opt.PRS.2SgTrns.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch10.V_Opt.PRS.2SgTrns.tsv     && echo "Jacobson (2001) Chapter 10 Verb Vocabulary - 2nd Person Singular Subject Transitive Optative (PRS Tense) - PASS" || echo "Jacobson (2001) Chapter 10 Verb Vocabulary - 2nd Person Singular Subject Transitive Optative (PRS Tense) - FAIL"
	@cut -f 1 ess.pairs.gold/Ch10.V_Opt.NEG.2Intr.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch10.V_Opt.NEG.2Intr.tsv     && echo "Jacobson (2001) Chapter 10 Verb Vocabulary - 2nd Person Subject Intransitive Optative (NEG) - PASS" || echo "Jacobson (2001) Chapter 10 Verb Vocabulary - 2nd Person Subject Intransitive Optative (NEG) - FAIL"
	@cut -f 1 ess.pairs.gold/Ch10.V_Opt.NEG.2Trns.tsv     | sort -d -f | uniq | flookup -i -w "" ess.fomabin | sort -d -f | diff - ess.pairs.gold/Ch10.V_Opt.NEG.2Trns.tsv     && echo "Jacobson (2001) Chapter 10 Verb Vocabulary - 2nd Person Subject Transitive Optative (NEG) - PASS" || echo "Jacobson (2001) Chapter 10 Verb Vocabulary - 2nd Person Subject Transitive Optative (NEG) - FAIL"


clean:
	rm -f ess.dot ess.pdf *.pairs *.pairs.tsv *.fomabin


bases.tsv: bases.tab
	cat bases.tab | sed 's,\r,\n,g' | sed 's,\v, ,g' > bases.tsv

.PHONY: all interactive clean test test-ch2
