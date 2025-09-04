import time
import os
def clear_console():
    os.system('clear')


class Item:
    def __init__(self, name, subcat):
        self.name = name
        self.subcat = subcat
        self.start_date = 'N/A'
        self.stock = 0

    def view_item(self):
        print(f"======== {self.name} ========")
        print(f'[1]Name: {self.name}\n[2]Subcategory: {self.subcat}\n[3]Active Start Date: {self.start_date}\n[4]Extra Stock: {self.stock}')
        option_select = input('Enter trait number to edit, or 0 to exit: ')
        if option_select == '1':
            self.name = input('Enter new item name: ')
        elif option_select == '2':
            self.subcat = input('Enter new subcategory name: ')
        elif option_select == '3':
            self.start_date = input('Enter start date for current item (DD/MM/YY): ')
        elif option_select == '4':
            self.subcat = input('Enter number of items in stock (excluding current active item): ')
        elif option_select == '0':
            return

    
class Collection:
    def __init__(self, name):
        self.name = name
        self.items = []

    def view_collection(self):
        clear_console()
        print(f"======== {self.name} ========")
        
        if not self.items:
            print("(empty!)")
            time.sleep(1.5)
            clear_console()

        for item in self.items:
            print(f"[{self.items.index(item)+1}] {item.name} ({item.subcat})")
        self.menu_actions()

        
    def menu_actions(self): 
        print("======== Actions ========\n[1]Add item\n[2]Edit/Remove item\n[3]Rename collection\n[0]Exit\n") 
        menu_action = input("Enter choice: ")
        
        if menu_action == "1":
            name = input("Item name: ")
            subcat = input("Item subcategory: ")
            self.items.append(Item(name,subcat))
            self.view_collection()
        
        elif menu_action == '2':
            select_item = input('Enter item number: ')
            self.items[int(select_item)-1].view_item()
            self.view_collection()


            
            


        elif menu_action == "3":
            new_name = input("Enter new collection name: ")
            self.name = new_name
            self.view_collection()
        
            
            
        elif menu_action == "0":
            clear_console()
            
#Maybe 'Memo' Collection object?
class Memo(Collection):
    def __init__(name, items):
        super().__init__(name, items)
        


#Create new objects   
def create_item(collections):        
    name = input("Item name: ")
    col = input("Item collection: ")
    subcat = input("Item subcategory: ")
    
    item = Item(name, subcat)

    for c in collections:
        if col.lower() == c.name.lower():
            c.items.append(item)
            clear_console()
            break
    else:
        new_col = Collection(col)
        new_col.items.append(item)
        collections.append(new_col)
        clear_console()
    
def create_collection(collections):
    name = input("Collection name: ")
    new_collection = Collection(name)
    for c in collections:
        if c.name.lower() == name.lower():
            print("Collection already exists!")
            time.sleep(3)
            clear_console()
            break
    else:
        collections.append(new_collection)
        clear_console()
