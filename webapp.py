import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_input = st.session_state["new_todo"] + '\n'
    todos.append(todo_input)
    functions.write_todos(todos)


st.title("To-do App")
#st.subheader("This is my to-do app")
st.subheader("Boost your productivity by keeping track of your todos")
st.text("Use the input box to enter a new todo. "
        "Check the boxes to mark todos as completed")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter a new todo here..",
              on_change=add_todo, key="new_todo")
