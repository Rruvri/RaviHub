


class Item:
    def __init__(self, name, cat):
        self.name = name
        self.cat = cat
        
        self.item_dict = {
            "item": (f"{self.name}"),
            }
        
    

    def add_to_collection(self, collections):
        for c in collections:
            if self.cat.lower() == c["name"].lower():
                
                
                c["items"].append(self.item_dict)


            else:
                collections.append(Collection(self.cat))
                f"{self.cat}".items.append(self.item_dict)
                return collections
    
class Collection:
    def __init__(self, name):
        self.name = name
        self.items = []
        
    
    def view_items(self):
        for item in self.items:
            print(item["name"])


# defs
def create_new_item(col):
    name_input = input("Item name: ")
    cat_input = input("Item category: ")
    new_item = Item(name_input, cat_input)
    new_item.add_to_collection(col)

def create_new_collection(col):
    input = input("Collection name: ")
    new_col = Collection(input)
    col.append(new_col)
    return col

"""
# dead code (for now)

new_name = input("Item name: ")
    new_cat = input("Item category: ")
    use_choice = input("Single-use[1], or indefinite amount usage[2]? Enter choice [1/2]: ")
    if use_choice == 1:
        new_item = SingleUseItem(new_name, new_cat)


class SingleUseItem(Item):
    def __init__(self, name, cat):
        super().__init__(name, cat)

    def uses_calc(self, amount, start_date):
        self.amount = amount
        self.start_date = start_date


def uses_calc(self, amount, start_date):
        # will be overridden on typecat basis
        pass
"""
