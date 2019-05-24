" ============================================================================
" FILE: scriptnames.py
" AUTHOR: delphinus <me@delphinus.dev>
" License: MIT license
" ============================================================================

function! denite#source#scriptnames#load() abort
  let save_verbose = &verbose
  let &verbose = 0
  redir => out
  silent scriptnames
  redir END
  let &verbose = save_verbose
  return out
endfunction
