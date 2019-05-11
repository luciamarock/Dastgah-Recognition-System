#!/bin/bash
#e9e12ac46d62cce3ea8afcd3e12580e7  matrices/scores.res
cd matrices 
rm -f scores.res
python statistics.py 
rm -f *.log
cat scores.res
cd ../
