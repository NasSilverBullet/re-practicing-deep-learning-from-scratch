# re-practicing-deep-learning-from-scratch

```python
# below is irrelevant with this repository
class FizzBuzz:
    def __init__(self, limit):
        self.limit = limit

    def __get(self, num):
        if num % 15 == 0:
            return "FizzBuzz"
        if num % 5 == 0:
            return "Buzz"
        if num % 3 == 0:
            return "Fizz"
        return num

    def run(self):
        for i in range(1, self.limit+1):
            print(self.__get(i))


fb = FizzBuzz(100)
fb.run()
```

Refs: <https://github.com/NasSilverBullet/Practicing-Deep-Learning-From-Scratch>
