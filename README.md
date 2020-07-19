# Finite state morphological analyzer for St. Lawrence Island Yupik

**This resource is part of the linguistic and cultural heritage of the St. Lawrence Island Yupik people. By accessing this resource, you agree to treat this resource, the St. Lawrence Island Yupik language, the St. Lawrence Island Yupik culture, and the St. Lawrence Island Yupik people with dignity and respect. If you do not agree to these conditions, you may not access this resource and you may not make copies of this resource.**

If you agree to these conditions, you may access this resource under the terms of the Creative Commons Attribution No-Commercial 4.0 license (https://creativecommons.org/licenses/by-nc/4.0/).


## Version

This is the development version of the St. Lawrence Island Yupik finite-state morphological analyzer.

This version incorporates changes made after the release of version 2.1 on 19 July 2020 at 13:01:49 2020 -0500.


## Overview

hello! this was my second attempt at implementing a morphological analyzer for Yupik using the `foma` FST toolkit. this README was written to document and describe some of the methods to my madness, and to assist anyone looking at this repo in understanding why certain things were implemented the way that they were. it's also a means for me to complain and vent about some aspects of the implementation that i'm not thrilled with, but didn't know how else to handle. hopefully, this README is sufficiently informative all on its own and withstands the test of time, idk we'll see! (emily, april 2, 2020).

this README is sectioned into multiple parts: one that describes some of the idiosyncracies of the `lexc` files, another that justifies the rewrite rules of the `foma` file, and yet another that describes some of the interesting questions and observations that have come out of developing this analyzer. the reader should note that many thoughts that are found in this README have also been documented as comments in their respective files.

---

## lexc file components

### header.txt

the header for the `lexc` file is pretty well-documented. it defines all of the multicharacter symbols and the root lexicons. some things that may be of interest to the reader: labels for lexical items are denoted by parentheses (), e.g., (N) labels a nominal root. morphological tags that stand in for morphemes are denoted by brackets [], e.g., *[Abs.Pl]* stands in for the absolutive singular morpheme, written *~sf:-w(e)t* in Jacobson (2001) Notation. any multicharacter symbol written with braces {} was defined to facilitate rule-writing. since braces are special characters in the `lexc` programming language, they have to be escaped with a % sign. also all of the Jacobson (2001) Notation symbols have been adapted to this {} format, e.g. *-w = %{.w.%}*, since people smarter than me have suggested steering clear of Jacobson (2001) Notation. we want a clear distinction here between actual text and symbols used to facilitate rule-writing.

### roots

roots! these are all of the noun roots and verb roots from Jacobson (2001) and Badten (2008). i manually added a few when i came across them in the postbase examples given in Badten (2008). unclear if those roots are true roots since they aren't listed as lexical entries in the dictionary, but what do i know. the noun roots are classified into nine inflection classes and the verb roots are classified into seven. one thing worth noting for noun roots is that *weak -gh* is written as **{g}h** in the intermediate form to distinguish it from *marked strong* and *strong -gh*. for verb roots, *special -te* is considered its own inflection class and is written as **{t}e\*** in the intermediate form to distinguish it from ordinary *-te*. lastly, roots that contain untraditional endings like *-ghh* or *-l* are grouped with roots that end in *-g*, *-w*, and *-ghw* for now, and any root that ends in *-eg* is considered a member of the *semi-final -e* inflection class.

### derivational suffixes (postbases)

i coded a list of postbases for *each* inflection class. this is significant, since it allows me to code only the morphophonological rules relevant for that particular class. for instance, since uvular dropping affects all roots that end in *-gh*, the uvular dropping symbol **{.c.}** appears in the postbase lists for all of the inflection classes whose roots end in *-gh*. the symbol will not, however, appear in the postbase lists for all other inflection classes, e.g. roots that end in a vowel, say.

with respect to maintenance, this is a pain and i hate it. but it's allowed for simpler `foma` rewrite rules and appears to handle exceptions much better than the previous analyzer that does not organize the roots into their respective inflection classes.

### inflectional suffixes

the same holds true for the inflectional suffixes, in that there exists a unique inflectional paradigm for each inflection class, and only the morphophonological rules relevant to that class are coded in the inflectional paradigm. again, very annoying for maintenance, but it seems to work well.

one thing to observe about the inflectional paradigms is that in some verb moods, there is less consistency than in others. for instance, for the indicative mood, there's a single morpheme that marks transitivity and mood and then the morphemes that mark person/number. this is not true for the interrogative and optative moods. the morpheme that marks transitivity and mood for these two moods vary depending on the person/number. that being said, it was easier to code the entire inflectional paradigm, including person/number markers, for the interrogative and optative moods here in this part of the `lexc` file. for more "consistent" moods like the indicative, the person/number markers are coded in [a different directory]{#person-/-number-markers}.

### person / number markers

i coded a table of person/number morphemes for each mood. these files are pretty straightforward and self-explanatory.

### demonstratives 

this took a couple of tries to get right, but after rereading Jacobson (2001) chapter 16 a few times, i think it's OK now? there's a note inside the *demonstratives.txt* file that explains my interpretation of Jacobson's documentation on demonstratives, and how the `lexc` file reflects that interpretation. generally-speaking though, there are four types of demonstratives: (1) demonstrative pronouns, (2) vocatives, (3) demonstrative adverbs, and (4) anaphoric forms. vocatives and demonstrative adverbs were hard-coded for the sake of simplicity, while demonstrative adverbs and the anaphoric forms are constructed in `lexc` via continuation classes. the anaphoric forms are constructed using the only prefix attested in Yupik, and i use the placeholder `[Anaphor]` to represent this prefix, since it has several allomorphs. a [`foma` rewrite rule](#ResolveDemAnaphor) handles this allomorphy. the reader should also note that while Appendix III in Jacobson (2001) lists a number of inflected demonstratives, that list is not complete.

as for any postbases that can suffix to demonstratives, they can presumably only suffix to a demonstrative's adverbial particle form, and can all be found in Badten (2008). these postbases are listed in the *dem-suffixes.txt* file under the `DemAdvPB` lexicon. fieldwork conducted in July 2018 with Speaker 14 found that the empty base **pi** and obsolete verb-root **ete** may also suffix to a demonstrative's adverbial particle form, as in **pikapiyaqunaasi ** and **amantuq** respectively.

### emotional roots

the list of emotional roots was taken from one of the appendices in Badten (2008), and the list of emotional root postbases from Jacobson (2001) chapter 13. they're all organized by inflection class. if i remember correctly, Badten (2008) also has a list of emotional root postbases, but there were a lot of discrepancies between Badten (2008) and Jacobson (2001) in regards to the correct Jacobson (2001) Notation for each postbase. i ended up coding the set of symbols that had the most examples supporting it. lastly, according to Badten (2008), there are a number of emotioanl root postbases that can be used with verb roots that express emotion (p.629, 631, 648, 649).

### enclitics

actually the most straightforward file in this monster of a project. i followed the Badten (2008) tradition of demarcating enclitics with an __=__ sign, e.g. *=llu*. interestingly, there are quite a few assimilation patterns that occur when suffixing an enclitic, described in [AssimilateEnclitic](#assimilateenclitic), all of them gleaned from examples given in Badten (2008). i don't believe that these patterns are formally documented anywhere else.

### interrogatives

this file makes me very sad and its problems are documented in the file therein. i did my best to translate chapters 8-9 in Jacobson (2001) to code, but interrogatives in Yupik are just confusing and not that well-documented to begin with, so idk how successful that attempt was. most of the interrogative forms documented in chapters 8-9 ended up in the exceptions file.

### numerals

pretty straightforward, except for the fact that the numerals are hard-coded and not all of them are listed here in the lexc. there also appear to be two derivational morphemes that are used exclusively with numerals, and presumably allow for additional derivation before inflection.

### particles

also very straightforward! practically on par with enclitics. the reader should note though that some of the particles were manually added while implementing the unit test cases, and that some of the particles also classify as other...parts of speech, e.g. *whani* is also a demonstrative, but the dictionary also listed it as a particle.

### positionals

this list was taken from...Jacobson (2001) chapter 18? 17? in any case, there aren't many positionals and they don't appear to function all that differently from nominal roots. on p.113 though in Jacobson (2001), he does mention that positionals can inflect for an alternative allative (terminalis), which is handled in this file.

### postinflectional morphology

### postural roots

like the emotional roots, this list of postural roots was taken from one of the appendices in Badten (2008), and i deferred to the previous analyzer to figure out which -gh's were strong and which were weak. that being said, there might be errors. also according to Jacobson (2001), there are a few verb roots that can function like postural roots, and according to Badten (2008), there are postural root postbases that can suffix to "certain other verb roots" (p.648). the files handles these edge cases.

### pronouns

Appendix II of Jacobson (2001) lists nearly all of the attested pronouns in Yupik, but i think it's missing the ablative-modalis forms? not sure tbh, but there a couple of lexical items that appear in the elementary primers that are definitely pronouns, but aren't listed in Appendix II, e.g. **ellmineng* and **elpeneng**.

### quantifer-qualifier roots

these were coded according to the description given in chapter 12 of Jacobson (2001). in the previous iteration of the analyzer, all of the quantifier-qualifier roots were marked as ending in a strong *gh*. given the morphophonological rules in the quantifier-qualifier inflectional paradigm, however, i don't think this distinction actually matters. i left it as is though, since i'm assuming there was a good reason for marking these as strong *gh* to begin with.

### obsolete verb-root ete-

this verb root was also introduced, alongside quantifier-qualifier roots in chapter 12, of Jacobson (2001). it maps to a really wonky-looking intermediate form *{I}te\** because (1) it has two forms: **ete** and **ite**, hence the allomorph symbol {I} and (2) it ends in *special -te*. there is a `foma` rewrite rule that handles [{I}]{resolvei}.

## exceptions

these are what they sound like. they're surface forms that deviate from what's expected to surface after carrying out each morphophonological rule. i did my best to keep this list organized, so they're grouped by "type", e.g. demonstrative exceptions, noun exceptions, verb exceptions, etc. hopefully, by the time you're reading this, i've also gone in and noted the source of each of these exceptions, e.g. from Jacobson (2001), Badten (2008, etc. the header file for `exceptions.lexc` is identical to that of `ess.lexc` save for the `Root` lexicon.

## parallel forms

also what they sound like. these are valid surface forms that exist in Yupik in addition to the expected surface form. again, i tried to keep this file organized, noting the source of each of these parallel forms. the header file is also identical to that of `ess.lexc` save for the `Root` lexicon.

---

## foma rewrite rules

### ResolveI

### ResolveDemAnaphor

### AssimilateEnclitic
