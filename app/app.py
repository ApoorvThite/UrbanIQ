import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

from src.preprocess import apply_labels

# Simulate population data with lat/long for 3 tiles
data = {
    "region_id": ["img001.jpg", "img002.jpg", "img003.jpg"],
    "lat": [28.61, 28.62, 28.63],
    "lon": [77.21, 77.23, 77.25],
    "population_density": [6500, 2200, 800]
}
df = pd.DataFrame(data)
df = apply_labels(df)

priority_color = {"High": "red", "Medium": "orange", "Low": "green"}

m = folium.Map(location=[28.62, 77.23], zoom_start=12)
for _, row in df.iterrows():
    folium.CircleMarker(
        location=(row["lat"], row["lon"]),
        radius=8,
        color=priority_color[row["priority"]],
        popup=f"{row['region_id']} ({row['priority']})"
    ).add_to(m)

st.title("UrbanIQ – Development Priority Map")
folium_static(m)
