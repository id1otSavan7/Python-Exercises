class MathPower:
    def __init__(self, x = 0, max = 1):
        self.x = x 
        self.max = max

    def __iter__(self):
        self.n = 1
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result = self.x ** self.n
            self.n = self.n + 1
            return result
        else:
            raise StopIteration

"""
a = MathPower(3, 5)
i = iter(a)

while True:
    try:
        item = next(i)
        print(item)
    except StopIteration:
        break
        
"""
for item in MathPower(2,5):
    print(item)