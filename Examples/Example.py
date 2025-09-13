import PyConText

operations = ["Addition", "Subtraction", "Multiplication", "Division"]

PyConText.Console.clear()
a = PyConText.Widget.input("Enter the first number")
b = PyConText.Widget.input("Enter the second number")

operation = PyConText.Widget.radio(operations)

if operation == "Addition":
    PyConText.Widget.output([f"{a} + {b}",f"= {int(a) + int(b)}"], alignment="center")
if operation == "Subtraction":
    PyConText.Widget.output([f"{a} - {b}",f"= {int(a) - int(b)}"], alignment="center")
if operation == "Multiplication":
    PyConText.Widget.output([f"{a} * {b}",f"= {int(a) * int(b)}"], alignment="center")
if operation == "Division":
    PyConText.Widget.output([f"{a} / {b}",f"= {int(a) / int(b)}"], alignment="center")