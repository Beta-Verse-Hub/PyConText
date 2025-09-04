import os
import shutil

screen = []
screen_width = 0
screen_height = 0

def init(width=shutil.get_terminal_size().columns, height=shutil.get_terminal_size().lines, main_char="[]"):
    """
    Initializes the screen with a given width and height, and fills it with
    a given character.

    Parameters
    ----------
    width : int
        The width of the screen in characters
    height : int
        The height of the screen in lines
    main_char : str
        The character to fill the screen with, defaults to "[]"
    """
    global screen, screen_width, screen_height

    Console.clear()

    screen_width = width
    screen_height = height

    for y in range(height):
        screen.append([])
        for x in range(width):
            screen[y].append(main_char)

class Console():

    @staticmethod
    def get_size():
        """
        Returns the size of the terminal in characters as a tuple of (width, height)
        
        Parameters
        ----------
        None

        Returns
        -------
        tuple
        """
        return shutil.get_terminal_size()

    @staticmethod
    def clear():
        """
        Clears the console screen

        This function works by checking the current operating system and calling the
        relevant command to clear the screen. If the operating system is Windows, it
        calls "cls". If the operating system is not Windows, it calls "clear".

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        os.system("cls" if os.name == "nt" else "clear")

class Cursor():

    @staticmethod
    def move_to_start():
        """
        Moves the cursor to the start of the current line

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        print("\033[H", end="")