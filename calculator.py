def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def operation_symbol(op):
    if op == "Add": return "+"
    if op == "Subtract": return "-"
    if op == "Multiply": return "*"
    if op == "Divide": return "/"
    return ""

import streamlit as st

st.title("Professional Calculator")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("First Number", value=0.0, step=0.1)
with col2:
    num2 = st.number_input("Second Number", value=0.0, step=0.1)

st.markdown("---")
st.header("Select Operation")

operation = st.radio("Choose an operation:", ("Add", "Subtract", "Multiply", "Divide"), horizontal=True)

st.markdown("---")

result = None
if st.button("Calculate", use_container_width=True):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    st.header("Result")
    if result == "Error! Division by zero.":
        st.error(result)
    elif result is not None:
        st.success(f"{num1} {operation_symbol(operation)} {num2} = {result}")

def operation_symbol(op):
    if op == "Add": return "+"
    if op == "Subtract": return "-"
    if op == "Multiply": return "*"
    if op == "Divide": return "/"
    return ""
