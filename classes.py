from sysfunc import clear_console
from tracking import c_d_formatted
from items import *
from memos import *




import time



def input_to_dt():
	pass # what did you want to do with this?
	
			
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
				
			print(f'[{self.items.index(item)+1}] {item.name} ({item.item_dict['Subcollection']}) | ({item.stock} in stock)')
			if item.active_item:
				base_active = f'   -> Active item | Start date: {item.active_item["Start Date"]} '
				
				
				if item.item_dict["Measure Type"] == 'Count (per item)':
					base_active = base_active + f' [{item.item_dict["Count per Unit"] - item.active_item["Uses"]}/{item.item_dict["Count per Unit"]} remaining]'
					
					
				elif item.item_dict["Measure Type"] == 'Weight (per item)':
					if item.item_dict['Use Style'] == 'Percentage':
						base_active = base_active + f' [{item.active_item["Percentage remaining"]}% remaining]'
					elif item.item_dict['Use Style'] == 'Average':
						base_active = base_active + f' [{item.active_item["Uses"]} uses in current period]'
				else:
					base_active = base_active + f'[{item.active_item["Uses"]} in current period]'
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
			
			
			group_name = input('Enter group name: ')
			group_items = input('Select items for group, separated with [,]')
			group = [] + groups.get(group_name, [])
			for item_number in group_items.split(','):
				gr_use_amount = input(f'For {self.items[int(item_number)-1].name}, enter use amount for group usage: ')
				
				self.items[int(item_number)-1].item_dict["Groups"][group_name] = gr_use_amount
				group.append(self.items[int(item_number)-1].name)
				
			groups[group_name] = group
			
			
			
		elif menu_action == "":
			clear_console()
			return
			
			
		clear_console()
		self.view_collection()

			
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

