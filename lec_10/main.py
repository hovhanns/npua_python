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

class Child(Parent1, Parent2):
    def __init__(self, name, age):
        Parent1.__init__(self, name)
        Parent2.__init__(self, age)
        #super(Parent3, self).__init__(age)


        #super(Parent1, self).__init__(name)
        #super(Parent2, self).__init__(age)
        
        #Parent2.__init__(self, age)
        #super(Parent1, self).__init__(age)
    def speak(self):
        Parent1.speak(self)
        Parent2.speak(self)
        print(self.age, "I am a child")


print(Child.mro())
c = Child("Alice", 10)
c.speak()
# print(c.name)
# print(c.age)
