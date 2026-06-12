class Employee:

    __salary=50000
    def __init__(self,name):
        self.name=name

    def increment(self):
        self.__salary +=10000

    def deduct(self):
        self.__salary -=5000

    def get_salary(self):
        print(f"Salary of employees {self.name} is :{self.__salary}")


#Employee 1 Rahul
e1=Employee("Rahul")
e1.increment()
e1.deduct()
e1.get_salary()

#Employee 2 Rakesh
e2=Employee("Rakesh")
e2.increment()
e2.deduct()
e2.get_salary()
