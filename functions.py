FILEPATH = "todos.txt"


def get_todos(filepath = FILEPATH): #with a default parameter ("filepath")
    """ Read the text file and the return the list of
    to-do items."""
    with open(filepath, 'r') as file_local:  #Localize the variable in func
        todos = file_local.readlines()
    return todos

def write_todos(todos_arg, filepath = FILEPATH): #non-default parameter before the default one
    """Writes the to-do item list in the text file."""
    with open(filepath, 'w') as file: #alternatively you can explicitly mention the args below in each instance(no need to respect the order then)
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello there")
"""if this very func directly executed the above func returns the print results
Otherwise, if it is imported, __name__ = function
"""
