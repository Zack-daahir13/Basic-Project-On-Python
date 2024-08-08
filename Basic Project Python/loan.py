s1 = "welcome"
print(s1 [-3 : -1])

















class loan:
    def __init__(self, anualinterestrate=2.5, numofyears= 1, loanamount= 1000, borrowe = "" ):
        self.__anualinterestrate= anualinterestrate
        self. numofyears=numofyears
        self. __loanamount = loanamount
        self. __borrowe = borrowe
        
    def getanualinterestrate (self):
        return self. __anualinterestrate
    
    def getnumofyears(self):
        return self. numofyears
    
    def getloanamount(self):
        return self. __loanamount
    
    def getborrowe(self):
        return self.__borrowe
    
    def setanualinterestrate(self, anualinterestrate):
         self.__anualinterestrate= anualinterestrate
    def setnumofyears(self, numofyears):
        self. numofyears=numofyears
    def setloanamount(self, loanamount):
        self. __loanamount = loanamount
    def setborrowe(self, borrowe):
        self. __borrowe = borrowe
        
    def getmonthlypyment(self):
        monthlytinterestrate= self.__anualinterestrate / 1200
        monthlypymen = \
        self. __loanamount * monthlytinterestrate /(1-(1/ (1+ monthlytinterestrate)**(self.numofyears*12)))
        return monthlypymen
    
    def gettotalpyment(self):
        totalpyment= self.getmonthlypyment() * \
            self.numofyears * 12
        return totalpyment