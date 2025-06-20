# UrbanIQ

UrbanIQ is a geospatial machine learning project that uses satellite imagery and population data to classify urban regions into high, medium, or low priority for development or green cover. It aims to empower urban planners, environmental NGOs, and local governments with data-driven insights for sustainable city development.

---

## 🚀 Features

- 🔭 **Satellite Image Classification** using CNNs (ResNet18/FastAI)
- 🧭 **Geospatial Data Integration** with OpenStreetMap and population density data
- 🌐 **Interactive Map Visualization** using Folium + GeoPandas
- 🧠 **Custom ML Pipeline** for training and deploying models
- 🤝 **Open Data Friendly** and easily extensible to other cities/regions

---

## 🧱 Tech Stack

- **Python 3.10+**
- **Google Earth Engine / OpenStreetMap APIs**
- **PyTorch / FastAI**
- **GeoPandas / Rasterio / Shapely**
- **Folium / Streamlit / Leaflet.js**
- **Jupyter for EDA and prototyping**

---

## 📁 Project Structure

UrbanIQ/
├── data/ # Raw and processed geospatial data
├── notebooks/ # Jupyter Notebooks for EDA & modeling
├── src/ # Training, preprocessing, prediction code
├── app/ # Streamlit dashboard & visualization
├── models/ # Trained CNN models (e.g., ResNet)
├── reports/ # Analysis reports and figures
├── tests/ # Unit tests
├── README.md # You're here!
├── requirements.txt # Required packages
└── setup.sh # Environment setup script

## 📊 Example Use Case

Given satellite imagery and population stats of an area like New Delhi or Nairobi, UrbanIQ can help:
- Identify underdeveloped high-density zones (for infrastructure planning)
- Detect green deserts (urban areas lacking greenery)
- Monitor urban sprawl over time

---

## ✅ How to Run

```bash
# Clone the repo
git clone https://github.com/your-username/UrbanIQ.git
cd UrbanIQ

# Setup environment
pip install -r requirements.txt

# Run Streamlit app
streamlit run app/app.py