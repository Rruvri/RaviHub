import time
import os



def clear_console():
    os.system('clear')


class Item:
    def __init__(self, name, col, subcat, item_dict={}, active_item=[], stock=0, item_history=[]):
        self.name = name
        self.subcat = subcat
        self.col = col
        self.stock = stock
        self.item_dict = item_dict
        self.active_item = active_item
        self.item_history = item_history
        self.init_dict()

    def init_dict(self):
        self.item_dict = {'Name': self.name,
                           'Collection': self.col,
                             'Subcollection': self.subcat,
                               'Brand': 'N/A',
                               'Price': 'N/A',
                               'Measure Type': 'N/A'}

    def activate_new_item(self, unit='N/A'):
        if self.active_item:
            print(f'[Current active item]\nStart: {self.active_item[0][0]}\nEnd: {self.active_item[0][1]}')
            confirm_new_active = input('Confirm new active item (current will be saved to history)? [Y/N]: ')
            if confirm_new_active == 'y'.lower():
                if len(self.active_item[0]) == 1:
                    self.conclude_item()
                    
        start = input('Enter start date of new item use: ')
        self.active_item = [(start, ), (unit, 0)]


    def conclude_item(self):
        end_date = input('Enter end date for current [DD/MM/YY]: ')
        final_date_stats = self.active_item[0] + (end_date,)
        self.active_item[0][1] = final_date_stats
        self.item_history.append(self.active_item)
        del self.active_item[1]
        self.stock -= 1

    def use_item(self, uses):
        pass
    
    def update_stock(self):
        print(f'In stock (excluding current active item): {self.stock}')
        self.stock = input('Enter new stock number: ')

    def view_item_traits(self):
        print(f"======== {self.name} ========")
        index_num = 1
        for key, value in self.item_dict.items():
            print(f'[{index_num}] {key}: {value}')
            index_num +=1

        self.edit_item()
    
    def edit_item(self):
        trait_list = list(self.item_dict.keys()) 
        option_select = input('Enter trait number to edit, or [0] to exit: ')  
        
        if option_select == '0':
            return
        
        #This is messy exit code, need to handle the errors
        elif int(option_select) > len(trait_list):
            print('Invalid option, please try again or exit')
            clear_console()
            self.view_item_traits()

        change = input(f'Enter change for {trait_list[int(option_select)-1]}: ')
        self.item_dict[trait_list[int(option_select)-1]] = change
        
        self.view_item_traits()
    
    
        
        

class Count(Item):
    def __init__(self, name, col, subcat, item_dict, active_item, stock, item_history, count_per_item):
        super().__init__(name, col, subcat, item_dict, active_item, stock, item_history)
        self.count_per_item = count_per_item
        self.item_dict["Measure Type"] = 'Count (per item)'
        self.item_dict["Count per Unit"] = count_per_item
      
    def activate_new_item(self, unit='N/A'):
        return super().activate_new_item(self.count_per_item)
    
    def use_item(self, count_used):
        count_copy = int(self.active_item[1][0])
        new_active_count = int(count_copy - count_used)
        if new_active_count < 1:
            self.conclude_item()
        self.active_item[1] = (new_active_count,)
        
            
            
        
        

