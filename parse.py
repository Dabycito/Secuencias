import csv
import pandas as pd

df = pd.read_csv("./F_results/helicase.csv")

print(df.columns[2])
print(df.iloc[0][0])
print(df.iloc[2][1])



'''print(df.iloc[2][1])
print(df.iloc[2][2])
print(df.iloc[3][1])
print(df.iloc[3][2])
print(df.iloc[3][3])

print("El largo de la tabla es de "+str(len(df.iloc[0])-1))
'''

        