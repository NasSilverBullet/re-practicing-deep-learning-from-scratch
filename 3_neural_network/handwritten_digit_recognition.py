# 手書き数字認識
import sys
import os
import numpy as np
from PIL import Image
sys.path.append(os.curdir + '/deep-learning-from-scratch')
from dataset.mnist import load_mnist

# 手書き数字認識
print('手書き数字認識')

# MNIST データセット
print('MNIST データセット')


(x_train, t_train), (x_test, t_test) = \
        load_mnist(flatten=True, normalize=False)

print(x_train.shape)  # (60000, 784)  -> 訓練画像
print(t_train.shape)  # (60000,)  -> 訓練ラベル
print(x_test.shape)  # (10000, 784)  -> テスト画像
print(t_test.shape)  # (10000,)  -> テストラベル


def img_swhow(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


# MNIST の画像表示
print('MNIST の画像表示')
img = x_train[0]
label = t_train[0]
print(label)  # 5
print(img.shape)  # (784,)
img = img.reshape(28, 28)
print(img.shape)  # (28, 28)
img_swhow(img)
print(os.path.abspath(''))
