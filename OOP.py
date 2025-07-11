class Employee:
    #init är en special method som man skriver när man skapar en klass
    def __init__(self, firstname, lastname, email, salary = 9000):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        # self.email = f"{firstname}.{lastname}@hotmail.com"
        
    def information(self):# glöm inte att skriva self
        return f"{self.firstname} {self.lastname} and has a salary of {self.salary}"


    #Metod nummer 2
    def email(self):
        return f"{self.firstname}.{self.lastname}@hotmail.com"


emp_1 = Employee("Jason", "Bourne", "8000")#objekt av instans class


print(emp_1.information())

#denna är att föredra
print(Employee.information(emp_1))


# print(emp_1.firstname)
# print(emp_1.lastname)
# print(emp_1.salary)

# print("{} {}".format(emp_1.firstname, emp_1.lastname))  #format är en inbyggd metod


