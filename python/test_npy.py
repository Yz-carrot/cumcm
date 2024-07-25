#用于读取并输出npy文件中的矩阵，用作验算

import numpy as np

flow_matrix = np.load(r'D:\NJU\Secondary\CUMCM\cumcm\Lucky\flow_matrix.npy')

# 将 .npy 文件内容转换回文本格式
converted_lines = []
num_nodes = 25
for i in range(num_nodes):
    for j in range(num_nodes):
        if i != j:
            converted_lines.append(f"{i+1} {j+1} {int(flow_matrix[i, j])} 0;\n")

print(converted_lines)