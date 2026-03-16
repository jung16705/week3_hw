#!/usr/bin/env python3
"""
創建河川資料樣本 - 解決載入過慢問題
"""

import geopandas as gpd
import pandas as pd

def create_river_sample():
    """創建河川資料樣本"""
    print("🔄 創建河川資料樣本...")
    
    # 載入原始河川資料
    print("📊 載入原始河川資料...")
    rivers_gdf = gpd.read_file('rivers_data.geojson')
    print(f"   原始資料: {len(rivers_gdf):,} 筆")
    
    # 隨機取樣 1000 筆資料
    sample_size = min(1000, len(rivers_gdf))
    rivers_sample = rivers_gdf.sample(n=sample_size, random_state=42)
    
    # 確保包含主要河流
    major_rivers = ['濁水溪', '高屏溪', '淡水河', '蘭陽溪', '秀姑巒溪']
    major_river_data = rivers_gdf[rivers_gdf['RIVER_NAME'].isin(major_rivers)]
    
    # 合併樣本和主要河流
    rivers_final = pd.concat([rivers_sample, major_river_data]).drop_duplicates()
    
    print(f"   樣本資料: {len(rivers_final):,} 筆")
    print(f"   主要河流: {len(major_river_data)} 筆")
    print(f"   檔案大小: 預計 < 5MB")
    
    # 保存樣本
    rivers_final.to_file('rivers_data_sample.geojson', driver='GeoJSON')
    print("✅ 河川樣本已保存: rivers_data_sample.geojson")
    
    return rivers_final

if __name__ == "__main__":
    create_river_sample()
