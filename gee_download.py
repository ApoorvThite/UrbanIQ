import ee
ee.Initialize(project='ecosplit')

# Define Delhi region
region = ee.Geometry.Rectangle([77.15, 28.55, 77.30, 28.75])

# Load Sentinel-2 Surface Reflectance and select RGB bands
image = (
    ee.ImageCollection("COPERNICUS/S2_SR")
    .filterBounds(region)
    .filterDate('2024-01-01', '2024-01-31')
    .sort('CLOUD_COVER')
    .first()
    .select(['B4', 'B3', 'B2'])  # Red, Green, Blue
)

task = ee.batch.Export.image.toDrive(
    image=image.clip(region),
    description='delhi_urbaniq_tile',
    folder='UrbanIQ',
    fileNamePrefix='delhi_tile_2024_01',
    scale=10,
    region=region.getInfo()['coordinates']
)

task.start()
print("Export started — check Earth Engine Tasks Dashboard.")
