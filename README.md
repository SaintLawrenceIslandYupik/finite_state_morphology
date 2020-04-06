# yupik-foma-v2

hello! this was my second attempt at implementing a morphological analyzer for Yupik using the `foma` FST toolkit. this README was written to document and describe some of the methods to my madness, and to assist anyone looking at this repo in understanding why certain things were implemented the way that they were. it's also a means for me to complain and vent about some aspects of the implementation that i'm not thrilled with, but didn't know how else to handle. hopefully, this README is sufficiently informative all on its own and withstands the test of time, idk we'll see! (emily, april 2, 2020).

this README is sectioned into multiple parts: one that describes some of the idiosyncracies of the `lexc` files, another that justifies the rewrite rules of the `foma` file, and yet another that describes some of the interesting questions and observations that have come out of developing this analyzer. the reader should note that many thoughts that are found in this README have also been documented as comments in their respective files.

---

## lexc file components

### header.txt

the header for the `lexc` file is pretty well-documented. it defines all of the multicharacter symbols and the root lexicons. some things that may be of interest to the reader: labels for lexical items are denoted by parentheses (), e.g., (N) labels a nominal root. morphological tags that stand in for morphemes are denoted by brackets [], e.g., *[Abs.Pl]* stands in for the absolutive singular morpheme, written *~sf:-w(e)t* in Jacobson (2001) Notation. any multicharacter symbol written with braces {} was defined to facilitate rule-writing. since braces are special characters in the `lexc` programming language, they have to be escaped with a % sign. also all of the Jacobson (2001) Notation symbols have been adapted to this {} format, e.g. *-w = %{.w.%}*, since people smarter than me have suggested steering clear of Jacobson (2001) Notation. we want a clear distinction here between actual text and symbols used to facilitate rule-writing.

### roots

### derivational suffixes (postbases)

### inflectional suffixes

### person / number markers

### demonstratives 

-

### emotional roots

the list of emotional roots was taken from one of the appendices in Badten(2008), and the list of emotional root postbases from Jacobson (2001) chapter 13. they're all organized by inflection class. if i remember correctly, Badten (2008) also has a list of emotional root postbases, but there were a lot of discrepancies between Badten (2008) and Jacobson (2001) in regards to the correct Jacobson (2001) Notation for each postbase. i ended up coding the set of symbols that had the most examples supporting it. lastly, according to Badten (2008), there are a number of emotioanl root postbases that can be used with verb roots that express emotion (p.629, 631, 648, 649).

### enclitics

actually the most straightforward file in this monster of a project. i followed the Badten (2008) tradition of demarcating enclitics with an __=__ sign, e.g. *=llu*. interestingly, there are quite a few assimilation patterns that occur when suffixing an enclitic, described in [AssimilateEnclitic](#assimilate-enclitic), all of them gleaned from examples given in Badten (2008). i don't believe that these patterns are formally documented anywhere else.

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

-

### quantifer-qualifier roots

-

### obsolete verb-root ete-

-

## exceptions

## parallel forms

---

## foma rewrite rules

### AssimilateEnclitic
