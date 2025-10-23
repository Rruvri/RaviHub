from sysfunc import clear_console
from tracking import c_d_formatted

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
		print('Enter entry number to edit, [return] to exit\n   [to add a new entry, enter key name, then [space], then value]')
		edit_choice = input(': ')
		if edit_choice == '':
			clear_console()
			return
		elif ' ' in edit_choice:
			add_entry = edit_choice.split(' ')
			dictionary[add_entry[0]] = add_entry[1]
			return #this works fine but needs a sort + update method
		
		key_list = list(dictionary)
		selected_key = dictionary[key_list[int(edit_choice)-1]]
		
		
		if isinstance(selected_key, dict):
			return self.view_dict(selected_key) #need to add option for adding entries (i.e. missed a day)
			
			
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
		print(f'\nYou currently have an active item!\n  Start: {self.active_item["Start Date"]}\n   Uses: {self.active_item["Uses"]}')
		old_end = input('\nEnter the end date [DD/MM/YY] for this item, or [return] to go back')
		if old_end == '':
			clear_console()
			return self.view_item()
			
		self.active_item["End Date"] = old_end
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
			self.active_item["Remaining"] = self.item_dict["Count per Unit"] - self.active_item["Uses"]
			
			
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
