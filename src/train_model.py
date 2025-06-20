from fastai.vision.all import *
import pandas as pd
from pathlib import Path

data_path = Path("data/processed")
df = pd.read_csv(data_path / "labeled_metadata.csv")
df['tile_path'] = df['tile_name'].apply(lambda x: str(data_path / x))

# Manual split
df['is_valid'] = df.index % 5 == 0

# Print debug info
print("✅ CSV size:", len(df))
print("✅ Class counts:")
print(df['label'].value_counts())
print("✅ Files that exist:")
print(df['tile_path'].apply(lambda x: Path(x).exists()).value_counts())

# DataBlock
dblock = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_x=ColReader('tile_path'),
    get_y=ColReader('label'),
    splitter=ColSplitter('is_valid'),
    item_tfms=Resize(256),
    batch_tfms=aug_transforms()
)

# DataLoaders
dls = dblock.dataloaders(df, bs=2, num_workers=0)  # num_workers=0 fixes MacOS bugs

# Show batch
dls.show_batch(max_n=6)

# Train
learn = vision_learner(dls, resnet18, metrics=accuracy)
learn.fine_tune(5)

# Save
learn.export("models/urbaniq_resnet18.pkl")
print("✅ Model trained and saved!")
