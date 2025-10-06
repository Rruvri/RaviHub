import os
import sys

    
def clear_console():
    os.system('clear')


def tester(collections, groups):
    for c in collections:
        for item in c.items:
            if item.active_item:
                print(item.name, item.active_item)
            if item.item_history:
                print(f'    {item.name}, {item.item_history}')
    if groups:
        print(groups.items()) 

def dev_mode():
    pass