class Square:
    square_list = []

    def __init__(self, size):
        self.size = size
        self.square_list.append(self)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.size, self.size, self.size, self.size)

s1 = Square(10)
s2 = Square(20)

print(s1)
print(s2)
print(s1.square_list)

same_s1 = s1

for s in s1.square_list:
    print("---")
    print(s is same_s1)

