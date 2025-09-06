expenses = [] # empty list to store the total expenses 
budget = 8,00,000
def menu():
    while(True):
        print("--WELCOME TO THE TASK MANAGEMENT APP--")
        print("1. Add new amount ")
        print("2. View all expenses")
        print("3. Remove  some amount")
        print("4. Exit")

        choise = int(input("Enter your choise "))
        if choise == 1:
            add_amount()
        elif choise == 2 :
            view_all_Expense()
        elif choise == 3 :
            remove_amount()
        elif choise == 4 :
            print(" Exiting the application...")
            exit()
        else :
            print("Invalid choise")


def add_amount():
    amount = int(input("Enter the amount"))
    expenses.append({"Amount" : amount })
    print("New amount added successfully")

def view_all_Expense():
    print("Your total expense  list")
    if len(expenses ) == 0:
        print("Zero amount in list ")
    else :
        total_expenses = sum(expenses)
        if total_expenses == budget:
            print("Zero saving")
        elif total_expenses > budget:
            print( f" you budget are over by {total_expenses- budget}")
        elif total_expenses < budget:
            print(f" you saving amount is { budget - total_expenses}")

def remove_amount():
    if len(expenses) == 0:
        print("List is empty !\n")
    else:
        try:
            search_index = int(input("Enter the amount that you want to remove ")) - 1
            if 0<=search_index  < len(expenses):
                removed_amount = expenses.pop(search_index)
                print(f"amount removed - {removed_amount['Amount']}\n")
            else:
                print("invalid amount .\n ")
        except ValueError:
            print("Please Enter a Valid amount \n ")
menu()
