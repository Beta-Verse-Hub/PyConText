# Import required modules
import PyConText

# Define operations
operations = ["Addition", "Subtraction", "Multiplication", "Division"]

# Clear the console
PyConText.Console.clear()

# Get two numbers
a = PyConText.Widget.input("Enter the first number")
b = PyConText.Widget.input("Enter the second number")

# Get the operation
operation = PyConText.Widget.radio(operations)

if operation == "Addition":
    PyConText.Widget.output([f"{a} + {b}",f"= {int(a) + int(b)}"], alignment="center") # Add the two numbers
if operation == "Subtraction":
    PyConText.Widget.output([f"{a} - {b}",f"= {int(a) - int(b)}"], alignment="center") # Subtract the two numbers
if operation == "Multiplication":
    PyConText.Widget.output([f"{a} * {b}",f"= {int(a) * int(b)}"], alignment="center") # Multiply the two numbers
if operation == "Division":
    PyConText.Widget.output([f"{a} / {b}",f"= {int(a) / int(b)}"], alignment="center") # Divide the two numbers
