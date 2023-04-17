# we can inherit attributes, or behaviours (functions)
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale")


class Fish(Animal):
    
    def __init__(self):
        super().__init__() # this line is not required though recommended
        self.num_eyes = 5

    def breathe(self):
        super().breathe()
        print("doing this under water")


    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.breathe()
nemo.swim()

print(nemo.num_eyes)

