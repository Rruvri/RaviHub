
collections = []

class Item:
    def __init__(self):
        self.name = input("Item name: ")
        self.cat = input("Item category: ")

        
    def uses_calc(self, amount, start_date):
        # will be overridden on typecat basis
        pass

    def add_to_collection(self):
        for c in collections:
            if self.cat.lower() == c.name.lower():
                c.items.append(self)

    
class Collection:
    def __init__(self, name):
        self.name = name
        self.items = []
        collections.append(self)


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
"""
