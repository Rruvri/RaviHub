from world_objects import *

collections = []



def main():
    while True:
        print("======= RaviHub =======")
        for c in collections:
            print(f"{c["name"]}: {c["items"][0]}")


        add_item = input("Add item [y/n]? ")
        if add_item == "y":
            create_new_item(collections)
            main()

main()
