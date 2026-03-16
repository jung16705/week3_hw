# 洪災避難所風險評估與收容量分析

## 專案概述

本專案利用水利署河川圖資建立多級警戒緩衝區，結合消防署避難收容所資料，評估各行政區的避難所洪災風險與收容量缺口。

### 分析特色

- **三級風險緩衝區**：500m / 1km / 2km
- **真實政府資料**：水利署河川圖 + 消防署避難所資料
- **決策導向分析**：評估收容量是否足夠

## 檔案結構

```
hw/
├── flood_risk_assessment.ipynb  # 主要分析筆記本
├── requirements.txt             # Python 套件需求
├── README.md                   # 說明文件
├── shelter_data.csv            # 避難所資料（需自行準備）
└── rivers_data.geojson         # 河川圖資（需自行準備）
```

## 環境設定

### 1. 安裝 Python 套件

```bash
pip install -r requirements.txt
```

### 2. 啟動 Jupyter Notebook

```bash
jupyter notebook
```

然後開啟 `flood_risk_assessment.ipynb`。

## 資料準備

### 避難所資料 (shelter_data.csv)

需要包含以下欄位：
- `name`: 避難所名稱
- `address`: 地址
- `capacity`: 收容量（人數）
- `longitude`: 經度
- `latitude`: 緯度

### 河川圖資 (rivers_data.geojson)

政府開放平台的水利署河川圖資，格式為 GeoJSON 或 Shapefile。

## 分析流程

### 1. 資料載入與預處理
- 載入避難所 CSV 資料
- 載入河川 GeoJSON 資料
- 座標系統轉換（WGS84 → TWD97）

### 2. 多級緩衝區建立
- 500m 高風險緩衝區
- 1000m 中風險緩衝區
- 2000m 低風險緩衝區

### 3. 風險評估
- 空間連接分析
- 避難所風險分級
- 收容量損失計算

### 4. 行政區分析
- 按行政區統計收容量
- 計算安全收容量
- 評估缺口比例

### 5. 視覺化與決策支援
- 風險分布圖表
- 空間地圖展示
- 政策建議生成

## 主要功能

### 風險分級系統
- **高風險**：距離河川 500m 內
- **中風險**：距離河川 500-1000m
- **低風險**：距離河川 1000-2000m

### 分析指標
- 各風險等級避難所數量
- 各風險等級收容量
- 行政區收容量缺口比例
- 高風險避難所清單

### 輸出成果
- CSV 格式的統計結果
- GeoJSON 格式的空間資料
- Markdown 格式的摘要報告
- 互動式查詢系統

## 使用範例

### 基本分析

```python
# 執行完整分析流程
# 請按照 Jupyter Notebook 中的 cell 順序執行
```

### 自訂緩衝區距離

```python
# 修改緩衝區距離
buffer_distances = [300, 800, 1500]  # 自訂距離（公尺）
buffer_zones = create_multi_level_buffers(rivers_projected, buffer_distances)
```

### 特定行政區查詢

```python
# 查詢特定行政區
district = "台北市大安區"
district_shelters = shelter_risk_assessment[
    shelter_risk_assessment['district'] == district
]
```

## 政策應用

### 即時決策支援
- 暴雨期間的避難所啟用決策
- 緊急疏散路線規劃
- 資源調度優先級排序

### 長期規劃
- 新設避難所地點選擇
- 現有避難所防護工程優先級
- 都市更新與防災規劃整合

## 技術規格

- **Python 版本**：3.8+
- **主要套件**：
  - pandas：資料處理
  - geopandas：地理空間分析
  - matplotlib/seaborn：資料視覺化
  - shapely：幾何計算

## 注意事項

1. **座標系統**：確保所有資料使用相同的座標系統
2. **資料品質**：檢查經緯度座標的準確性
3. **記憶體使用**：大型資料集可能需要較多記憶體
4. **執行時間**：空間分析可能需要較長計算時間

## 擴展建議

### 短期擴展
- 加入即時雨量資料
- 整合人口密度資訊
- 增加路網分析功能

### 長期擴展
- 機器學習風險預測
- 3D 地形分析
- 多災害綜合評估

## 授權

本專案僅供學術研究使用，請遵守相關資料的使用授權條款。

## 聯絡方式

如有問題或建議，請透過適當管道聯繫。

---

**更新日期**：2025-03-16
