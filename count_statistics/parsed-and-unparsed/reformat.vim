:%s/a\n/a\t/
:%s/e\n/e\t/
:%s/i\n/i\t/
:%s/u\n/u\t/
:%s/p\n/p\t/
:%s/t\n/t\t/
:%s/k\n/k\t/
:%s/q\n/q\t/
:%s/v\n/v\t/
:%s/l\n/l\t/
:%s/z\n/z\t/
:%s/y\n/y\t/
:%s/r\n/r\t/
:%s/g\n/g\t/
:%s/w\n/w\t/
:%s/h\n/h\t/
:%s/f\n/f\t/
:%s/s\n/s\t/
:%s/m\n/m\t/
:%s/n\n/n\t/

" Command => vim -c "argdo source reformat.vim | w" *.count
