import sys
import os
import pandas as pd
import numpy as np
import networkx as nx
import community as community_louvain

'''
#inputs
fasta_seqs = sys.argv[1]
path_output = sys.argv[2]

cores = 12#definir
#1. alinear multiple y obtener matriz de distancia, install clustal-omega
command = "clustalo -i {} -o {}result_alignment.aln --distmat-out={}distance_matrix.dist --full --force --threads 2".format(
    fasta_seqs,
    path_output,
    path_output,
    coress
)

os.system(command)
'''
#2. Parsear matriz de distancia
doc_open = open("./Seqs/100_200/tape_measure_protein/tape_measure_distance_matrix.dist", 'r')
number_seq = doc_open.readline()
number_seq = int(number_seq.replace("\n", ""))
print(number_seq)
line = doc_open.readline()
df_data = pd.DataFrame()
index_values = []

data_values_all = []

while line:
    distances = line.replace("\n", "").split(" ")
    seq_id = distances[0]
    distances = [float(value) for value in distances[1:] if len(value)>1]
    data_values_all +=distances
    #check if are there error in alignment
    if len(distances) != number_seq:
        length_value = len(distances)
        for i in range(length_value, number_seq):
            distances.append(1)
    df_data[seq_id] = distances
    index_values.append(seq_id)
    line = doc_open.readline()

doc_open.close()
df_data.index = index_values

print(df_data)
df_data.to_csv("./F_results/tape_measure_protein.csv")


'''
#3. filter and create graph
q1 = np.quantile(data_values_all, .25)

graph_data = nx.Graph()N
for node in index_values:
    graph_data.add_node(node)

for column in df_data.columns:
    for index in df_data.index:
        if column != index:
            if df_data[column][index] <= q1:
                graph_data.add_edge(column, index, weigth=df_data[column][index])

#4. apply louvain and get modularity
partition = community_louvain.best_partition(graph_data)
modularity_value = community_louvain.modularity(partition, graph_data)

#5. get groups
matrix_group = []
for element in partition:
    row = [element, partition[element]]
    matrix_group.append(row)

df_groups = pd.DataFrame(matrix_group, columns=['id_example', 'group'])
print(df_groups)
print(modularity_value)'''