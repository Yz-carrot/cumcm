#用于把数据转为矩阵，保存在npy文件中

import numpy as np

# 读取文件内容
file_path = r"D:\NJU\Secondary\CUMCM\cumcm\Lucky\data1.txt"
with open(file_path, 'r') as file:
    lines = file.readlines()

# 初始化业务流量和距离的矩阵
num_nodes = 25
flow_matrix = np.zeros((num_nodes, num_nodes))
distance_matrix = np.zeros((num_nodes, num_nodes))

# 解析文件内容
for line in lines:
    data = line.split()
    if len(data) < 4:
        continue  # 跳过格式不正确的行
    node1 = int(data[0]) - 1
    node2 = int(data[1]) - 1
    try:
        flow = float(data[2].replace(';', ''))  # 去除多余的字符
        distance = float(data[3].replace(';', ''))  # 去除多余的字符
    except ValueError:
        continue  # 跳过无法转换的行
    flow_matrix[node1, node2] = flow
    distance_matrix[node1, node2] = distance

# 保存矩阵为 .npy 文件
flow_matrix_path = r"D:\NJU\Secondary\CUMCM\cumcm\Lucky\flow_matrix.npy"
distance_matrix_path = r"D:\NJU\Secondary\CUMCM\cumcm\Lucky\distance_matrix.npy"
np.save(flow_matrix_path, flow_matrix)
np.save(distance_matrix_path, distance_matrix)
