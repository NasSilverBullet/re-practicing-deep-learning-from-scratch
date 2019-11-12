import numpy as np
import matplotlib.pylab as plt


#  ステップ関数の実装
def step_function(x):  # スカラ値しか受けとらない
    if x > 0:
        return 1
    return 0


print("ステップ関数の実装")
print(step_function(0.5))  # 1


# python は同一名メソッドを同一ライブラリ内で宣言できる
# オーバーライドする形になる
def step_function(x):  # numpy配列を引数に取る
    y = x > 0
    return y.astype(np.int)  # boolean を int に変換


print(step_function(np.array([-1.0, 1.0, 2.0])))


#  ステップ関数のグラフ
def step_function(x):  # 一行で書ける
    return np.array(x > 0, dtype=np.int)


print('ステップ関数のグラフ')
x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()


#  シグモイド関数の実装
def sigmoid(x):
    return 1/(1 + np.exp(-x))  # ブロードキャストが行われている


print('シグモイド関数の実装')
x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)  # y 軸の範囲を指定
plt.show()


#  ReLU関数
def relu(x):
    return np.maximum(0, x)  # 0 をブロードキャストし、比較している


print('ReLU関数')
x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)  # y 軸の範囲を指定
plt.show()
