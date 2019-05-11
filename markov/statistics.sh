#!/bin/bash

cd matrices 
sed -i "s/1\\t3\\t0\\t1/1\\t0\\t0\\t1/g" results.log
sed -i "s/1\\t0\\t1\\t1/1\\t1\\t1\\t1/g" results.log
sed -i "s/1\\t0\\t3\\t1/1\\t3\\t3\\t1/g" results.log
sed -i "s/1\\t1\\t0\\t1/1\\t0\\t0\\t1/g" results.log
sed -i "s/6\\t1\\t6\\t4/6\\t6\\t6\\t4/g" results.log
rm -f scores.res
python statistics.py 
rm -f *.log
cat scores.res
cd ../
