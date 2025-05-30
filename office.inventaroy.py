FILENAME = "inventory.txt"
inventory = {}

def store_inventory():

    with open(FILENAME, "w") as file:
        for item in inventory:
            file.write(item + "\n")

def load_inventory():

    global inventory
    inventory = {}
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                item = line.strip()
                inventory[item] = True
    except FileNotFoundError:
        print("No inventory file found. Starting fresh.")

def display_inventory():

    if inventory:
        print("Current Inventory:")
        for item in inventory:
            print("- " + item)
    else:
        print("Inventory is empty.")

def add_item():

    item = input("Enter the item: ").strip()
    if item in inventory:
        print("Item is already present.")
    else:
        inventory[item] = True
        store_inventory()
        print("Item added successfully.")

def remove_item():

    item = input("Enter the item: ").strip()
    if item in inventory:
        del inventory[item]
        store_inventory()
        print("Item removed successfully.")
    else:
        print("Item not found.")

def main():

    load_inventory()

    while True:
        print(" Welcome to Inventory Management")
        print("1. Display Inventory")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            display_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            print("Exiting")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

