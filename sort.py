import csv
import pandas as pd
df = pd.read_csv("dwarf_star.csv")

df = df[df['Star_name'].notna()]
df = df[df['Distance'].notna()]
df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]

df["Radius"] = 0.102763*df["Radius"]

df['Mass'] = df['Mass'].astype(float)
df["Mass"] = 0.000954588*df["Mass"]

df.to_csv("sort.csv")