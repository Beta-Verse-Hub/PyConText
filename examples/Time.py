# Import required modules
import PyConText
import keyboard
import time

# Clear the console
PyConText.Console.clear()

# Loop until the escape key is pressed
while not keyboard.is_pressed("esc"):
    PyConText.Cursor.move(0, 0) # Move the cursor to the top left
    PyConText.Widget.output(f"Current time: {time.strftime('%H:%M:%S')}", alignment="center") # Output the current time
    time.sleep(0.01) # Wait for 1 second
