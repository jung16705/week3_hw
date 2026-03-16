# 中文字體修復指南

## 問題描述
Jupyter Notebook 中的圖表顯示中文為亂碼（方塊或問號）。

## 解決方案

### 1. 自動修復（推薦）
我們已經更新了 `flood_risk_assessment.ipynb`，加入了自動字體檢測功能：

```python
# 重新執行第一個 cell 即可
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 系統會自動檢測可用的中文字體
# 並選擇最適合的字體進行設定
```

### 2. 手動安裝中文字體

#### macOS 使用者
```bash
# 安裝 Google Noto 字體（推薦）
brew install --cask font-noto-sans-cjk

# 或安裝其他中文字體
brew install --cask font-source-han-sans
brew install --cask font-wqy-zenhei
```

#### Windows 使用者
1. 下載並安裝 [Microsoft YaHei](https://docs.microsoft.com/zh-cn/typography/font-list/microsoft-yahei)
2. 或下載 [Noto Sans CJK](https://fonts.google.com/noto/specimen/Noto+Sans+CKJ)

#### Linux 使用者
```bash
# Ubuntu/Debian
sudo apt-get install fonts-noto-cjk

# CentOS/RHEL
sudo yum install google-noto-cjk-fonts
```

### 3. 驗證字體安裝

執行測試腳本：
```bash
python test_font.py
```

## 已修復的功能

### ✅ 自動字體檢測
- 系統會自動檢測可用的中文字體
- 按優先級選擇最適合的字體
- 如果沒有中文字體，會使用英文備用標籤

### ✅ 智能降級
- 中文字體失敗時自動切換英文標籤
- 確保圖表始終可讀
- 提供清晰的錯誤提示

### ✅ 支援的字體優先級
1. Noto Sans CJK TC（最佳）
2. PingFang TC（macOS）
3. Microsoft YaHei（Windows）
4. SimHei（Windows）
5. Arial Unicode MS（跨平台）
6. DejaVu Sans（備用）

## 使用說明

### 重新執行分析
1. 重新啟動 Jupyter Notebook
2. 重新執行第一個 cell（字體設定）
3. 確認看到 "✅ 使用中文字體：[字體名稱]" 訊息
4. 繼續執行後續分析

### 如果仍有問題
1. 確認已安裝上述字體
2. 重新啟動 Python 核心
3. 執行 `python test_font.py` 驗證
4. 檢查 `font_test.png` 輸出圖片

## 技術細節

### 字體檢測邏輯
```python
def setup_chinese_font():
    available_fonts = [f.name for f in fm.fontManager.ttflist]
    chinese_fonts = ['Noto Sans CJK TC', 'PingFang TC', ...]
    
    for font in chinese_fonts:
        if font in available_fonts:
            plt.rcParams['font.sans-serif'] = [font] + ...
            return font
```

### 備用機制
- 當中文字體不可用時
- 自動切換為英文標籤
- 避免完全無法顯示的問題

## 常見問題

### Q: 為什麼還是顯示方塊？
A: 可能原因：
1. 字體未正確安裝
2. 需要重新啟動 Jupyter
3. 字體快取需要清理

### Q: 可以強制使用特定字體嗎？
A: 可以在第一個 cell 中修改：
```python
plt.rcParams['font.sans-serif'] = ['你的字體名稱']
```

### Q: Linux 系統特別注意事項？
A: 某些 Linux 發行版需要：
```bash
fc-cache -fv  # 重建字體快取
```

---

**更新日期**：2025-03-16  
**狀態**：✅ 已修復