class Measure(Item):
    def __init__(self, name, subcat, start_date, stock, measure_per_item, item_unit_measure):
        super().__init__(name, subcat, start_date, stock)
        self.measure_per_item = measure_per_item
        self.item_unit_measure = item_unit_measure

        self.item_avg_history = []

        self.active_item = []

        if self.start_date != 'N/A':
            self.active_item.append(self.start_date, self.measure_per_item, 0)

    def manage_measure(self, count_used=0, amount_used=0):
        
        self.active_item[2] + count_used
        
        self.active_item[1] - amount_used

        if self.active_item[1] == 0:
            end_date = input("Enter active item's finish date (DD/MM/YY): ")
            item_avg = {'Start date':self.active_item[0], 'End date':end_date} #TO-DO: add averaging method
            self.item_avg_history.append(item_avg)
            self.active_item = []
            self.start_date = 'N/A'
        
        








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
            print(f"[{self.items.index(item)+1}] {item.name} ({item.subcat}) | ({item.stock} in stock)")
            if item.active_item:
                base_active = f'   -> Active item | Start date: {item.active_item[0][0]}' 
                if item.item_dict["Measure Type"] == 'Count (per item)':
                    base_active = base_active + f' [{item.active_item[1][1]}/{item.active_item[1][0]} used]'
                print(base_active+'\n')

        self.menu_actions()

        
    def menu_actions(self): 
        print("======== Actions ========\n[1]Add item\n[2]Edit/Remove item\n[3]Rename collection\n[4]Upgrade item\n[5]Activate item\n[6]Use item\n[0]Exit\n") 
        menu_action = input("Enter choice: ")
        
        if menu_action == "1":
            name = input("Item name: ")
            subcat = input("Item subcategory: ")
            self.items.append(Item(name, self.name, subcat))
            self.view_collection()
        
        elif menu_action == '2':
            select_item = input('Enter item number: ')
            self.items[int(select_item)-1].view_item_traits()
            self.view_collection()

        elif menu_action == "3":
            new_name = input("Enter new collection name: ")
            self.name = new_name
            self.view_collection()


        elif menu_action == '4':
            select_item = input('Enter item number: ')
            
            selected_item = self.items[int(select_item)-1]
            
            print(f'Selected: {selected_item.name}')
            
            item_measure_parameters = input('Is the item a [C]ountable (i.e. a pack of SIX eggs), or a [M]easurable (i.e. a ONE KG bag of lentils)? Enter choice: ')
            
            if item_measure_parameters == 'c'.lower():
                count_per_item = input('Enter the number of uses each new item has (i.e., a pack of SIX eggs has 6 uses): ')
                new_count_item = Count(selected_item.name, selected_item.col, selected_item.subcat, selected_item.item_dict, selected_item.active_item, selected_item.stock, selected_item.item_history, count_per_item)
                self.items.pop(int(select_item)-1)
                self.items.append(new_count_item)
            self.view_collection()

        elif menu_action == '5':
            select_item = input('Enter item number: ')
            self.items[int(select_item)-1].activate_new_item()
            self.view_collection()
        
        elif menu_action == '6':
            select_item = input('Enter item number: ')
            use_amount = input('Enter amount used: ')
            self.items[int(select_item)-1].use_item(int(use_amount))
                
                        
        elif menu_action == "0":
            clear_console()





            
#========Memos

#Need to see how to check if col is memo, so it can be printed separately 
class Memos:
    def __init__(self):
        self.items = []
    
    def view_collection(self):

        for memo in self.items:
            if not self.items:
                print('No memos!')
                return
            base_memo = f"[{self.items.index(memo)+1}] {memo.name} | {memo.start_date}"
            if memo.notes != 'N/A':
                print(f'{base_memo} (view to see notes)')
            else:
                print(base_memo)  
    
    def full_view(self):
        for memo in self.items:
            if not self.items:
                print('No memos!')
                return
            base_memo = f"[{self.items.index(memo)+1}] {memo.name} | {memo.start_date}"
            if memo.notes != 'N/A':
                print(f'{base_memo}\n-> {memo.notes}\n')
            else:
                print(f'{base_memo}\n')
        
        menu_choice = input('=======================\nActions:\n[1]Delete a memo\n[0]Return\nEnter choice: ')
        if menu_choice == '1':
             del_choice = input('Enter memo no. to delete (or 0 to exit): ')
             if del_choice == '0':
                 self.full_view()
             del self.items[int(del_choice)-1]
             self.full_view()
        
        elif menu_choice == '0':
            clear_console()
            return


#todo - finish this + main interactions

class Memo(Item):
    def __init__(self, name, subcat):
        super().__init__(name, subcat)
        self.notes = 'N/A'
        self.start_date = 'N/A'
    
    def view_item(self):
        print(f'{self.start_date}|{self.name}[{self.subcat}]')
        if self.notes != 'N/A':
            print(self.notes)
        

        


#=============Create new objects

#=items    
def create_item(collections):        
    name = input("Item name: ")
    col = input("Item collection: ")
    subcat = input("Item subcategory: ")
    
    item = Item(name, col, subcat)

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

#memos
def create_memo(memos):
    title = input('Memo header: ')
    cat = input('Memo category: ')
    new_memo = Memo(title, cat)
    
    date = input('Enter memo date (DD/MM/YY) if required, return(enter) if not: ')
    if date != '':
        new_memo.start_date = date
    notes = input('Enter memo notes if required, return(enter) if not: ')
    if notes != '':
        new_memo.notes = notes
    memos.items.append(new_memo)
    clear_console()

#collections         
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
    
