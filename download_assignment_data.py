#!/usr/bin/env python3
"""
下載作業要求的資料 - Week 3 Assignment
"""

import os
import requests
import pandas as pd
import geopandas as gpd
from urllib.parse import quote
import zipfile
import io

def download_shelter_data():
    """下載消防署避難所資料"""
    print("🔄 下載消防署避難所資料...")
    
    # 政府開放平台 URL
    shelter_url = "https://data.gov.tw/dataset/73242"
    
    print(f"📋 資料來源: {shelter_url}")
    print("⚠️ 請手動下載避難收容處所.csv 檔案")
    print("📝 步驟:")
    print("   1. 訪問: https://data.gov.tw/dataset/73242")
    print("   2. 下載 '避難收容處所.csv'")
    print("   3. 將檔案放在同一目錄")
    
    return False

def download_river_data():
    """下載水利署河川資料"""
    print("🔄 下載水利署河川資料...")
    
    # 水利署 URL
    river_url = "https://gic.wra.gov.tw/Gis/gic/API/Google/DownLoad.aspx?fname=RIVERPOLY&filetype=SHP"
    
    try:
        print("📥 從水利署載入河川資料...")
        rivers_gdf = gpd.read_file(river_url)
        
        # 保存為本地檔案
        rivers_gdf.to_file('rivers_data_from_wra.geojson', driver='GeoJSON')
        
        print(f"✅ 河川資料下載成功: {len(rivers_gdf):,} 筆")
        print(f"📐 坐標系統: {rivers_gdf.crs}")
        print(f"💾 已保存: rivers_data_from_wra.geojson")
        
        return True
        
    except Exception as e:
        print(f"❌ 下載失敗: {e}")
        print("⚠️ 請手動下載或使用網路下載")
        return False

def download_township_data():
    """下載鄉鎮界線資料"""
    print("🔄 下載鄉鎮界線資料...")
    
    # 國土測繪中心 URL
    township_url = 'https://www.tgos.tw/tgos/VirtualDir/Product/3fe61d4a-ca23-4f45-8aca-4a536f40f290/' + quote('鄉(鎮、市、區)界線1140318.zip')
    
    try:
        print("📥 從國土測繪中心載入鄉鎮界線...")
        
        # 下載 ZIP 檔案
        response = requests.get(township_url)
        response.raise_for_status()
        
        # 解壓縮
        zip_file = zipfile.ZipFile(io.BytesIO(response.content))
        
        # 尋找 SHP 檔案
        shp_files = [f for f in zip_file.namelist() if f.endswith('.shp')]
        
        if shp_files:
            # 讀取第一個 SHP 檔案
            with zip_file.open(shp_files[0]) as f:
                townships_gdf = gpd.read_file(f)
            
            # 保存為本地檔案
            townships_gdf.to_file('townships_data_from_tgos.geojson', driver='GeoJSON')
            
            print(f"✅ 鄉鎮界線下載成功: {len(townships_gdf):,} 個行政區")
            print(f"📐 坐標系統: {townships_gdf.crs}")
            print(f"💾 已保存: townships_data_from_tgos.geojson")
            
            return True
        else:
            print("❌ ZIP 檔案中找不到 SHP 檔案")
            return False
            
    except Exception as e:
        print(f"❌ 下載失敗: {e}")
        print("⚠️ 請手動下載或使用網路下載")
        return False

def check_data_files():
    """檢查資料檔案是否存在"""
    print("🔍 檢查資料檔案...")
    
    files_to_check = [
        ('避難收容處所.csv', '消防署避難所資料'),
        ('rivers_data_from_wra.geojson', '水利署河川資料'),
        ('townships_data_from_tgos.geojson', '鄉鎮界線資料')
    ]
    
    missing_files = []
    
    for filename, description in files_to_check:
        if os.path.exists(filename):
            print(f"✅ {description}: {filename}")
        else:
            print(f"❌ {description}: {filename} (缺失)")
            missing_files.append((filename, description))
    
    return missing_files

def main():
    """主程式"""
    print("🚀 Week 3 Assignment 資料下載工具")
    print("=" * 50)
    
    # 檢查現有檔案
    missing_files = check_data_files()
    
    if not missing_files:
        print("\n✅ 所有資料檔案都已存在！")
        return
    
    print(f"\n⚠️ 缺失 {len(missing_files)} 個檔案")
    
    # 嘗試自動下載
    print("\n🔄 嘗試自動下載...")
    
    # 下載河川資料
    if any('河川' in desc for _, desc in missing_files):
        download_river_data()
    
    # 下載鄉鎮界線
    if any('鄉鎮' in desc for _, desc in missing_files):
        download_township_data()
    
    # 避難所資料需要手動下載
    if any('避難所' in desc for _, desc in missing_files):
        download_shelter_data()
    
    # 最後檢查
    print("\n🔍 最終檢查...")
    remaining_missing = check_data_files()
    
    if remaining_missing:
        print(f"\n⚠️ 還有 {len(remaining_missing)} 個檔案需要手動下載:")
        for filename, description in remaining_missing:
            print(f"   - {description}: {filename}")
    else:
        print("\n✅ 所有資料檔案都已準備就緒！")

if __name__ == "__main__":
    main()
