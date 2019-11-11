import numpy as np


def chapter_1_5_2():
    print('NumPy配列の生成')

    x = np.array([1.0, 2.0, 3.0])
    print(x)  # [1.0 2.0 3.0]

    print(type(x))  # <class 'numpy.ndarray'>


def chapter_1_5_3():
    print('NumPyの算術計算')

    x = np.array([1.0, 2.0, 3.0])
    y = np.array([2.0, 4.0, 6.0])

    print(x + y)  # [3. 6. 9.]

    print(x - y)  # [-1. -2. -3.]

    print(x * y)  # [ 2.  8. 18.]

    print(x / y)  # [0.5 0.5 0.5]

    # 各要素とスカラ値の計算
    # 各要素の数に合わせて展開してくれる -> ブロードキャスト
    x = np.array([1.0, 2.0, 3.0])
    print(x / 2.0)  # [0.5 1.  1.5]


def chapter_1_5_4():
    print('NumPyのN次元配列')
    A = np.array([[1, 2], [3, 4]])
    print(A)
    '''
    [[1 2]
     [3 4]]
    '''

    print(A.shape)  # (2, 2)

    print(A.dtype)  # int64

    B = np.array([[3, 0], [0, 6]])

    print(A + B)
    '''
    [[ 4  2]
     [ 3 10]]
    '''

    print(A * B)
    '''
    [[ 3  0]
     [ 0 24]]
    '''

    # 行列にもブロードキャストが可能
    print(A * 10)
    '''
    [[10 20]
     [30 40]]
    '''


def chapter_1_5_5():
    print('ブロードキャスト')

    A = np.array([[1, 2], [3, 4]])
    B = np.array([10, 20])

    print(A * B)  # ブロードキャストでBが[[10, 20], [10, 20]] に展開される
    '''
    [[10 40]
     [30 80]]
    '''


def chapter_1_5_6():
    print('要素へのアクセス')

    X = np.array([[51, 55], [14, 19], [0, 4]])
    print(X)
    '''
    [[51 55]
     [14 19]
     [ 0  4]]
    '''

    print(X[0])  # [51 55]

    print(X[0][1])  # 55

    for row in X:
        print(row)
        '''
        [51 55]
        [14 19]
        [0 4]
        '''

        X = X.flatten()
        print(X)  # [51 55 14 19  0  4]

        print(X[np.array([0, 2, 4])])  # [51 14  0]

        print(X > 15)  # [ True  True False  True False False]

        print(X[X > 15])  # [51 55 19]


chapter_1_5_2()
chapter_1_5_3()
chapter_1_5_4()
chapter_1_5_5()
chapter_1_5_6()
