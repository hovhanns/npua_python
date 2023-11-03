
class Student:
    count = 0
    def __init__(self, name, surname="", mog=0):
        self.name = name
        self.surname = surname
        self.mog = mog
        self.__deases = "some deases"
        Student.count+=1
    
    def __str__(self):
        return f"{self.name} {self.surname}"
    
    def say_hello(self):
        print("Hello, my name is", self.name)

    def say_problem(self):
        print(self.__deases)
    def __repr__(self):
        print("Repr called")
        return "" 

    def __private_func(self):
        print("called private")


    @staticmethod
    def say_class_name():
        print("This is a Student class")


s1 = Student("Samvel", "Hakobyan")
print(s1.name)
print(s1)
s1.say_problem()


print(s1.__dir__())

