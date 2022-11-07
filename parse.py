import csv
import pandas as pd

df = pd.read_csv("./F_results/helicase.csv")

Tabla = ["Secuencia1","Secuencia2","Distancia"]

#Largo de la tabla ser como len(df.iloc[0])-1

TableLen = len(df.iloc[0])-1
print(TableLen)
AuxMax = 3

for i in range(1,TableLen):
    for j in range(2,AuxMax):
        Tabla.append(str(df.columns[j]))
        print(df.columns[j])
        Tabla.append(str(df.iloc[i][0]))
        print(df.iloc[i][0])
        Tabla.append(str(df.iloc[i][j-1]))
        print(df.iloc[i][j-1])
    AuxMax=AuxMax+1
    
print(Tabla)



'''print(df.columns[2]) #De 2 hasta MaxColumnas
print(df.iloc[1][0])
print(df.iloc[1][1])

print(df.columns[2])
print(df.iloc[2][0])
print(df.iloc[2][1])

print(df.columns[3])
print(df.iloc[2][0])
print(df.iloc[2][2])

print(df.columns[2])
print(df.iloc[3][0])
print(df.iloc[3][1])

print(df.columns[3])
print(df.iloc[3][0])
print(df.iloc[3][2])

print(df.columns[4])
print(df.iloc[3][0])
print(df.iloc[3][3])

'''

'''print(df.iloc[2][1])
print(df.iloc[2][2])
print(df.iloc[3][1])
print(df.iloc[3][2])
print(df.iloc[3][3])
'''
print("El largo de la tabla es de "+str(len(df.iloc[0])-1))


        