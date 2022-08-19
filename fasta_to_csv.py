from Bio import SeqIO
import pandas as pd

meta = []
sequence = []
seq = ("./Seqs/700_1200/xylulose_kinase/xylulose_kinase.fasta")

for seq_record in SeqIO.parse(seq,"fasta"):
    meta.append(str(seq_record.id))
    sequence.append(str(seq_record.seq))

df = pd.DataFrame(data={"Meta": meta, "SequenceID": sequence})
print(df)

df.to_csv("./Clusters_in_csv/xylulose_kinase.csv")