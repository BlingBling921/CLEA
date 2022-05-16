test_pair = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
Lvec = np.array([e1 for e1, e2 in test_pair])  # 左边的测试实体组成的矩阵
Rvec = np.array([e2 for e1, e2 in test_pair])