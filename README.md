
# YuD

Python program to extract upstream and downstream regions in provided range of KBs, from the gtf file, for the given sequence Ids/related-information as specified in a csv file.


## Usage


For extracting upstream and downstream regions you need to clone or download this repository
```bash
git clone https://github.com/ChopraKritika/YuD.git
```

Then run the following command
```bash
pip install -r requirements.txt
```

Copy the code from link
```bash
https://gist.github.com/slowkow/8101481
```
Paste in a file and name it as GTF.py

You can access YuD.py file with code editors/IDE/CMD/Power-shell/bash etc.

For WINDOWS 

open Yud.exe, from extracted folder start Yud.exe


## Prerequisites

Two files are needed for successful extraction of upstream and downstream locations 

FIRST: .gtf file, containing information of all sequences 

SECOND: .csv file containing sequence ids or related information unique to each sequence, for which upstream and downstream regions are being searched 

Note: .cvs file should contain ids/other-information in 1st row, followed by start and end sites in 2nd and 3rd row respectively. Also, this file must contain headers. 

You can refer to sampleGTF.GTF and sampleCSV.csv files in folder Sample files.


## Functioning

Specify the file names for input (in any case-lowercase or uppercase), if not in same folder, provide path to file along with file name.
Mention KBs as integers. For instance, you want to look for 10 KBs, then you must enter 10 only. Sit back and relax.
2 files named upstream.csv and downstream.csv will be created.
