#!/bin/bash
args=("$@")
if [ ${#args} -ge 3 ]; then 
    python crawler.py ${args[0]} ${args[1]} ${args[2]}
else
    python crawler.py
fi
