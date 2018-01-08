"%s/\n.*?.*\n//
:%s/\r//

" Command => vim -c "argdo source reformat.vim | w" *.count
