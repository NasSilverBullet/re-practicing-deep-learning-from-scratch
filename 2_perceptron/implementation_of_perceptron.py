import numpy as np

# パーセプトロンの実装

# 簡単な実装


def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    return 1


print("AND")
print(AND(0, 0))  # 0
print(AND(1, 0))  # 0
print(AND(0, 1))  # 0
print(AND(1, 1))  # 1


# 重みとバイアスによると実装
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    if np.sum(w * x) + b <= 0:
        return 0
    return 1


print('AND version 2')
print(AND(0, 0))  # 0
print(AND(1, 0))  # 0
print(AND(0, 1))  # 0
print(AND(1, 1))  # 1


def NAND(x1, x2):  # 重みとバイアスが AND と逆転
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    if np.sum(w * x) + b <= 0:
        return 0
    return 1


print('NAND')
print(NAND(0, 0))  # 1
print(NAND(1, 0))  # 1
print(NAND(0, 1))  # 1
print(NAND(1, 1))  # 0


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = - 0.2
    if np.sum(w * x) + b <= 0:
        return 0
    return 1


print('OR')
print(OR(0, 0))  # 0
print(OR(0, 1))  # 1
print(OR(1, 0))  # 1
print(OR(1, 1))  # 1
