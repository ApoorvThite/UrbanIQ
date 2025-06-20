import pandas as pd
import rasterio
from rasterio.sample import sample_gen
import os

# File paths
csv_path = "data/processed/tile_metadata.csv"
pop_tif_path = "data/population/delhi_pop_density.tif"
output_csv = "data/processed/labeled_metadata.csv"

# Load tile metadata
df = pd.read_csv(csv_path)

# Open population raster
with rasterio.open(pop_tif_path) as pop_src:
    coords = [(row['lon'], row['lat']) for _, row in df.iterrows()]
    pop_vals = list(pop_src.sample(coords))
    pop_vals = [float(val[0]) if val[0] != pop_src.nodata else 0 for val in pop_vals]

df["pop_density"] = pop_vals

# Label function
def get_label(density):
    if density > 5000:
        return "High"
    elif density > 2000:
        return "Medium"
    else:
        return "Low"

df["label"] = df["pop_density"].apply(get_label)

# Save
df.to_csv(output_csv, index=False)
print(f"✅ Saved labeled metadata to {output_csv}")