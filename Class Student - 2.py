class student:
    grade = 3
    name = "Uzayr"

    def introduction(self):
        print("Hi, I'm a student")

    def details(self):
        print("My name is ", self.name)
        print("I'm in grade ", self.grade)

ob = student()
ob.details()
ob.introduction()