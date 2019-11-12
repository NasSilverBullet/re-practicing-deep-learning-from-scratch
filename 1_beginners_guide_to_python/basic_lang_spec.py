def chapter_1_3_1():
    print('-----算術計算-----')

    print(1 - 2)  # -1

    print(4 * 5)  # 20


def chapter_1_3_2():
    print('-----データ型-----')

    print(type(10))  # <class 'int'>

    print(type(2.718))  # <class 'float'>

    print(type('hello'))  # <class 'str'>


def chapter_1_3_3():
    print('-----変数-----')

    x = 10  # 初期化
    print(x)  # 10

    x = 100  # 代入
    print(x)  # 100

    y = 3.14
    print(x * y)  # 314.0

    print(type(x * y))  # <class 'float'>


def chapter_1_3_4():
    print('-----リスト-----')

    a = [1, 2, 3, 4, 5]

    print(a)  # [1, 2, 3, 4, 5]

    print(len(a))  # 5

    print(a[0])  # 1

    print(a[4])  # 5

    a[4] = 99
    print(a)  # 99


def chapter_1_3_5():
    print('-----ディクショナリ-----')

    me = {'height': 180}
    print(me['height'])  # 180

    me['weight'] = 70
    print(me)  # {'height': 180, 'weight': 70}


def chapter_1_3_6():
    print('-----ブーリアン-----')

    hungry = True
    sleepy = False

    print(type(hungry))  # <class 'bool'>

    print(not hungry)  # False

    print(hungry and sleepy)  # False

    print(hungry or sleepy)  # True


def chapter_1_3_7():
    print('-----if文-----')

    hungry = True
    if hungry:
        print('I'm hungry')  # <-

    hungry = False
    if hungry:
        print('I'm hungry')
    else:
        print('I'm not hungry')  # <-
        print('I'm sleepy')      # <-


def chapter_1_3_8():
    print('-----for文-----')

    for i in [1, 2, 3]:
        print(i)
        # 1
        # 2
        # 3


def chapter_1_3_9():
    print('-----関数-----')

    def hello():
        print('Hello World!')

    hello()  # Hello World!

    def hello(object):
        print('Hello ' + object + '!')

    hello('cat')  # Hello cat!


def chapter_1_4_2():
    print('----クラス-----')

    class Man:
        def __init__(self, name):
            self.name = name
            print('Initialized!')

        def hello(self):
            print('Hello ' + self.name + '!')

        def goodbye(self):
            print('Good bye ' + self.name + '!')

    m = Man('David')
    m.hello()  # Hello David!
    m.goodbye()  # Good bye David!


chapter_1_3_1()
chapter_1_3_2()
chapter_1_3_3()
chapter_1_3_4()
chapter_1_3_5()
chapter_1_3_6()
chapter_1_3_7()
chapter_1_3_8()
chapter_1_3_9()
chapter_1_4_2()
