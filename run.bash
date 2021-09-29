#!/bin/bash
echo ''
echo "Javascript"
node sync.js
echo ''
echo "Python"
python sync.py
echo ''
echo "Common Lisp"
sbcl --noinform --load sync.lisp --eval '(sync)' --quit
