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
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("(add) Enter name of item: ")
            shopping_list.append(item)
        elif choice == '2':
            item = input("(remove) Enter name of item: ")
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
