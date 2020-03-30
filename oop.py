# Singleton
class Singleton(object):
    _single = {}
    def __new__(self):
        if not self._single:
            self._single[self] = super(Singleton, self).__new__(self)
        return self._single[self]

class Counter():
    # переменная класса
    cnt = 0
    def __init__(self):
        # переменная объекта
        self.ID = Counter.cnt
        Counter.cnt += 1

# s = Singleton()
# s2 = Singleton()
# c1 = Counter()
# c2 = Counter()
# c3 = Counter()


mas = [0,1,2,3,4,5,2,5]
i = 0
while i < len(mas)-1:
    if mas[i] in mas[i+1:]:
        mas.pop(i)
    else:
        i +=1

print(mas)
