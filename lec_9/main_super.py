
class GlobalParent:
    def __init__(self):
        print("GlobalParent init")

class Parent1(GlobalParent):
    def __init__(self, name="Parent1"):
        super().__init__()
        print("Parent1 init")
        self.name = name

    def speak(self):
        print("I am a parent 1")

class Parent2(GlobalParent):
    def __init__(self, age=0):
        super().__init__()
        print("Parent2 init")
        self.age = age

    def speak(self):
        print("I am a parent 2")

class Child(Parent1, Parent2):
    def __init__(self, name, age):
        # Parent1.__init__(self, name)
        # Parent2.__init__(self, age)
        super().__init__()

    def speak(self):
        Parent1.speak(self)
        Parent2.speak(self)
        print(self.age, "I am a child")


print(Child.mro())
c = Child("Alice", 10)
# c.speak()
# print(c.name)
# print(c.age)