from world_objects import *

collections = []
def add_item():
    name = input("Item name: ")
    cat = input("Collection name: ")
    new_item = Item(name, cat)
    new_item.add_to_collection(collections)
    return collections



def main():
    while True:
        print("======= RaviHub =======")
        print("Active collections:")
        for c in collections:
            print(f"{c["name"]}: {c["items"][0]}")


        add = input("Add item [y/n]? ")
        if add == "y":
            add_item()
            

main()
