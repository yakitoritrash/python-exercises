class Human:
    def __init__(self, name, age, pos):
        self.name = name
        self.age = age
        self.pos = pos
    def move(self):
        self.pos += 1
        print(self.pos)


lain = Human("lain", 19, 10);
print(lain.age)
