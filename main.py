import sys

from PyQt5 import QtWidgets

from app.MainWindow import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec_())
