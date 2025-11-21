
import matplotlib.pyplot as plt

import numpy

import pandas as pd

pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 500)

df = pd.read_csv("intermediate_mapk_dataset.csv")
#df_filtered = df[['PDB_pos','Wildtype','Mutation','DMS_score']]
#df_intermediate = df_filtered.groupby(['PDB_pos', 'Wildtype', 'Mutation'])

# Dictionary for changing the Mutation/Wildtype column
aa3_to_aa1 = {
    "ALA": "A",
    "ARG": "R",
    "ASN": "N",
    "ASP": "D",
    "CYS": "C",
    "GLN": "Q",
    "GLU": "E",
    "GLY": "G",
    "HIS": "H",
    "ILE": "I",
    "LEU": "L",
    "LYS": "K",
    "MET": "M",
    "PHE": "F",
    "PRO": "P",
    "SER": "S",
    "THR": "T",
    "TRP": "W",
    "TYR": "Y",
    "VAL": "V",
    # common special/ambiguous tokens you might see:
    "SEC": "U",  # selenocysteine
    "PYL": "O",  # pyrrolysine
    "ASX": "B",  # Asp or Asn
    "GLX": "Z",  # Glu or Gln
    "XAA": "X",  # unknown/any
    "UNK": "X",
    "TER": "*",  # stop
    "STOP": "*"
}
# Changing the Mutation and Wildtype columns from 3 letter to 1 letter amino acid codes
df['Wildtype'] = df['Wildtype'].map(aa3_to_aa1)
df['Mutation'] = df['Mutation'].map(aa3_to_aa1)

df['site'] = df['PDB_pos']
df['label_site'] = df['Wildtype']
df_renamed = df.rename(columns={"Wildtype":"wildtype", "Mutation":"mutation"})
df_renamed["condition"] = "DMS"
df_renamed["protein_site"] = df_renamed["site"]

df_renamed['site_mean'] = (
    df_renamed.groupby("PDB_pos")["DMS_score"].transform("mean")
)
df_renamed['mut_mean'] = (
    df_renamed.groupby("PDB_pos")["DMS_score"].transform("mean")
)

df_renamed.to_csv('dms_view.csv')

#df_heatmap = df_filtered.pivot(index="Wildtype", columns="PDB_pos", values="DMS_score")
#sns.heatmap(df_heatmap, square=True)