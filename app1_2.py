from functions import get_todos, write_todos
import time
#you can also just "import functions". Then every time you call a function, do as methods: eg functions.get_todos()
text = """
Principles of productivity:
Managing you inflow.
Systemizing everything that repeats and whatnot
"""
print(text)
current_time = time.strftime("%d/%b/%Y_%H:%M:%S")
print("it is", current_time)
while True:
    #Get user input & strip space chars
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
#Shift+Tab unindent an entire block
    if user_action.startswith("add"):
        ##r"todo = input("enter a todo: ") + "\n"
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')
        #below, write todos in a file&close file

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")

        #new_todos = [item.strip("\n") for item in todos] #(A)list comprehension to get rid of the \n in added lines

        for index, item in enumerate(todos):
            item = item.strip('\n') #(B) if (A) used, delete this line
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)
        except ValueError:
            print("Bro, enter the number of the member you want to edit for fuck's sake.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number -1
            todo_to_remove = todos[index].strip('\n') #to get rid of space after the char

            todos.pop(index)

            write_todos(todos)
            message = f"Todo {todo_to_remove} has been removed from the list"
            print(message)
        except IndexError:
            print("Index value out of range")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid command")

print("Bye")