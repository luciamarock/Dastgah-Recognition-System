#!/bin/bash
echo processing $1_$2 of $3
cp scores/$1_* ./
cp $1_$2.csv unknown_1.csv

python read_float_notet.py $1 $3
python read_float_notet.py unknown 1 
mv $1_matrix.csv ./matrices
mv unknown_matrix.csv ./matrices
rm -f *.csv 
cd matrices/
python read_matrix.py 
python expected.py $1
rm -f unknown_matrix.csv
cd ../

