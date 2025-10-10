from sysfunc import clear_console
from tracking import c_d_formatted
import time



def input_to_dt():
    pass







class Item:
    def __init__(self, name, col, subcat):
        self.name = name
        self.col = col
        self.subcat = subcat

        #for c in cols:
         #   if col.lower() == c.name.lower():
         #Move this to a main function

        
        self.stock = 0
        self.item_dict = {'Name': self.name,
                           'Collection': self.col,
                             'Subcollection': self.subcat,
                             'Measure Type': 'N/A'}
        
        self.item_variants = []
        
        self.item_history = []

        self.active_item = {}

    def view_dict(self, dictionary):
        clear_console()
        index_num = 1

        for key, value in dictionary.items():
            print(f'[{index_num}] {key}: {value}')
            index_num +=1
        edit_choice = input('Enter entry number to edit, [return] to exit: ')
        if edit_choice == '':
            clear_console()
            return
        key_list = list(dictionary)
        selected_key = dictionary[key_list[int(edit_choice)-1]]
        
        
        if isinstance(selected_key, dict):
            return self.view_dict(selected_key)
        
        #could use a lambda here
        new_value = input('Enter new value: ')
        if isinstance(selected_key, int):
            new_value = int(new_value)
        elif isinstance(selected_key, float):
            new_value = float(new_value)
        elif isinstance(selected_key, tuple):
            new_value = tuple(new_value)
        
        
        dictionary[key_list[int(edit_choice)-1]] = new_value
        
        
    
    def view_item_traits(self):
        clear_console()
        print(f"======== {self.name} ========")
        self.view_dict(self.item_dict)
    
    def update_stock(self):
            print(f'In stock (excluding current active item): {self.stock}')
            self.stock = int(input('Enter new stock number: '))

    def activate_item(self):
        if self.active_item:
            self.conclude_item()

        s_d = input('Enter start date of new item [DD/MM/YY]: ')
        self.active_item = {'Start Date': s_d,
                             'Uses': 0,
                               'End Date': None,
                                 'Use Log': {}}
        if int(self.stock) > 0:
            self.stock -= 1
        

    def conclude_item(self):
        print(f'\nYou currently have an active item!\n  Start: {self.active_item['Start Date']}\n   Uses: {self.active_item['Uses']}')
        old_end = input('\nEnter the end date [DD/MM/YY] for this item, or [return] to go back')
        if old_end == '':
            clear_console()
            return self.view_item()
        
        self.active_item['End Date'] = old_end
        archive_copy = self.active_item
        self.item_history.append(archive_copy)
        self.active_item = False

        if self.stock > 0:
            self.stock -= 1

    def use_item(self, ext_uses=False):
        if not self.active_item:
            self.activate_item()
        if ext_uses:
            uses = int(ext_uses)
        else:
            uses = int(input('Enter amount used: '))
        
            
        use_copy = int(self.active_item['Uses'])
        use_copy += int(uses)
        self.active_item['Uses'] = int(use_copy) #might need to check these for int(/ str clash 

        
        current_date_uses = int(self.active_item["Use Log"].get(c_d_formatted, 0))
        self.active_item['Use Log'][f'{c_d_formatted}'] = current_date_uses + int(uses)
        

    def view_history(self):
        for hist_log in self.item_history:
            print(f'{hist_log}\n')

    def add_item_group(self, group_info):
        self.item_dict['Groups'].append(group_info)




# Subclasses

class Count(Item):
    def __init__(self, name, col, subcat, item_dict, active_item, stock, item_history, count_per_item):
        super().__init__(name, col, subcat)
        self.stock = stock
        self.item_dict = item_dict
        self.active_item = active_item
        self.item_history = item_history
        
        self.count_per_item = count_per_item
        self.item_dict["Measure Type"] = 'Count (per item)'
        self.item_dict["Count per Unit"] = int(count_per_item)

        if active_item:
            self.active_item['Remaining'] = self.item_dict["Count per Unit"] - self.active_item['Uses']  

      
    def activate_item(self):
        super().activate_item()
        
    def use_item(self, ext_uses=False):
        super().use_item()
        
        if int(self.active_item['Uses']) >= int(self.item_dict['Count per Unit']):
            self.conclude_item()



class Measure(Item):
    def __init__(self, name, col, subcat, item_dict, active_item, stock, item_history, measure_per_item, measure_unit, use_style):
        super().__init__(name, col, subcat)
        self.stock = stock
        self.item_dict = item_dict
        self.active_item = active_item
        self.item_history = item_history
        
        self.measure_per_item = measure_per_item
        self.measure_unit = measure_unit
        self.use_style = use_style
        self.item_dict["Measure Type"] = 'Weight (per item)'
        self.item_dict["Measure per Unit"] = measure_per_item
        self.item_dict["Measure Unit"] = measure_unit
        self.item_dict["Use Style"] = use_style

        if self.active_item and self.item_dict['Use Style'] == 'Percentage': 
            self.active_item['Percentage remaining'] = float(input('Enter estimated percentage remaining: '))
    
    def activate_item(self):
        super().activate_item()
        if self.item_dict['Use Style'] == 'Percentage':
            self.active_item['Percentage remaining'] = 100.0


    def use_item(self, ext_uses=False):
        if self.item_dict['Use Style'] == 'Percentage':
            if not self.active_item:
                self.activate_item()
            
            if ext_uses:
                perc_uses = int(ext_uses)
            else:
                perc_uses = float(input('Enter estimated percentage used: '))
            
            self.active_item['Percentage remaining'] = self.active_item['Percentage remaining'] - perc_uses
      
            current_date_uses = int(self.active_item["Use Log"].get(c_d_formatted, 0))
            self.active_item['Use Log'][f'{c_d_formatted}'] = current_date_uses + int(perc_uses)  

            if self.active_item['Percentage remaining'] <= 0.0:
                del self.active_item['Percentage remaining']
                self.conclude_item()
        else:
            super().use_item()


    






