def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            shopping_list.remove(item)
        except ValueError:
            print("[ Error ]: Option choice is invalid!")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
        elif choice == '2':
            item = input("(remove) Enter the item to remove: ")
            try:
                shopping_list.remove(item)
            except ValueError:
                print("[ Error ]: Item not found in the shopping list!")
        elif choice == '3':
            print("================================================")
            print(shopping_list)
            print("================================================")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
