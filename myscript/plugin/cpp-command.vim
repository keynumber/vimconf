" switch/case代码生成
"
" 根据一样或者多行case条件生成c/c++的switch/case语句
" 各个不同的case条件用空格隔开，可以分散在连续的多行
command! -range GenSwitchCase :<line1>,<line2>call GenSwitchCase()<CR>
