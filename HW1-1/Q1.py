import pandas as pd
import numpy as np

from Bio import SeqIO

txtfile= open("matrix.txt","r")

M1=txtfile.readline()
M2=txtfile.readline()
M3=txtfile.readline()
M4=txtfile.readline()



record = list(SeqIO.parse("Q1.fasta", "fasta"))
seq1_20 = record[0].seq
seq2_20 = record[1].seq
seq3_20 = record[2].seq
seq1_100 = record[3].seq
seq2_100 = record[4].seq
