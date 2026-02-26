class MyIterator:
    def __init__(self):
        self.x = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.x < 3:
            self.x += 1
            return self.x
        else:
            raise StopIteration

for i in MyIterator():
    print(i)