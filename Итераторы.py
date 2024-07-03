class EvenNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration


en = EvenNumbers(10, 25)
for i in en:
    if i % 2 == 0:
        print(i)