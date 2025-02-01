



import tkinter as tk
from tkinter import ttk

# Función para formatear números con comas
def format_number(number):
    try:
        if "." in number:  # Mantener decimales si existen
            integer_part, decimal_part = number.split(".")
            return "{:,}".format(int(integer_part)) + "." + decimal_part
        return "{:,}".format(int(number))
    except ValueError:
        return number  # Si no es número válido, devolver como está

# Manejo de la entrada de números
def button_click(number):
    current = entry.get().replace(",", "")  # Quitar comas antes de procesar
    if number == "." and "." in current.split()[-1]:  # Evitar múltiples puntos en un número
        return
    new_value = current + str(number)
    entry.delete(0, tk.END)
    entry.insert(tk.END, format_number(new_value))  # Volver a formatear con comas

# Borrar todo
def button_clear():
    entry.delete(0, tk.END)

# Borrar un solo carácter (retroceso)
def button_backspace():
    current = entry.get().replace(",", "")
    if current:
        new_value = current[:-1]  # Quitar último carácter
        entry.delete(0, tk.END)
        entry.insert(tk.END, format_number(new_value))  # Formatear con comas

# Manejo de operadores
def button_operator(operator):
    current = entry.get().replace(",", "")
    if current and current[-1] not in "+-*/":  # Evitar operadores repetidos
        entry.insert(tk.END, operator)

# Evaluar la operación
def button_equal():
    try:
        expression = entry.get().replace(",", "")  # Quitar comas antes de evaluar
        result = eval(expression)  # Calcular resultado
        entry.delete(0, tk.END)
        entry.insert(tk.END, format_number(str(result)))  # Formatear con comas
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Crear ventana principal
root = tk.Tk()
root.title("Calculadora")
root.configure(background="lightblue")
root.geometry("400x600")  # Tamaño de la ventana

# Crear cuadro de entrada
entry = ttk.Entry(root, font=("Helvetica", 24), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Crear estilo para los botones
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 20), padding=10)

# Crear botones numéricos
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text in '0123456789.':
        button = ttk.Button(root, text=text, command=lambda t=text: button_click(t))
    elif text in '/*-+':
        button = ttk.Button(root, text=text, command=lambda t=text: button_operator(t))
    elif text == '=':
        button = ttk.Button(root, text=text, command=button_equal)
    button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

# Botones de limpiar y retroceso
button_clear = ttk.Button(root, text='C', command=button_clear)
button_clear.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

button_backspace = ttk.Button(root, text='←', command=button_backspace)
button_backspace.grid(row=5, column=1, padx=10, pady=10, sticky="nsew")

# Ajustar el tamaño de las columnas y filas
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Correr la aplicación
root.mainloop()
