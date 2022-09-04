import sys

from PyQt5 import QtWidgets

from AllTabs import AllTabs

# from ui.UiMainWindow import UiMainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = AllTabs()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
