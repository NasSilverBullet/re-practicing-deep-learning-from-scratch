import numpy as np
# 出力層の設計

"""
一般的に
    回帰問題           -> 恒等関数
    分類問題(数値予測) -> ソフトマックス関数
"""

# 恒等関数とソフトマックス関数
print('恒等関数とソフトマックス関数')


# ソフトマックス関数
def implement_softmax():
    a = np.array([0.3, 2.9, 4.0])

    exp_a = np.exp(a)  # 指数関数
    print(exp_a)  # [ 1.34985881 18.17414537 54.59815003]

    sum_exp_a = np.sum(exp_a)  # 指数関数の和
    print(sum_exp_a)  # 74.1221542101633

    y = exp_a / sum_exp_a
    print(y)  # [0.01821127 0.24519181 0.73659691]

    return y


implement_softmax()


#  ソフトマックス関数の実装上の注意
print('ソフトマックス関数の実装上の注意')


def softmax(a):
    exp_a = np.exp(a)
    # RuntimeWarning: invalid value encountered in true_d
    return exp_a / np.max(exp_a)


print(softmax(np.array([0.1, 0.2, 0.3])))  # こっちはできる
print(softmax(np.array([1010, 1000, 990])))  # こっちはできない [nan nan nan]


# p.69 ソフトマックス関数のリファクタリング
def softmax(a):
    c = np.max(a)
    # 指数関数 によって数が大きくなりすぎて、計算の上で
    # オーバーフローを起こしてしまう
    # そこで最大の数をそれぞれの値から引くことで
    # それぞれの値を小さく保ち、オーバーフローを防ぐ
    exp_a = np.exp(a - c)
    return exp_a / np.sum(exp_a)


print(softmax(np.array([1010, 1000, 990])))  # これもできるようになる


# ソフトマックス関数の特徴
print('ソフトマックス関数の特徴')


a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)  # [0.01821127 0.24519181 0.73659691]
print(np.sum(y))  # 1.0  合計が必ず1になる
# つまりソフトマックス関数は問題に対して確率的(統計的)対応ができる
# -> 回帰問題の出力層はソフトマックスとなる

# しかし、ソフトマックス関数を通す前と後では各要素の大小関係は変わらない
# -> 指数関数の単調増加によるもの
# -> 分類問題のときはソフトマックス関数を省略できる
# -> 出力層は恒等関数となる


# 出力層のニューロンの数

# クラス分類では出力層のニューロンの数は分類したいクラスの数に設定する
# ニューロンが一番高い値を出力した層がニューラルネットワークが
# 予測したクラスとなる
