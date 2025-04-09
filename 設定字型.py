import matplotlib.pyplot as plt
from matplotlib import font_manager

# 設定字型 (請確認字型檔案位置)
font_path = "C:/Windows/Fonts/msjh.ttc"  # 微軟正黑體

# 使用字型管理器 (font_manager) 加載指定的字型檔案
font_prop = font_manager.FontProperties(fname=font_path)

# 設定 Matplotlib 的全域字型為指定的字型
# plt.rcParams 是 Matplotlib 的全域設定字典，'font.family' 用於設定字型
plt.rcParams['font.family'] = font_prop.get_name()