class Collection:
    def __init__(self, name):
        self.name = name
        self.items = []

    def view_collection(self):
        clear_console()
        print(f"======== {self.name} ========")

        for item in self.items:
            if not self.items:
                print('[Collection is empty!]')
                continue

            print(f"[{self.items.index(item)+1}] {item.name} ({item.subcat}) | ({item.stock} in stock)")
            if item.active_item:
                base_active = f'   -> Active item | Start date: {item.active_item['Start Date']} ' 
                
                
                if item.item_dict["Measure Type"] == 'Count (per item)':
                    base_active = base_active + f' [{item.item_dict['Count per Unit'] - item.active_item['Uses']}/{item.item_dict['Count per Unit']} remaining]'

                
                elif item.item_dict["Measure Type"] == 'Weight (per item)':
                    if item.item_dict['Use Style'] == 'Percentage':
                        base_active = base_active + f' [{item.active_item['Percentage remaining']}% remaining]'
                    elif item.item_dict['Use Style'] == 'Average':
                        base_active = base_active + f' [{item.active_item['Uses']} uses in current period]'
                else:
                    base_active = base_active + f'[{item.active_item['Uses']} in current period]'
                print(base_active+'\n')

        self.menu_actions()

    


    def menu_actions(self):
        print("======== Actions ========\n[1]Add item\n[2]Edit item\n[3]Rename collection\n[4]Upgrade item\n[5]Activate item\n[6]Use item\n[7]Update item stock\n[8]View active item log\n[9]Delete item\n[H]View item usage history\n[G]Add item group\n[return]Exit\n") 

              
        menu_action = input("Enter choice: ")

        if menu_action == "1":
            name = input("Item name: ")
            subcat = input("Item subcategory: ")
            self.items.append(Item(name, self.name, subcat))
            
        
        elif menu_action == '2':
            select_item = input('Enter item number: ')
            self.items[int(select_item)-1].view_item_traits()
            

        elif menu_action == "3":
            new_name = input("Enter new collection name: ")
            self.name = new_name
            
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


            elif item_measure_parameters == 'm'.lower():
                measure_unit = input('Enter the metric used to measure the item in its shorthand form (i.e. [g] for grams)   NOTE! - for items like a single onion, enter unit " whole" for now: ')
                measure_per_item = input('Enter the numeric measurement of the item (i.e. [1]kg bag of lentils)')
                use_style_check = input('Will the item be tracked on a [a]verage count method (i.e. recording number of cigarettes), or rough [p]ercentage tracker (i.e. using 50 percent of a bag of lentils)?')
                if use_style_check == 'a':
                    use_style = 'Average'
                elif use_style_check == 'p':
                    use_style = 'Percentage'
                new_measure_item = Measure(selected_item.name, selected_item.col, selected_item.subcat, selected_item.item_dict, selected_item.active_item, selected_item.stock, selected_item.item_history, measure_per_item, measure_unit, use_style)
                self.items.pop(int(select_item)-1)
                self.items.append(new_measure_item)
                

        elif menu_action == '5':
            select_item = input('Enter item number: ')
            self.items[int(select_item)-1].activate_item()
            self.items.append(self.items.pop(int(select_item)-1))
            
        
        elif menu_action == '6':
            select_item = input('Enter item number: ')
            self.items[int(select_item)-1].use_item()
            

        elif menu_action == '7':
            select_item = input('Enter item number: ')
            self.items[int(select_item)-1].update_stock()
            
        elif menu_action == '8':
            select_item = input('Enter item number: ')
            selected = self.items[int(select_item)-1]
            if not selected.active_item:
                print('No current active item!')
            else:
                selected.view_dict(selected.active_item)
                               
        elif menu_action == 'h':
            select_item = input('Enter item number: ')
            self.items[int(select_item)-1].view_history()
            exit_check = input('Press any key to exit')
            

        elif menu_action == '9':
            select_item = input('Enter item number: ')
            self.items.pop(int(select_item)-1)

        elif menu_action == 'g':
            from main import groups

            group_name = input('Enter group name: ')
            group_items = input('Select items for group, separated with [,]')
            group = [] + groups.get(group_name, [])
            for item_number in group_items.split(','):
                gr_use_amount = input(f'For {self.items[int(item_number)-1].name}, enter use amount for group usage: ')
                self.items[int(item_number)-1].add_item_group((group_name, gr_use_amount))
                group.append(self.items[int(item_number)-1].name)
            groups[group_name] = group


                        
        elif menu_action == "":
            clear_console()
            return
        
        
        clear_console()
        self.view_collection()

        
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
        
        menu_choice = input('=======================\nActions:\n[1]Delete a memo\n[return]Exit\nEnter choice: ')
        if menu_choice == '1':
             del_choice = input('Enter memo no. to delete (or [return] to exit): ')
             if del_choice == '0':
                 self.full_view()
             del self.items[int(del_choice)-1]
             clear_console()
             self.full_view()
        
        elif menu_choice == '':
            clear_console()
            return




class Memo(Item):
    def __init__(self, name, subcat):
        super().__init__(name, 'memos', subcat)
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