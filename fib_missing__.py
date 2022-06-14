class Fib(dict):
    def __init__(self):
        self[0] = self[1] = 1

    def __missing__(self, k):
        fibk = self[k] = self[k-1] + self[k-2]
        return fibk


fibd = Fib()
print(fibd[10])
