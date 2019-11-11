import numpy as np
import matplotlib.pyplot as plt
# from を使うと imread をグローバルなメソッドのように使用できる
from matplotlib.image import imread


def chapter_1_6_1():
    print('単純なグラフの描画')

    x = np.arange(0, 5, 0.1)  # 0 から 6 まで 0.1 刻みで生成
    y = np.sin(x)

    # グラフの描画
    plt.plot(x, y)
    plt.show()


def chapter_1_6_2():
    print('pyplotの機能')

    x = np.arange(0, 6, 0.1)  # 0 から 6 まで 0.1 刻みで生成

    y1 = np.sin(x)
    y2 = np.cos(x)

    # グラフの描画
    plt.plot(x, y1, label="sin")  # キーワード引数は=の両脇にスペースをつけない
    plt.plot(x, y2, linestyle='--', label='cos')  # 破線で描画
    plt.xlabel('x')  # x 軸のラベル
    plt.ylabel('y')  # y 軸のラベル
    plt.title('sin & cos')  # タイトル
    plt.legend()  # 凡例を表示する
    plt.show()


def chapter_1_6_3():
    img = imread('deep-learning-from-scratch/dataset/lena.png')
    plt.imshow(img)
    plt.show()


chapter_1_6_1()
chapter_1_6_2()
chapter_1_6_3()
