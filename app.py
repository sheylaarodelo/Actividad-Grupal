import streamlit as st

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir por cero"
    return a / b

st.title("Calculadora Básica")

num1 = st.number_input("Ingrese el primer número", value=0.0)
num2 = st.number_input("Ingrese el segundo número", value=0.0)

operacion = st.selectbox("Seleccione la operación", ["Sumar", "Restar", "Multiplicar", "Dividir"])

if st.button("Calcular"):
    if operacion == "Sumar":
        resultado = sumar(num1, num2)
    elif operacion == "Restar":
        resultado = restar(num1, num2)
    elif operacion == "Multiplicar":
        resultado = multiplicar(num1, num2)
    elif operacion == "Dividir":
        resultado = dividir(num1, num2)

    st.write("Resultado:", resultado)