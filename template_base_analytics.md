# 基礎分析のテンプレート
## List
各変数列ごとに、list型のliとして渡す
```
import statistics as st
import matplotlib.pyplot as plt

# 要約統計量を算出
if None in li:
    print("欠損値数:" + str(li.count(None)))
else:
    print("欠損値　:なし")
    print("平均値　:{0:.3f}".format(st.mean(li)))
    print("中央値　:{0:.3f}".format(st.median(li)))
    print("最大値　:{0:.3f}".format(max(li)))
    print("最小値　:{0:.3f}".format(min(li)))
    print("分散　　:{0:.3f}".format(st.pvariance(li)))
    print("標準偏差:{0:.3f}".format(st.pstdev(li)))
    
try:
    print("最頻値　:{0:.3f}".format(st.mode(li)))
except st.StatisticsError as e:
    print("最頻値　:なし(複数個あります)")

# ヒストグラムで可視化して、分布の偏りや外れ値を見つける
plt.hist(li, bins=10)
plt.show()
```

## 
## DataFrame
