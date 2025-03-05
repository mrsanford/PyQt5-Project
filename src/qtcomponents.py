# All the code needed to define interface components

# Widgets are all sorts of interface components
from typing import Callable
from PyQt5 import QtWidgets as qtw
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg


class WindowWithVerticalSlots(qtw.QWidget):
    """
    A window with a title and an empty
    vertical container (QVBoxLayout).
    Intended use of this class is to
    inherit and extend
    """

    def __init__(self, title: str):
        super().__init__()
        # Set the window title
        self.setWindowTitle(title)

        # Create an empty vertical layout container
        self.my_layout = qtw.QVBoxLayout(self)
        # will tell it its a child belonging to the window
        return


class WindowWithFigureAbove(WindowWithVerticalSlots):
    """
    A window with a vertical latyout and matplotlib figure above.
    """

    def __init__(self, fig: plt.figure, title: str = "Window with a Figure"):
        super().__init__(title=title)

        # Put the figure into a canvas
        self.canvas = FigureCanvasQTAgg(fig)
        # We already generate a figure when we pass this into the constructor
        # Add that to the layout
        self.my_layout.addWidget(self.canvas)
        return


class ButtonRow(qtw.QHBoxLayout):
    """
    A row of buttons. Names must be provided for each button.
    """

    # btw: don't create two buttons with the same name
    def __init__(self, names: list[str]):
        super().__init__()
        self.buttons = []
        for name in names:
            self.buttons.append(qtw.QPushButton(name))  # the name of the button
            self.addWidget(self.buttons[-1])
        return


class ButtonBox(qtw.QVBoxLayout):
    """
    A vertical container of ButtonRow objects.
    Specify nrows and ncols when creating.
    """

    def __init__(self, nrows: int, ncols: int):
        super().__init__()

        self.rows = []
        for _ in range(nrows):
            names = [str(n) for n in range(ncols)]
            self.row.append(ButtonRow(names))
            self.addLayout(self.rows[-1])
        return


def configure_button(button: qtw.QPushButton, text: str, command: Callable):
    button.setText(text)
    button.clicked.connect(command)
    return None


class InputPopup(qtw.QDialog):
    """
    A popup window with a text box and
    an OK button to allow the user to enter
    freeform text.
    """

    def __init__(self, title: str):
        super().__init__()
        self.setWindowTitle(title)

        # Place to enter some text
        self.text_entry = qtw.QLineEdit(self)  # belongs to me

        # OK button to click
        self.ok_button = qtw.QPushButton("Ok", self)

        # When the button is clicked, it calls the accept method
        # of the QDialog, which lets the application know that
        ## the interaction with the dialog is complete
        self.ok_button.clicked.connect(self.accept)

        # Create a vertical layout and add the widgets
        self.my_layout = qtw.QVBoxLayout(self)
        # Can change and use the class if preferred
        self.my_layout.addWidget(self.text_entry)
        self.my_layout.addWidget(self.ok_button)
        return

    # Gets the text back from the textbox to put back on the welcome box
    def get_text(self) -> str:
        return self.text_entry.text()
