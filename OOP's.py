#Classes And Objects.
#why we are creating classes and objects?
#******************************************* object -------> ex:- x=10, a="hello world"...........
#how to create a class?
#use the keyword "Class"
"""class customer:
    pass
#object creation
c1 = customer()
print(c1)"""
#what is ---main---?
#main is nothing but from which file the class is coming from

"""attributes:- these are 2 types (class and object).
1. class attribute(common attributes):- comes from class and these attributes accessible by every object
2. object attribute:- means unique attributes that can be applicable to particular object"""

#creats a class
class customer:
#create class attributes---> creating variables inside the class
    bank_name = "HFC Bank"
    branch = "Mumbai"
    state = "Maharashtra"
    ifsc = "HFC0000023"
#create an object
c1 = customer() 
c2 = customer()
#how can an object access the class attribute?
print(c1.bank_name)
print(c2.ifsc)

#create a methods for class customers
#what is methods?
#methods can be created inside the class.
#methods are nothing but creating functions inside the class
class customer:
#create class attributes---> creating variables inside the class
    bank_name = "HFC Bank"
    branch = "Mumbai"
    state = "Maharashtra"
    ifsc = "HFC0000023"
"""before creating the object attributes we need to initiate object
attributes inside the class"""
def __init__(self,name,age,initial_amount,acc_no):
#whai is __init__ ?
#when you create an object by default it runs with init method ---> it is nothing but initialization method"""
    self.name = name
    self.age = age
    self.initial_amount = initial_amount
    self.acc_no = acc_no
#creating methods (inside class)
    def welcome(self):
        print(f"hello {self.name} and welcome to {self.bank_name}, {self.branch}")
    def check_balance(self):
        print(f'your current balance is {self.initial_amount}')
    def deposit(self,amount):
        self.initial_amount += amount #--->initial_amount = initial_amount + amount
        print(f"transaction is completed."
              f"{amount} has been created to your {self.acc_no}."
              f"the updated balance is {self.initial_amount}")
    def withdraw(self,amount):
        if amount <= self.initial_amount:
            self.initial_amount -= amount
            print(f"transaction is completed."
                  f"{amount} has been deduct from your {self.acc_no}."
                  f"the updated balance is {self.initial_amount}")
        else:
            print("insufficient balance")
            self.check_balance()

#create an object attribute
c1 = customer("python",22,10000,123456789)
c2 = customer()
#c2 = customer()
#how can we access the particular methods?
#c1.welcome()
#c1.check_balance()
c1.deposit(10000)
c1.withdraw(20000)
#how can an object access the class attribute?
print(c1.bank_name)
#print(c2.ifsc)
#how can an object access object attributes?
print(c1.initial_amount)

#class.method(object)
#what is self?
#its a extra parameter in the method definition
#self act as a pointer/reference to act as an object

x = "hello"
x.upper()




































