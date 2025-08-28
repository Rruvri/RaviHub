import os
import sys
import time
import pickle
from newobjects import *

def clear_console():
    os.system('clear')
    
collections = []

with open('collection_save.pkl', 'rb') as f:
    collections_load = pickle.load(f)
collections = collections_load



    



def main():
    while True:
        print("======= RaviHub =======")
        print("Open Collections:")
        for col in collections:
            print(f"{col.name}: {[item.name for item in col.items]}")
        print("=======================")

        menu_choice = input("Actions:\n[1]Create new item\n[2]Create new collection\n[3]View a collection\n[4]Save and exit\nEnter choice: ")
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
            clear_console()
            with open('collection_save.pkl', 'wb') as f:
                pickle.dump(collections, f)
            print("Saved! Now exiting...")
            time.sleep(1)
            sys.exit()

            
         
            

         

        

    

main()