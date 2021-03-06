#!/usr/bin/python3
import re
import sys
import os
from shutil import copyfile


file= sys.argv[1]
outfile = file.rsplit(".")[0]+"_oneline.fa"
print(file,outfile)

# Open file. If line starts with > add 1o to contig count.
# Store other lines as seq data.
with open(file) as f:

    contigCount = 0
    totalLines = 0
    seq = []
    contig = []

    for line in f:
        totalLines += 1
        if line.startswith(">"):
            contigCount += 1
            contig.append(line)
        else:
            seq.append(line)

    f.close()

# Open the specifed output file.
# If the number of contigs == lines in file / 2 do nothing 
# else start splitting contigs to one line each. 
sys.stdout = open(outfile,"w")
if (int(contigCount) * 2) != int(totalLines):
    with open(file,"r") as f1:
        seq = f1.read()
        seq = re.split("^>",seq,flags=re.MULTILINE)
        del seq[0]
        f1.close()


    emptlist = []

    for i in seq:
        header, seq = i.split("\n", 1)
        header = ">"+header+"\n"
        seq = seq.replace("\n","") #+ "\n"
        print(header+seq)
else:
    copyfile(file, outfile)
    





