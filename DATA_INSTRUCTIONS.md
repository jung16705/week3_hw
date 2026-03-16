# Data Files Required for ARIA.ipynb

## Required Data Files

The `ARIA.ipynb` notebook requires the following data files to run:

### 1. shelter_data.csv
- **Source**: Fire Department shelter data from data.gov.tw
- **Size**: 161,728 bytes
- **Content**: 967 emergency shelters with coordinates and capacity
- **Required for**: All analysis cells

### 2. rivers_data.geojson  
- **Source**: Water Resources Agency river data
- **Size**: 76,794,120 bytes (~77MB)
- **Content**: 13,262 river segments for buffer analysis
- **Required for**: Buffer zone creation and risk assessment

## How to Obtain Data

### Option 1: Use Provided Files
The data files are included in this repository for convenience.

### Option 2: Download Original Data
```python
# Download shelter data from data.gov.tw
import pandas as pd
shelter_df = pd.read_csv('https://data.gov.tw/dataset/73242')

# Download river data from Water Resources Agency
import geopandas as gpd
rivers = gpd.read_file('https://gic.wra.gov.tw/Gis/gic/API/Google/DownLoad.aspx?fname=RIVERPOLY&filetype=SHP')
```

## File Locations
- Place `shelter_data.csv` in the same directory as `ARIA.ipynb`
- Place `rivers_data.geojson` in the same directory as `ARIA.ipynb`

## Note
These data files are large (especially the river data) and are not included in the official assignment submission to keep the repository size manageable. However, they are provided here for complete functionality.

## Assignment Submission
The official assignment submission includes only the 4 required deliverables:
1. ARIA.ipynb
2. shelter_risk_audit.json  
3. risk_map.png
4. README.md

The data files are supporting files for running the analysis.
