# All the code needed to define interface components

# Widgets are all sorts of interface components
from PyQt5 import QtWidgets as qtw

# Your application will contain exactly one instance
## of a QApplication object (or derived subclass)
# class SayHelloApp(qtw.QApplication):
#     """
#     Contains a VerticalHelloBox (a class) to prompt
#     the user for their name and say hello!
#     """

#     def __init__(self):
#         # Call the constructor for the parent class
#         # the one required argument is usually sys.argv
#         ## which are command line parameters, but we dont
#         ### need any now, hence the empty list
#         super().__init__([])

#         # Add the VerticalHelloBox
#         self.main_widget = VerticalHelloBox()

#         # Run the application
#         self.main_widget.show()
#         sys.exit(self.exec_())
#         return


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
