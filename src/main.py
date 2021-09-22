# importing necessary modules
from PyQt5 import QtWidgets
from PyQt5 import uic
import sys
import wikipedia

# creating window class
class Window(QtWidgets.QMainWindow):
    # creating the constructor
    def __init__(self):
        # calling the parent constructor
        super().__init__()

        # calling init_window method
        self.init_window()

    # creating init_window method
    def init_window(self):
        # loading the gui
        self.gui = uic.loadUi("Search_ui.ui", self)
        # coonecting a slot to the clicked signal of search button
        self.gui.search_button.clicked.connect(self.search_info)
        # showing the window
        self.show()

    # creating the slot(search_info'method)
    def search_info(self):
        # clearing all data from the output area
        self.gui.output_area.clear()

        if self.gui.search_entry.text()=="":
            self.gui.output_area.append("<p style = 'color: aqua'> You haven't passed any value ! </p>")

        else:

            # trying to search
            try:
                # getting the result from the wikipedia and storing it in a variable
                result = wikipedia.summary(self.gui.search_entry.text())

            # handling the error through except block
            except:
                # trying to append error message in output area
                try:
                    # inserting error message in output area
                    self.gui.output_area.append(f"<p style = 'color: red;'> The result isn't found </p>")

                # handling error
                except:
                    pass
            # else block
            else:
                # inserting the result obtained from wikipedia on the output area
                self.gui.output_area.append(result)

# creating the Application function
def Application():
    # creating QApplication object
    App = QtWidgets.QApplication(sys.argv)
    # creating an instance of Window class 
    window = Window()
    # exit of the window
    sys.exit(App.exec_())

# Main flow
if __name__ == "__main__":
    # calling the Application function
    Application()