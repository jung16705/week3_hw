#!/usr/bin/env python3
"""
性能測試 - 檢查資料載入速度
"""

import pandas as pd
import geopandas as gpd
import time

def test_data_loading():
    """測試資料載入性能"""
    print("🚀 ARIA 資料載入性能測試")
    print("=" * 50)
    
    # 測試避難所資料載入
    print("\n📊 測試避難所資料載入...")
    start_time = time.time()
    
    shelter_df = pd.read_csv('shelter_data_clean.csv')
    shelter_time = time.time() - start_time
    
    print(f"   ✅ 載入完成: {shelter_time:.3f} 秒")
    print(f"   📊 資料量: {len(shelter_df):,} 筆")
    print(f"   💹 檔案大小: {shelter_df.memory_usage(deep=True).sum() / 1024:.1f} KB")
    
    # 測試河川資料載入
    print("\n🌊 測試河川資料載入...")
    start_time = time.time()
    
    rivers_gdf = gpd.read_file('rivers_data.geojson')
    rivers_time = time.time() - start_time
    
    print(f"   ✅ 載入完成: {rivers_time:.3f} 秒")
    print(f"   📊 資料量: {len(rivers_gdf):,} 筆")
    
    # 記憶體使用情況
    shelter_memory = shelter_df.memory_usage(deep=True).sum() / 1024 / 1024
    print(f"\n💾 記憶體使用:")
    print(f"   避難所資料: {shelter_memory:.2f} MB")
    print(f"   河川資料: 約 {rivers_gdf.memory_usage().sum() / 1024 / 1024:.1f} MB")
    
    # 總結
    total_time = shelter_time + rivers_time
    print(f"\n📈 性能總結:")
    print(f"   總載入時間: {total_time:.3f} 秒")
    print(f"   平均速度: {(len(shelter_df) + len(rivers_gdf)) / total_time:.0f} 筆/秒")
    
    # 性能評級
    if total_time < 1:
        print(f"   🚀 性能評級: 優秀 (< 1秒)")
    elif total_time < 3:
        print(f"   ✅ 性能評級: 良好 (< 3秒)")
    elif total_time < 5:
        print(f"   ⚠️  性能評級: 一般 (< 5秒)")
    else:
        print(f"   ❌ 性能評級: 需要優化 (> 5秒)")
    
    return shelter_time, rivers_time

def test_optimized_loading():
    """測試優化載入方法"""
    print("\n🔧 優化載入測試")
    print("=" * 50)
    
    # 只載入必要欄位
    start_time = time.time()
    shelter_df = pd.read_csv('shelter_data_clean.csv', 
                           usecols=['name', 'address', 'longitude', 'latitude', 'capacity', 'county', 'district'])
    optimized_time = time.time() - start_time
    
    print(f"📊 優化載入 (必要欄位): {optimized_time:.3f} 秒")
    print(f"   📊 資料量: {len(shelter_df):,} 筆")
    print(f"   💹 記憶體: {shelter_df.memory_usage(deep=True).sum() / 1024:.1f} KB")
    
    return optimized_time

if __name__ == "__main__":
    # 標準載入測試
    shelter_time, rivers_time = test_data_loading()
    
    # 優化載入測試
    optimized_time = test_optimized_loading()
    
    # 比較結果
    print(f"\n📊 性能比較:")
    print(f"   標準載入: {shelter_time:.3f} 秒")
    print(f"   優化載入: {optimized_time:.3f} 秒")
    print(f"   改善幅度: {((shelter_time - optimized_time) / shelter_time * 100):.1f}%")
    
    print(f"\n✅ 性能測試完成！")
