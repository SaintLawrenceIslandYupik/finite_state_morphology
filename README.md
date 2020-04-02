# yupik-foma-v2

hello! this was my second attempt at implementing a morphological analyzer for Yupik using the `foma` FST toolkit. this README was written to document and describe some of the methods to my madness, and to assist anyone looking at this repo in understanding why certain things were implemented the way that they were. it's also a means for me to complain and vent about some aspects of the implementation that i'm not thrilled with, but didn't know how else to handle. hopefully, this README is sufficiently informative all on its own and withstands the test of time, idk we'll see! (emily, april 2, 2020).

this README is sectioned into multiple parts: one that describes some of the idiosyncracies of the `lexc` files, another that justifies the rewrite rules of the `foma` file, and yet another that describes some of the interesting questions and observations that have come out of developing this analyzer. the reader should note that many thoughts that are found in this README have also been documented as comments in their respective files.

---

## lexc file components

### header.txt

### roots

### derivational suffixes (postbases)

### inflectional suffixes

### person / number markers

### demonstratives 

### emotional roots

### enclitics

actually the most straightforward file in this monster of a project. i followed the badten (2008) tradition of demarcating enclitics with an __=__ sign, e.g. =llu. interestingly, there are quite a few assimilation patterns that occur when suffixing an enclitic, described in [AssimilateEnclitic](#assimilate-enclitic), all of them gleaned from examples given in badten (2008). i don't believe that these patterns are formally documented anywhere else.

### interrogatives

### numerals

### particles

### positionals

### postinflectional morphology

### postural roots

### pronouns

### quantifer-qualifier roots

### obsolete verb-root ete-

---

## foma rewrite rules

### AssimilateEnclitic
