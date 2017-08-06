if !has('python')
finish
endif

function! Doxify()
    pyfile ~/src/python/doxify/doxify.py
endfunc

command! Doxify call Doxify()
