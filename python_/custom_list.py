class CustomList(list):

    def __init__(self):
        pass

    def get(self):
        pass

    def __sub__(self, array):
        for val in array:
            if val in self:
                self.remove(val)
        return self
    
    # def append(self, val):
    #     if val not in self:
    #         super().append(val)

c = CustomList()
c1 = CustomList()
c2 = CustomList()
c.append(2)
c.append(3)
c1.append(3)
c2.append(4)

print("outside", c)
print("outside", c1)

r = c - c2
print(r)

