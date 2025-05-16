import streamlit as st
import functions

todos = functions.get_todos()

st.title("Todo App")
#terminal: streamlit run web_app.py
st.subheader("This is the Todo app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)


st.text_input(label="Enter a todo:", placeholder="Add new todo...") #or an empty string