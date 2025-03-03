# All the code needed to define interface components

# Widgets are all sorts of interface components
from PyQt5 import QtWidgets as qtw
import sys


# Your application will contain exactly one instance
## of a QApplication object (or derived subclass)
class SayHelloApp(qtw.QApplication):
    """
    Contains a VerticalHelloBox (a class) to prompt
    the user for their name and say hello!
    """

    def __init__(self):
        # Call the constructor for the parent class
        # the one required argument is usually sys.argv
        ## which are command line parameters, but we dont
        ### need any now, hence the empty list
        super().__init__([])

        # Add the VerticalHelloBox
        self.main_widget = VerticalHelloBox()

        # Run the application
        self.main_widget.show()
        sys.exit(self.exec_())
        return


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


class VerticalHelloBox(WindowWithVerticalSlots):
    """
    Contains a text box and a button the user
    can press which opens another window for
    them to enter their name
    """

    def __init__(self):
        super().__init__(title="Example Interface using PyQt5")
        self.configure()
        return

    def configure(self) -> None:
        self.greeting_box = qtw.QLabel(self)  # belongs to me
        self.hello_button = qtw.QPushButton("Who are you?", self)

        # Bind the button to a function, so that when the button is
        ## pressed, the function is called
        self.hello_button.clicked.connect(self.hello_button_clicked)

        # Add the two objects to the layout
        self.my_layout.addWidget(self.greeting_box)
        self.my_layout.addWidget(self.hello_button)
        return None

    def hello_button_clicked(self) -> None:
        # Create a new InputPopup
        name_getter = InputPopup("Your name:")

        # Run the dialog box and wait for the user to click the button
        if name_getter.exec_() == qtw.QDialog.Accepted:
            # Set the text in the main window to whatever the user input
            self.greeting_box.setText(f"Hello {name_getter.get_text()}!")
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
