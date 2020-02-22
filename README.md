# Dastgah-Recognition-System

This software has been used for developing a Dastgah Recognition System. It uses Python as programming language but includes C++ libraries and functions. 
This repository has been created for allowing complete reproducibility of the results presented in the paper “Automatic Dastgah Recognition using Markov Models” submitted for the “14th International Symposium on Computer Music Multidisciplinary Research (CMMR)”. 

In this repository two archives are present: pdct_ir.tgz and markov.tgz they both has been tested ONLY on linux systems. 

pdct_ir.tgz contains the pitch detection, it generates .cvs scores of the .mp3 input audio files. 

Download the archive and extract the content in any location of your computer using this command:

$>  tar -xzvf pdct_ir.tgz 

you will find some .py files and a folder called “data”. 
In this folder you will put your audio files in mp3 format. In this archive, data folder contains a json file with the formal description of audio samples which have been used for the research presented in the paper “Automatic Dastgah Recognition using Markov Models” .

For running the analysis program you need to install a few component, instructions for doing this will be soon available here: 

… 



markov.tgz contains the Markov model implementation for the Dastgah recognition task. Download the archive and extract its content with the command:

$>   tar -xzvf markov.tgz

you will find .py programs and .sh linux scripts. In the next version (under preparation) of this package .sh scripts will be removed and all the functionalities will be included in python scripts. 
The “scores” folder contains the .csv scores textual files associated to the mp3 audio samples I used for my research, they can be freely shared so you can use those scores without needing the audio files. However you are free to use your audio files and apply this software for their classification. 

This package doesn't need so much additional libraries to be installed however a detailed “How to use” description is under preparation. In the meantime you can download the paper here: http://mtg.upf.edu/node/3975

… 

