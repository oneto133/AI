import pandas as pd

df = pd.read_parquet("hf://datasets/emdemor/ptbr-perguntas-e-respostas-squad/base-train-dataset.parquet")


print(df.columns)