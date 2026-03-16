#!/usr/bin/env python3
"""
清理避難所資料 - 修復資料問題
"""

import pandas as pd
import numpy as np

def clean_shelter_data():
    """清理避難所資料"""
    print("🧹 清理避難所資料...")
    
    # 載入原始資料
    df = pd.read_csv('shelter_data.csv')
    print(f"📊 原始資料: {len(df)} 筆")
    
    # 1. 移除容量為 0 的記錄
    df_clean = df[df['capacity'] > 0].copy()
    print(f"📊 移除容量為0的記錄: {len(df) - len(df_clean)} 筆")
    
    # 2. 檢查座標範圍（台灣範圍：經度 119-122, 緯度 21-26）
    valid_coords = (
        (df_clean['longitude'].between(119, 122)) & 
        (df_clean['latitude'].between(21, 26))
    )
    df_clean = df_clean[valid_coords].copy()
    print(f"📊 移除座標異常的記錄: {len(df) - len(df_clean)} 筆")
    
    # 3. 移除重複記錄（基於座標）
    df_clean = df_clean.drop_duplicates(subset=['longitude', 'latitude'], keep='first')
    print(f"📊 移除重複座標記錄: {len(df) - len(df_clean)} 筆")
    
    # 4. 處理缺失值
    df_clean = df_clean.fillna({
        'name': 'Unknown',
        'address': 'Unknown',
        'county': 'Unknown',
        'district': 'Unknown',
        'village': 'Unknown',
        'disaster_types': 'Unknown',
        'manager': 'Unknown',
        'phone': 'Unknown'
    })
    
    # 5. 確保容量為整數
    df_clean['capacity'] = df_clean['capacity'].astype(int)
    
    # 6. 重新索引
    df_clean = df_clean.reset_index(drop=True)
    
    print(f"📊 清理後資料: {len(df_clean)} 筆")
    print(f"💰 總容量: {df_clean['capacity'].sum():,} 人")
    print(f"📍 座標範圍: 經度 {df_clean['longitude'].min():.3f}~{df_clean['longitude'].max():.3f}, 緯度 {df_clean['latitude'].min():.3f}~{df_clean['latitude'].max():.3f}")
    
    # 保存清理後的資料
    df_clean.to_csv('shelter_data_clean.csv', index=False, encoding='utf-8')
    print("✅ 清理後資料已保存: shelter_data_clean.csv")
    
    # 顯示清理統計
    print("\n📋 清理統計:")
    print(f"   原始記錄: {len(df)}")
    print(f"   清理後記錄: {len(df_clean)}")
    print(f"   移除記錄: {len(df) - len(df_clean)} ({(len(df) - len(df_clean))/len(df)*100:.1f}%)")
    
    return df_clean

if __name__ == "__main__":
    clean_data = clean_shelter_data()
