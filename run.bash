#!/bin/bash
echo 'Synchronous Versions'
echo ''
echo "Javascript"
node sync.js
echo ''
echo "Python"
python sync.py
echo ''
echo "Common Lisp"
sbcl --noinform --load sync.lisp --eval '(sync)' --quit

echo ''
echo 'Asynchronous Versions'
echo ''
echo "Javascript"
node async.js
# echo ''
# echo "Python"
# python async.py
echo ''
echo "Common Lisp"
sbcl --noinform --load async.lisp --eval '(progn (async1) (async2))' --quit
