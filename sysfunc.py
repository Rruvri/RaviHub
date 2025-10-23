import os
import sys

	
def clear_console():
	os.system('clear')


def tester(collections, groups, prev_dt):
	print(prev_dt)
	print('\n\n')
	
	for c in collections:
		for item in c.items:
			if item.active_item:
				print(item.name, item.active_item)
			if item.item_history:
				print(f'->    {item.name}, {item.item_history}')
	print('\n\n')
	if groups:
		print(groups.items()) 
	
def reset_groups(collections):
	for c in collections:
			for item in c.items:
				item.item_dict["Groups"] = {}



def dev_mode():
	pass