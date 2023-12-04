class Parent1:
    def __init__(self, name="Parent1"):
        print("Parent1 init")
        self.name = name

    def speak(self):
        print("I am a parent 1")

class Parent2:
    def __init__(self, age=0):
        print("Parent2 init")
        self.age = age

    def speak(self):
        print("I am a parent 2")

class Child(Parent2, Parent1):
    def __init__(self, name, age, surname):
        Parent1.__init__(self, name)
        Parent2.__init__(self, age)
        self.surname = surname
    # def speak(self):
    #     # Parent1.speak(self)
    #     # Parent2.speak(self)
    #     print(self.age, "I am a child")


print(Child.mro())
c = Child("Alice", 10, "Smith")
c.speak()
print(str(c))