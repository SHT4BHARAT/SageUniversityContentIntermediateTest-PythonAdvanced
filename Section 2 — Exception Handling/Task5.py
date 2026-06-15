class AccountLockedError(Exception):
    pass

class LoginSystem:
    __password = "python@123"
    __attempts = 3
    
    def __init__(self):
        pass

    def login(self):
        try:
            for i in range(self.__attempts):
                pas=input("Enter the Password:")
  #             print({self.__attempts}-1)
                if pas==self.__password:
                    print("Login Succesfully")
                else:
                    print("Login Failed!\nTry again")
                    self.__attempts-=1
                
            if self.__attempts==0:
                raise AccountLockedError

        except AccountLockedError:
            print("No Remaining Login Attempts")

        except Exception as e:
            print ("Login Failed:",e)

        

l=LoginSystem()
l.login()


                

            
                



            

      



     