import streamlit as st
import functions


if "todos" not in st.session_state:
    st.session_state.todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"]
    if new_todo:
        st.session_state.todos.append(new_todo)
        functions.write_todos(st.session_state.todos)
        st.session_state["new_todo"] = ""

todos = functions.get_todos()

st.title("Todo App")
#terminal: streamlit run C:\Users\maham\PycharmProjects\ArditSulce\To_Do\web_app.py
st.subheader("This is the Todo app")
st.write("This app is to increase your productivity")

for todo in st.session_state.todos:
    st.checkbox(todo, key=todo)



st.text_input(label="Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo") #or an empty string