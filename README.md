# PyConText

PyConText is a Python package for displaying text in the console with format and give console cursor control.
**Note: It is windows-only**

## Dependencies

PyConText requires the following modules:
- os
- shutil
- keyboard
- ctypes (and wintypes)

## Installation
Install the either without examples or with examples(source code) from the releases page.
Add the PyConText.py file to your project folder and import it like this:
```python
import PyConText
```

## Console Functions

### get_size()

Returns the size of the terminal as a named tuple of two integers, columns and lines.

*Parameters*
None

*Returns*
collections.namedtuple
- A named tuple of two integers, columns and lines.

### clear()

Clears the console screen.

*Parameters*
None

*Returns*
None

## Cursor Functions

### move(x:int=0, y:int=0)
Moves the cursor to a given position

*Parameters*
x : int
- The x position of the cursor starting from 0
y : int
- The y position of the cursor starting from 0

*Returns*
None

### get_cursor_position()

Requests the current position of the cursor from the terminal and returns it as a tuple of two integers, the row and column of the cursor.

*Parameters*
None

*Returns*
tuple
- A named tuple of two integers, the row and column of the cursor. If the operation is unsupported returns None.

## Widget Functions

### input(prompt: str, end: str = ": ", erase: bool = True)

Reads input from the user and returns it as a string.

*Parameters*
prompt : str
- The text to display to the user before reading input
end : str
- The string to append to the end of the prompt, defaults to ": "
erase : bool
- Whether to erase the input line after reading, defaults to True

*Returns*
str
- The input from the user as a string

### radio(options: list, selection_character: chr = "*", unselection_character: chr = " ")

Creates a radio button menu from a given list of options

*Parameters*
options : list
- A list of strings to be used as the options
selection_character : chr
- The character to use to mark the selected option, defaults to "*"
unselection_character : chr
- The character to use to mark the unselected options, defaults to " "

*Returns*
str
- The selected option as a string

### output(output, alignment="left")
Outputs the given string or list of strings to the console, with optional alignment

*Parameters*
output : str or list
- The string or list of strings to output
- If it is a list, each element will be printed on a new line
alignment : str
- The alignment of the output, either "left", "center", or "right". Defaults to "left"

*Returns*
None

