class MyRange:
    def __init__(self, value, end):
        self.value = value
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1, 10)

for i in nums:
    print(i)