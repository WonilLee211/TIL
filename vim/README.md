# vim

## 학습 출처

<br>

### 단축키 관련 사이트

- [VimGenius](http://vimgenius.com/)

- [ShortcutFoo](https://www.shortcutfoo.com/app/dojos/vim/beginner-text-navigation/practice)

<br>

### 연습

- VimTutor
- [Vim Valley](https://vimvalley.com/course/basic-movement/welcome/)
- [Vim Golf](https://www.vimgolf.com/)


## setting

<br>

### 출처

- https://easy-study-note.tistory.com/7
- https://onurmark.tistory.com/3

<br>

### setting

1. vim-plug 설치
    - curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
        https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
2. ~/.vimrc cusmtomization

```vim
set nocompatible
filetype off
"set rtp+=~/.vim/bundle/Vundle.vim

call plug#begin('~/.vim/plugged')
"call vundle#begin()

Plug 'gmarik/Vundle.vim'

Plug 'ctrlpvim/ctrlp.vim' " Fuzzy search 지원 - 파일 탐색을 도와주는 플러그인
Plug 'SirVer/ultisnips' " snippet 입력을 도와주는 플러그인:wq
Plug 'honza/vim-snippets' " 많이 쓰는 스니펫을 모아둔 플러그인
Plug 'vim-airline/vim-airline' " 상태 표시창을 추가해주는 플러그인
Plug 'vim-airline/vim-airline-themes' " 상태표시창의 테마 설정 플러그인
Plug 'airblade/vim-gitgutter' " git에서 변화된 라인을 +, -와 같이 표시해주는 플러그인
Plug 'tpope/vim-fugitive' " vim에서 git명령을 사용할 수 있도록 지원하는 플러그인
Plug 'Valloric/YouCompleteMe' " 자동완성을 지원하는 플러그인
Plug 'rdnetto/YCM-Generator', { 'branch': 'stable' } " 자동완성 설정을 편하게 만들어주는 플러그인
Plug 'flazz/vim-colorschemes'
Plug 'tomasr/molokai'
let g:molokai_original=1
let g:rehash256 = 1

Plug 'majutsushi/tagbar' " tagbar 단축키 <F3>
Plug 'jiangmiao/auto-pairs'
Plug 'mattn/emmet-vim'
Plug 'tpope/vim-surround'
Plug 'scrooloose/nerdcommenter'
Plug 'ntpeters/vim-better-whitespace'
Plug 'terryma/vim-multiple-cursors'
Plug 'ronakg/quickr-cscope.vim' " cscope로 c분석을 도와주는 플러그인
Plug 'junegunn/vim-easy-align'
Plug 'derekwyatt/vim-fswitch'
Plug 'wellle/targets.vim'
Plug 'blueyed/vim-diminactive' " 활성창 강조
Plug 'tmhedberg/SimpylFold'
Plug 'vim-syntastic/syntastic' " syntax 교정 플러그인
Plug 'kien/ctrlp.vim' " 파일 찾기 플러그인

call plug#end()
"call vundle#end()

"문법 강조
syntax enable
if has("syntax")
  syntax on
endif
set t_Co=256
set number                     " show line number
set cursorline                 " show cursor line
set ruler                      " show cursor position on status bar
set cindent                    " according the C indenting rules
set autoindent                 " Copy indent from current line when starting a new line in insert mode
set smartindent                " When starting a new line '{', 'cinwords' '}'
set cino=(0,:0,t0              " Indent options
set enc=utf-8                  " Encoding vim inside
set fenc=utf-8                 " File encoding
set nocompatible               " Vi-compatible
set backspace=indent,eol,start " Backspace erase option
set hlsearch                   " Highlight all search pattern
set incsearch                  " While typing a search command, show where the pattern
set smartcase                  " search upper/lower case with lower/upper case
set diffopt=vertical
set wildmenu                   " show wildmenu
set wildmode=list:longest,full " wildmenu option
set path+=./**
set list                       " show tabs endlie, blank
set listchars=tab:→\ ,extends:›,precedes:‹,nbsp:·,trail:·
set showbreak=\\               " line break symbol
set showtabline=2
set visualbell
set laststatus=2               " show status bar
set statusline=\ %<%l:%v\ [%P]%=%a\ %h%m%r\ %F\
set hidden                     " When off a buffer is unloaded when it is abandoned
" 화면분할
set splitright
set splitbelow
" 화면분할 시 이동 단축키 리매핑
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>
set smarttab                   " delete by tap size with backspace bar
set expandtab                  " replace tab with space bar
set tabstop=4                  " tap size
set mouse=a                    " mouse active
set history=255                " the number of used commands in history
set mps=(:),{:},[:],<:>        " move to a pair bracket using '%' on another
set showmatch                  " highlight pair bracket
:au Filetype c,cpp,java set mps+=:;
" NORMAL 모드에서 숫자 위에 커서를 올린 후 <C-a>/<C-x>를 입력하면 숫자가 증가/감소합니다.
" 기본 1이며 숫자를 괄호 앞에 명시하여 연산할 수 있습니다. 진법에 상관없이 연산이 가능합니다.
set nf=alpha,octal,hex,bin
" scroll option
set nowrap
set sidescroll=2
set sidescrolloff=10
set ww+=h,l
" code foliding
set foldmethod=indent
set foldlevel=99
nnoremap <space> za
"bracket auto complete
inoremap ( ()<Esc>i
inoremap { {}<Esc>i
inoremap {<CR> {<CR>}<Esc>O
inoremap [ []<Esc>i
inoremap ' ''<Esc>i
inoremap " ""<Esc>i
autocmd FileType cpp : inoremap <<space> <<<space>
autocmd FileType cpp : inoremap ><space> >><space>
autocmd FileType cpp : inoremap :main<CR> #include<space><iostream><CR><CR>using<space>namespace<space>std;<CR><CR>int<space>main(){<CR><CR>}<esc><k>


" Color scheme
colorscheme molokai
hi MatchParen ctermfg=208 ctermbg=233 cterm=bold

augroup ctype
        autocmd!
        autocmd BufRead,BufNewFile *.h,*.c set filetype=c
augroup END

augroup filetype_c_cpp
        autocmd!
        autocmd FileType c,cpp setl ts=8 sw=8 sts=8
        autocmd FileType c,cpp :TagbarOpen
augroup END

augroup filetype_quickfix
        autocmd!
        autocmd FileType qf setl nonumber norelativenumber nocursorline
augroup END

augroup open_lastread
        autocmd!
        autocmd BufReadPost *
                \ if line("'\"") > 0 && line("'\"") <= line("$") |
                \   exe "normal g`\"" |
                \ endif
augroup END


" Make command
command -nargs=* Make wa | make <args> | cwindow 3

nnoremap <F5> :Make<CR>
nnoremap <F6> :Make check<CR>

let g:ycm_confirm_extra_conf           = 0
let g:ycm_auto_trigger                 = 1
let g:ycm_key_list_select_completion   = ['<C-j>', '<Down>']
let g:ycm_key_list_previous_completion = ['<C-k>', '<Up>']
let g:ycm_autoclose_preview_window_after_completion = 1

nnoremap <leader>gl :YcmCompleter GoToDeclaration <CR>
nnoremap <leader>gf :YcmCompleter GoToDefinition <CR>
nnoremap <leader>gg :YcmCompleter GoToDefinitionElseDeclaration <CR>

let g:UltiSnipsListSnippets        = "<C-g><Tab>"
let g:UltiSnipsExpandTrigger       = "<Tab>"
let g:UltiSnipsJumpForwardTrigger  = "<Tab>"
let g:UltiSnipsJumpBackwardTrigger = "<S-Tab>"
let g:UltiSnipsSnippetDirectories  = ['~/.vim/UltiSnips', 'UltiSnips']
let g:UltiSnipsEditSplit           = "vertical"

set wildignore+=*/tmp/*,*.so,*.swp,*.zip     " MacOSX/Linux
" Window
"set wildignore+=*\\tmp\\*,*.swp,*.zip,*.exe

let g:ctrlp_custom_ignore = {
        \ 'dir':  '\v[\/]\.(git|hg|svn)$',
        \ 'file': '\v\.(exe|so|dll)$',
        \ 'link': 'some_bad_symbolic_links',
\ }

let g:ctrlp_user_command = ['.git', 'cd %s && git ls-files -co --exclude-standard']

let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#buffer_nr_show = 1
let g:airline#extensions#tabline#formatter = 'unique_tail'
let g:airline_theme='molokai'
let g:airline_powerline_fonts = 1

let g:NERDSpaceDelims = 1
let g:NERDCompactSexyComs = 1
let g:NERDDefaultAlign = 'left'
let g:NERDCommentEmptyLines = 1
let g:NERDTrimTrailingWhitespace = 1
let g:NERDToggleCheckAllLines = 1
let g:NERDCreateDefaultMappings = 0
let g:NERDCustomDelimiters = {
        \ 'c': { 'leftAlt': '/*', 'rightAlt': '*/', 'left': '//' },
        \ 'cpp': { 'leftAlt': '/*', 'rightAlt': '*/', 'left': '//' }
\ }

nmap <Leader>; <plug>NERDCommenterToggle
vmap <Leader>; <plug>NERDCommenterToggle gv

function! LoadCscope()
        let db = findfile("cscope.out", ".;")
        if (!empty(db))
                let path = strpart(db, 0, match(db, "/cscope.out$"))
                set nocscopeverbose " suppress 'duplicate connection' error
                exe "cs add " . db . " " . path
                set cscopeverbose
                " else add the database pointed to by environment variable
        elseif $CSCOPE_DB != ""
                cs add $CSCOPE_DB
        endif
endfunction
au BufEnter /* call LoadCscope()

" Open QF when multiple matches.
let g:quickr_cscope_keymaps = 0

nmap <leader>cs <plug>(quickr_cscope_symbols)
nmap <leader>cg <plug>(quickr_cscope_global)
nmap <leader>cc <plug>(quickr_cscope_callers)
nmap <leader>cf <plug>(quickr_cscope_files)
nmap <leader>ci <plug>(quickr_cscope_includes)
nmap <leader>ct <plug>(quickr_cscope_text)
nmap <leader>ce <plug>(quickr_cscope_egrep)
nmap <leader>cd <plug>(quickr_cscope_functions)
nmap <leader>ca <plug>(quickr_cscope_assignments)

let g:AutoPairsFlyMode = 0
let g:AutoPairsShortcutBackInsert = '<M-b>'

nmap <F3> : Tagbar<CR>
let g:diminactive_enable_focus = 1

```

3. vim 실행 상태에서 `:PlugInstall` 명령어 실행

4. Ycm 자동완성 기능을 설정하기 위한 언어 및 버전 설치
    - `brew install cpp cmake python3-dev`
5. clang-completer 컴파일 및 설치
    - `cd ~/.vim/plugged/YouCompleteMe/`
    - `/.install.py --clang-completer`

