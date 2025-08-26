from newobjects import *

collections = []


           
def main():
    while True:
        print("======= RaviHub =======")
        print("Open Collections:")
        for col in collections:
            print(f"{col.name}: {[item.name for item in col.items]}")
        print("=====================")

        menu_choice = input("Actions:\n[1]Create new item\n[2]Create new collection\n[3]View collection")
        if menu_choice == "1":
            create_item(collections)
         

        

    

main()