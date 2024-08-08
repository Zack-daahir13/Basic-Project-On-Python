class item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
class warehouse:
    def __init__(self):
        self.items = []
        
    def add_item(self,item):
        self.items.append(item)
        
    def remove_item(self, item):
        self.items.remove(item)
        
    def search_item(self, name):
        search_result = []
        for item in self.items:
            if item.name == name:
                search_result.append(item)
        return search_result
    

item1 = item("chery", 10, 12)
item2 = item("table", 13, 9)
item3 = item("iphone 14 pro", 30, 800)
item4 = item("iphone 12 pro", 30, 800)
item5 = item("sumsung s23 ultra", 10, 500)

# create ware house instance
warehouse = warehouse()
warehouse.add_item(item1)
warehouse.add_item(item2)
warehouse.add_item(item3)
warehouse.add_item(item4)
warehouse.add_item(item5)


search_result= warehouse.search_item("iphone 14 pro")
for item in search_result:
    print("item name: ", item.name)
search_result= warehouse.search_item("table")
for item in search_result:
    print("price: ", item.price)
    print("quantity: ", item.quantity)
        
        
        
        