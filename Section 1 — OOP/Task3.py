#Hybrid inheritance Prohram 

class Father:
    def property(self):
        print("Father's Property")

    def business(self):
        print("Father's Business")

class Son(Father):
    def study(self):
        print("Son Study")

class Daughter(Father):
    def dance(self):
        print("Daughter Dance ")

class GrandChild(Son,Daughter):
    def gaming(self):
        print("GrandChild gaming")

g=GrandChild()
g.property()
g.business()
g.study()
g.dance()
g.gaming()