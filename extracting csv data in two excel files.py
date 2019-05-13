import csv
import pandas as pd

with open('in.csv') as f:
    reader=csv.reader(f)
    count=0
    to_move=[]
    for row in reader:
        to_move.append(row)
transfer1 = to_move[0:100]
transfer2 = to_move[100:200]

pd.DataFrame(transfer1).to_excel('out1.xlsx',header=False,index=False)
pd.DataFrame(transfer2).to_excel('out2.xlsx',header=False,index=False)
