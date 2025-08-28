import time
import os
def clear_console():
    os.system('clear')

class Item:
    def __init__(self, name, subcat):
        self.name = name
        self.subcat = subcat
    
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
            print(f"{item.name}[{item.subcat}]\n")
        
        
        
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
