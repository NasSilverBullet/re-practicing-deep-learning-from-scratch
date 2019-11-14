import numpy as np

# 多次元配列
print('多次元配列')
A = np.array([1, 2, 3, 4])
print(A)  # [1 2 3 4]   <- 一次元配列
print(np.ndim(A))  # 1  <- 次元
print(A.shape)  # (4,)  <- タプルになっている
print(A.shape[0])  # 4

B = np.array([[1, 2], [3, 4], [5, 6]])
print(B)
"""
[[1 2]   二次元配列
 [3 4]
 [5 6]]
"""
print(np.ndim(B))  # 2  <- 次元
print(B.shape)  # (3, 2)

# 行列の積
print('行列の積')
A = np.array([[1, 2], [3, 4]])
print(A.shape)  # (3, 2)

B = np.array([[5, 6], [7, 8]])
print(B.shape)  # (2, 2)

print(np.dot(A, B))
"""
[[19 22]
 [43 50]]
"""

A = np.array([[1, 2], [3, 4], [5, 6]])
print(A.shape)  # (3, 2)


B = np.array([7, 8])
print(B.shape)  # (2,)

print(np.dot(A, B))  # [23 53 83]


# ニューラルネットワークの行列の積
print('ニューラルネットワークの行列の積')
X = np.array([1, 2])
print(X.shape)  # (2,)
W = np.array([[1, 3, 5], [2, 4, 6]])
print(W.shape)  # (2, 3)
Y = np.dot(X, W)
print(Y)  # [ 5 11 17 ]

# 3層ニューラルネットワークの実装
print('3層ニューラルネットワークの実装')
X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(W1.shape)  # (2, 3)
print(X.shape)  # (2,)
print(B1.shape)  # (3,)

A1 = np.dot(X, W1) + B1
print(A1)  # [0.3, 0.7 1.1]


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


Z1 = sigmoid(A1)  # 活性化関数
print(A1)  # [0.3, 0.7 1.1]
print(Z1)  # [0.57444252 0.66818777 0.75026011]


# 第2層
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

print(Z1.shape)  # (3,)
print(W2.shape)  # (3,2)
print(B2.shape)  # (2,)

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)


# 出力層
def identity_function(x):  # 恒等関数
    return x


W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

A3 = np.dot(Z2, W3) + B3
Y = identity_function(A3)

"""
出力層んひおける活性化関数
- 回帰問題では恒等関数
- 2クラス分類ではシグモイド関数
- 他クラス分類問題はソフトマックス関数
"""

# 実装のまとめ
print('実装のまとめ')


def init_network():
    network = {
            'W1': np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.5]]),
            'b1': np.array([0.1, 0.2, 0.3]),
            'W2': np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]]),
            'b2': np.array([0.1, 0.2]),
            'W3': np.array([[0.1, 0.3], [0.2, 0.4]]),
            'b3': np.array([0.1, 0.2]),
            }

    return network


def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)

    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)

    return y


network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)  # [0.31655918 0.69567667]
