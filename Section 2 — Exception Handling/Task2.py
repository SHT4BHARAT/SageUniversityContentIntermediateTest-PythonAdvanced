class LoginSystem:
    __password = "python@123"
    __attempts = 3
    
    def __init__(self):
        pass

    def login(self):
        try:
            if self.__attempts == 0:
                raise AccountLockedError
            
            else:
                for i in range(self.__attempts):
                    pas=input("Enter the Password:")
                    if pas==self.__password:
                        print("Login Succesfully")
                    else:
                        self.__attempts-=1
        except AccountLockedError:
            print("No Remaining Login Attempts")

        except Exception as e:
            print ("Login Failed:",e)

        finally:
            pass 

l=LoginSystem()
l.login()


                

            
                



            

      



     