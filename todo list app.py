todo_list = [] # empty list to store the task 
def menu():
    while(True):
        print("--WELCOME TO THE TASK MANAGEMENT APP--")
        print("1. Add new taks")
        print("2. View all task")
        print("3. Remove a task")
        print("4. mark a task as completed")
        print("5. Exit")

        choise = int(input("Enter your choise "))
        if choise == 1:
            add_task()
        elif choise == 2 :
            view_task()
        elif choise == 3 :
            remove_task()
        elif choise == 4 :
            done_task()
        elif choise == 5 :
            print(" Exiting the application...")
            exit()
        else :
            print("Invalid choise")


def add_task():
    task = input("Enter the task")
    todo_list.append({"Task" : task, "Status" : "pending" })
    print("New task added successfully\n ")


def view_task():
    print("Your Todo list")
    if len(todo_list)== 0:
        print("No pending task ")
    else :
        for index , task in enumerate(todo_list , 1):
            print(f"{index} : {task['Task']} - {task['Status']} ")
    print("\n")


def remove_task():
    if len(todo_list) == 0:
        print("List is empty !\n")
    else:
        try:
            search_index = int(input("Enter the task number that you want to remove ")) - 1
            if 0<=search_index  < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"task removed - {removed_task['Task']}\n")
            else:
                print("invalid Task number.\n ")
        except ValueError:
            print("Please Enter a Valid Task Number \n ")


def done_task():
    if len(todo_list) == 0:
        print("List is empty")
    else:
        try:
            search_index = int(input("What is the index of the task that you want to mark as done"))
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]['Status'] = 'Done'
                print(f" Task {todo_list[search_index]['Task']} has been marked as Done.")
            else:
                        print("invalid Task number.\n ")
        except ValueError:
            print("Please Enter a Valid Task Number \n ")
menu()
