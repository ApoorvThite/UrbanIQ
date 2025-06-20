from pathlib import Path
import pandas as pd

df = pd.read_csv("data/processed/labeled_metadata.csv")
df['tile_path'] = df['tile_name'].apply(lambda x: f"data/processed/{x}")
print(df['tile_path'].apply(lambda x: Path(x).exists()).value_counts())


import pandas as pd

df = pd.read_csv("data/processed/labeled_metadata.csv")
print("✅ Label distribution:")
print(df["label"].value_counts())