
class Item:
    def __init__(self, name, subcat):
        self.name = name
        self.subcat = subcat
    
class Collection:
    def __init__(self, name):
        self.name = name
        self.items = []
        
        
def create_item(collections):        
    name = input("Item name: ")
    col = input("Item collection: ")
    subcat = input("Item subcategory: ")
    
    item = Item(name, subcat)

    for c in collections:
        if col.lower() == c.name.lower():
            c.items.append(item)
            break
    else:
        new_col = Collection(col)
        new_col.items.append(item)
        collections.append(new_col)
    
    