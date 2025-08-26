


class Item:
    def __init__(self, name, cat):
        self.name = name
        self.cat = cat
        
        self.item_dict = {
            "item": (f"{self.name}"),
            }
        
    def add_to_collection(self, col):
        for c in col:
            if self.cat.lower() == c["name"].lower():
                
                
                c["items"].append(self.item_dict)


            else:
                new_col = (Collection(self.cat))
                col.append(new_col)
                new_col.items.append(self.item_dict)
                return col
    
class Collection:
    def __init__(self, name):
        self.name = name
        self.items = []
        
    
    def view_items(self):
        for item in self.items:
            print(item["name"])


# defs


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
