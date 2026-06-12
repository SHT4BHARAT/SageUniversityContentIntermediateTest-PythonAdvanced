class AgeVerification:
    def set_age(self):
        age=int(input("Enter the age:"))
        try:
            if self.age<0:
                raise ValueError
            if self.age < 18:
                raise UnderAgeError
            if self.age > 100:
                raise InvalidAgeError
            else:
                print("Valid Age!")
        except ValueError :
            print("Age cannot be less then Zero")
"""
        except UnderAgeError :
            print("Not Eligible to Vote")

        except InvalidAgeError :
            print("Age cannot more then 100")
"""
       

a=AgeVerification()
a.set_age()

"""try:
    num=int(input("enter the number"))
    print(10/num)
except ZeroDivisionError:
    print("Cannot divide by zero ")
except ValueError:
    print("type number only")
    """