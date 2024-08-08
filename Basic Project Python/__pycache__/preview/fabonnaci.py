s = input("enter word: ")
if len(s) % 2==0:
    print(s, "contains is even")
else:
    print(s, "contains an odd")
    
name = "cabdimaalik"
print(name[2])

h = "kani waa arday"
print(h[ :6])

x = "maxamed cabdi maalik"
print("cabdi" in x)

s = input("Enter a string: ")
if "Python" in s:
 print("Python", "is in", s)
else:
    print("python is not in", s)


sub = "python"
for i in range(0, len(sub), 2):
    print(sub[i], end= "")
    
exit()

        
#encaplation
class employee():
    def __init__(self, name, salary, project):
        self.name = name
        self.salary = salary
        self.project = project
        
    def show(self):
        print("name: ", self.name)
    def take(self):
        print(self.name, "wuxuu qaataa lacag gaareeso: ", self.salary)
    def work (self):
        print(self.name, "is working", self.project)
emp = employee("cabdimaalik c/laahi muuse: ", 2000, "Primier Bank" )
emp.show()
emp.take()
emp.work()
#inheritance
class parent():
    def first(self):
        print("first function")
        
    def second(self):
        print("second child")
ob = parent()
ob.first()
ob.second()
#object
class employee():
    def __init__ (self, name, age, compony):
        self.name = name
        self.age = age
        self.compony = compony
        
        
var = employee("zaki", 20, "hormuud")
print(var.name)
var = employee("cabdimaalik", 25, "IBS BANK")
print(var.name)
print(var.age)
print(var.compony)

        
exit()
l = [1, 2, 3, -1, -1]
x = [l[0] + l[1] + l[2], l[-1] + l[-2]]
print(x)


















exit()
def fabonnacia(lis, count):
    if len(lis)<=1:
        return[]
    update_list =lis
    for _ in range(count):
        number = lis[-1] + lis[-2]
        update_list.app