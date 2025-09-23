import time
import os



def clear_console():
    os.system('clear')



class Item:
    def __init__(self, name, col, subcol):
    
        self.name = name
        self.col = col
        self.subcol = subcol
        self.active_item = [] 
        self.stock = 0       
        
        self.item_dict = {'Name': self.name,
                           'Collection': self.col,
                             'Subcollection': self.subcol,
                               'Specifics': 'N/A'}

    #TODO - Define active item

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

    def set_active_item(self, start_date):
        self.active_item = [start_date]
        #return self.active_item
    def set_stock(self, new_stock):
        self.stock = int(new_stock)
        



class Collection:
    def __init__(self, name):
        self.name = name
        self.subcols = []
        
    def view_collection(self):
        clear_console()
        
        print(f"======== {self.name.upper()} ========")
        
        if not self.subcols:
            print("(empty!)")
            time.sleep(1.5)
            clear_console()
        
        for subcol in self.subcols:
            print(f'----{subcol.name}----')
            for item in subcol.items:
                base_item_info = f"[{subcol.items.index(item)+1}] {item.name} ({item.subcol})"
                print(base_item_info)
                #print( | Active start date: {item.start_date} ({item.stock} in stock)")
    
    def add_item(self, item):
        if item.subcol not in list(map(lambda subcol: subcol.name, self.subcols)):
            new_subcol = Subcollection(item.subcol, '', self.name)
            self.subcols.append(new_subcol)
            
        for subcol in self.subcols:
            if item.subcol == subcol.name:
                subcol.items.append(item)

        self.view_collection()
        
            
class Subcollection(Collection):
    def __init__(self, name, parent_col):
        super().__init__(name)
        self.parent_col = parent_col
        self.items = []
    
    
        

    ''' 
    self.menu_actions()   
    def menu_actions(self): 
        print("======== Actions ========\n[1]Add item\n[2]Edit/Remove item\n[3]Rename collection\n[4]Upgrade item\n[0]Exit\n") 
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


        elif menu_action == '4':
            select_item = input('Enter item number: ')
            
            selected_item = self.items[int(select_item)-1]
            
            print(f'Selected: {selected_item.name}')
            
            item_measure_parameters = input('Is the item a [C]ountable (i.e. a pack of SIX eggs), or a [M]easurable (i.e. a ONE KG bag of lentils)? Enter choice: ')
            
            if item_measure_parameters == 'c'.lower():
                count_per_item = input('Enter the number of uses each new item has (i.e., a pack of SIX eggs has 6 uses): ')
                new_count_item = Count(selected_item.name, selected_item.subcat, selected_item.start_date, selected_item.stock, count_per_item)
                self.items.pop(int(select_item)-1)
                self.items.append(new_count_item)    
                
                        
        elif menu_action == "0":
            clear_console()
        '''


        








'''

























        







class Count(Item):
    def __init__(self, name, subcat, start_date, stock, count_per_item):
        super().__init__(name, subcat, start_date, stock)
        self.count_per_item = count_per_item

        self.base_options = self.base_options + f'\n[5]Units per item: {self.count_per_item}'
        
        self.item_avg_history = []
        
        self.active_item = []

        if self.start_date != 'N/A':
            self.active_item.append(self.start_date, self.count_per_item)
        
    def view_item(self):
        super(Count, self).view_item
        
        if super().view_item.option_select == '5':
            self.count_per_item = input('Enter new units per item: ')
            
    
    def manage_count(self, count_used):
        self.active_item[1] - count_used
        if self.active_item[1] < 1:
            end_date = input("Enter active item's finish date (DD/MM/YY): ")
            item_avg = {'Start date':self.active_item[0], 'End date':end_date} #TO-DO: add averaging method
            self.item_avg_history.append(item_avg)
            self.active_item = []
            self.start_date = 'N/A'
    

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
    

        
'''