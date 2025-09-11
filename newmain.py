#Imports + sys commands

import os
import sys
import time
import pickle

from newobjects import *
from tracking import *

def clear_console():
    os.system('clear')

# Set-Up
    
collections = []

with open('collection_save.pkl', 'rb') as f:
    collections_load = pickle.load(f)
collections = collections_load

memos = Memos()
memos.items = []






def main():
    while True:
        
        print("======= RaviHub =======")
        print("Open Collections:")
        for col in collections:
            print(f"{col.name}: {[item.name for item in col.items]}")
        print("=======================")
        
#Main Menu + Options

        menu_choice = input("Actions:\n[1]Create new item\n[2]Create new collection\n[3]View a collection\n[4]Delete a collection\n[5]Add new memo\n[0]Save and exit\n\nEnter choice: ")
        
        if menu_choice == "1":
            clear_console()
            create_item(collections)

        elif menu_choice == "2":
            clear_console()
            create_collection(collections)

        elif menu_choice == "3":
            clear_console()
            if not collections:
                    print("No collections yet, returning to main menu...")
                    time.sleep(2)
                    clear_console()   
            for col in collections:
                print(f"[{collections.index(col) + 1}] {col.name}\n") 
            view_choice = input("Enter collection [number]: ")
            clear_console()
            collections[int(view_choice) -1].view_collection()

        elif menu_choice == '4':
            for col in collections:
                print(f"[{collections.index(col) + 1}] {col.name}\n") 
            delete_choice = input("Enter collection [number]: ")
            confirm = input("Are you SURE you want to delete?[Y/N]: ")
            if confirm.lower() == 'y':
                del collections[int(delete_choice) -1]
            elif confirm.lower() == 'n':
                break
        
        elif menu_choice == '5':

            
        elif menu_choice == '0':
            clear_console()
            with open('collection_save.pkl', 'wb') as f:
                pickle.dump(collections, f)
            print("Saved! Now exiting...")
            time.sleep(1)
            sys.exit()

            
         
            

         

        

    

main()