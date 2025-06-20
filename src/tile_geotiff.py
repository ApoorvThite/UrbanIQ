import rasterio
from rasterio.windows import Window
from rasterio.transform import xy
from pathlib import Path
import numpy as np
from PIL import Image
import csv
import os
from pyproj import Transformer

# Parameters
tile_size = 128
input_path = "data/raw/delhi_tile_2024_01.tif"
output_dir = Path("data/processed/")
output_dir.mkdir(parents=True, exist_ok=True)
csv_path = output_dir / "tile_metadata.csv"

def tile_image():
    with rasterio.open(input_path) as src:
        width = src.width
        height = src.height
        transform = src.transform
        bands = src.count

        tile_id = 0
        with open(csv_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["tile_name", "lat", "lon"])

            for y in range(0, height, tile_size):
                for x in range(0, width, tile_size):
                    if x + tile_size > width or y + tile_size > height:
                        continue  # skip incomplete edge tiles

                    window = Window(x, y, tile_size, tile_size)
                    data = src.read(window=window)

                    # Convert (3, H, W) to (H, W, 3)
                    img = np.transpose(data, (1, 2, 0))
                    img = ((img - img.min()) / (img.max() - img.min()) * 255).astype(np.uint8)
                    tile_img = Image.fromarray(img)

                    tile_name = f"tile_{tile_id:04}.jpg"
                    tile_path = output_dir / tile_name
                    tile_img.save(tile_path)

                    # Get center coordinates
                    center_x = x + tile_size // 2
                    center_y = y + tile_size // 2
                    transformer = Transformer.from_crs(src.crs, "EPSG:4326", always_xy=True)
                    center_x_map, center_y_map = xy(transform, center_y, center_x)
                    lon, lat = transformer.transform(center_x_map, center_y_map)

                    writer.writerow([tile_name, lat, lon])
                    tile_id += 1

    print(f"✅ Created {tile_id} tiles and saved to {output_dir}")
    print(f"🗺️ Metadata saved to {csv_path}")

if __name__ == "__main__":
    tile_image()