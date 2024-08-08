class bank_acount:
    def __init__(self, owner_name, amount):
        self.name = owner_name
        self.Balance = amount
        
    def with_draw(self):
        
        person_name = input("enter name: ")
        if person_name == self.owner_name:
            amount = input("enter your amount: ")
            self.Balance -= int(amount)
            print(f"you have with draw ${amount}"  )
        else:
            print("") 
            
    def get_balance(self, name):
        if name ==self.owner_name:            
            print(f'')
        else:
            ("this name is wrong")
        
user1 = bank_acount("zack", 1000)
user1.with_draw(100)
        
        
        