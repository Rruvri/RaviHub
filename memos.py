from items import *


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
