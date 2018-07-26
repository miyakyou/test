import statistics

data = [8,17,11,6,21,7,8,9,0,5,22,14,36,2,5,0,3,0]

print("平均値：", statistics.mean(data))
print("中央値：", statistics.median(data))
print("最頻値：", statistics.mode(data))
print("分散値：", statistics.pvariance(data))
print("標準偏差：", statistics.pstdev(data))