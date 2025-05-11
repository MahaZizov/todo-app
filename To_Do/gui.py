import sys

import functions

import FreeSimpleGUI as sg

import time
#in terminal set-executionpolicy remotesigned -scope currentuser
#then instal pyinstaller to create an exe file
#terminal go to cd "to_do"
#terminal: pyinstaller --onefile --clean gui.py --add-data "add.png;." --log-level=DEBUG
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

def resource_path(relative_path):
    """Get absolute path to resource, works for PyInstaller or noraml script"""
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

sg.theme("Dark")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button(size=50, image_source=resource_path("add.png"), mouseover_colors="#D2B48C",
                       tooltip="Add Todo", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

#layout = [[label], [input_box, add_button], [list_box, edit_button, complete_button],
          #[exit_button]]

window = sg.Window('My To-Do App',
                   layout=[[clock],
                          [label],
                          [input_box, add_button],
                          [list_box, edit_button, complete_button],
                          [exit_button]],
                   font=("Helvetica", 20))  #[[label, input_box]]

while True:
    event, values = window.read(timeout=100) #timeout makes sure while loop runs even if no events are detected
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()