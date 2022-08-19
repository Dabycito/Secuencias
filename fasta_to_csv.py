from Bio import SeqIO
import pandas as pd

meta = []
sequence = []
seq = ("./Seqs/PDB/enzyme_all_beta_proteins/enzyme_all_beta_proteins2.fasta")

for seq_record in SeqIO.parse(seq,"fasta"):
    meta.append(str(seq_record.id))
    sequence.append(str(seq_record.seq))

df = pd.DataFrame(data={"Meta": meta, "SequenceID": sequence})
print(df)

df.to_csv("./Clusters_in_csv/enzyme_all_beta_proteins.csv")