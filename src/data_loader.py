import os
import pandas as pd
from glob import glob
from PIL import Image

def load_image_tiles(image_dir, extension="jpg"):
    image_paths = glob(os.path.join(image_dir, f"*.{extension}"))
    images = [(os.path.basename(p), Image.open(p)) for p in image_paths]
    return images

def load_population_data(csv_path):
    return pd.read_csv(csv_path)