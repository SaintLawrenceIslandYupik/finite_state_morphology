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

### emotional roots

-

### enclitics

actually the most straightforward file in this monster of a project. i followed the Badten (2008) tradition of demarcating enclitics with an __=__ sign, e.g. *=llu*. interestingly, there are quite a few assimilation patterns that occur when suffixing an enclitic, described in [AssimilateEnclitic](#assimilate-enclitic), all of them gleaned from examples given in Badten (2008). i don't believe that these patterns are formally documented anywhere else.

### interrogatives

this file makes me very sad and its problems are documented in the file therein. i did my best to translate chapters 8-9 in Jacobson (2001) to code, but interrogatives in Yupik are just confusing and not that well-documented to begin with, so idk how successful that attempt was. most of the interrogative forms documented in chapters 8-9 ended up in the exceptions file.

### numerals

pretty straightforward, except for the fact that the numerals are hard-coded and not all of them are listed here in the lexc. there also appear to be two derivational morphemes that are used exclusively with numerals, and presumably allow for additional derivation before inflection.

### particles

also very straightforward! practically on par with enclitics. the reader should note though that some of the particles were manually added while implementing the unit test cases, and that some of the particles also classify as other...parts of speech, e.g. *whani* is also a demonstrative, but the dictionary also listed it as a particle.

### positionals

-

### postinflectional morphology

-

### postural roots

-

### pronouns

### quantifer-qualifier roots

-

### obsolete verb-root ete-

## exceptions

## parallel forms

---

## foma rewrite rules

### AssimilateEnclitic
