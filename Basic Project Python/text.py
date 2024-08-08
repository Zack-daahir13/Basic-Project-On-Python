class loan:
  def __init__(self, anualinterestrate= 1, numofyears= 2.5, loanamount= 7, borrowe= ""):
    self.__anualinterestrate = anualinterestrate
    self.__numofyears = numofyears
    self.__loanamount = loanamount
    self.__borrowe = borrowe
  
  def getanualinterestrate (self):
    return self.__anualinterestrate

  def getnumofyears (self):
    return self.__numofyears
  
  def getloanamount (self):
    return self.__loanamount
  
  def getborrowe (self):
    return self.__borrowe

  def setanualinterestrate (self, anualinterestrate):
    self.__anualinterestrate = anualinterestrate
    
  def setnumofyears (self, numofyears):
    self.__numofyears = numofyears

  def setloanamount  (self, loanamount):
    self.__loanamount = loanamount
    
  def setborrowe (self, borrowe):
    self.__borrowe = borrowe
    
    
  def getmonthlypyment(self):
    monthlyinterestrate = self.__anualinterestrate / 1200
    monthlypyment = \
exit()
#instan method of object waa qaab aad ku print gareen karto class ka wuxuuna riference unoqonaa classka

class person:
  def subject(self):
    print("this subject is programin 2 python")
    
    
  def edditor(self):
    print("the edditor is visual studio code")
    
why=person()
why.subject()



#2 constractive method : markaad print gareeneeso kaliya waxaad waceesaa classka name 
# oo uma baahna inaad sameesato instant bmethod

class project:
  def __init__(self):
    print("this project is web developer")

project()

#
class Math:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
    

   
  def add (self):
    print("this is addition")
    print(self.num1 + self.num2)
    
    
  def subt(self):
    print("this is substriction")
    print( self.num1 - self.num2)
    
  def multiply(self):
    print("this is multplication")
    print(self.num1 * self.num2)
  
kudar =Math (6,6)
kudar = Math (10, 10)
kudar =Math (20, 20)
kudar.add()
kudar.add()
kudar.add()
kudar = Math(10, 4)
kudar.subt()
kudar = Math (10, 10)
kudar.multiply()

  
  
  
class xog:
  def  __init__(self, name, age, job):
    self.name = name
    self.age = age
    self.job = job
    
person = xog("zack", "25", "software developer")
print(person.name)
print(person.age)
print(person.job)


class cusub:
  def __init__ (self):
    print("hello welcome")  
    
cusub()
  
  
  
  
  
exit()
class warbixin:
  def __init__(self, name, age, job, cost):
    self.name= name
    self.age= age
    self.job= job
    self.cost= cost
    
report= warbixin("zack", "29", "manager bank", "100" )
print(report.name)
print(report.age)
print(report.job)
print(report.cost)


