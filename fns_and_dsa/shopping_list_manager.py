def display_menu():
    print("\n--------SHOPPING MANAGER-------")
    print("1. Add Item")
    print("2. Remove List")
    print("3. View List")
    print("4. EXit")
    print ("---------------------------------")
    
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            item= input("Enter an Item: ")
            shopping_list.append(item)
            print(item, "has been added to the list")
    
        elif choice == '2':
            item= input("Which item do you want to remove from your list")
            if item in shopping_list:
                shopping_list.remove(item)
                print(item, "Successfully removed")
            else:
                print(item, "is not in your list")
                
            
        elif choice == '3':
            if len(shopping_list) == 0:
                print("Your list is empty.")
            else:
                for item in shopping_list:
                    print(item)

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()