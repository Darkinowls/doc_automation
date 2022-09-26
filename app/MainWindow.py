from PyQt5.QtWidgets import QFileDialog, QMessageBox

from app.helpers import models_helper, dollar_rate_helper
from app.components.ContextMaker import ContextMaker
from app.components.DocumentMaker import DocumentMaker
from ui.UiMainWindow import UiMainWindow


# Mediator
class MainWindow:
    __ui_main_window: UiMainWindow
    __context_maker: ContextMaker
    __document_maker: DocumentMaker

    def __init__(self):
        self.__ui_main_window = UiMainWindow()
        self.__context_maker = ContextMaker(self.__ui_main_window)

    def setup_ui(self, main_window):
        self.__ui_main_window.setupUi(main_window)
        self.__modify_ui_with_outside_data()
        self.__ui_main_window.done_button.clicked.connect(self.__make_documents)

    def __modify_ui_with_outside_data(self):
        models_helper.set_models(self.__ui_main_window.model)
        self.__ui_main_window.dollar_rate.setValue(dollar_rate_helper.get_average_sell_dollar_rate())

    def __make_documents(self):
        folder_path = QFileDialog.getExistingDirectory(
            None, "Виберіть папку для створення нової папки з документами")
        if not folder_path:
            return
        self.__document_maker = DocumentMaker(self.__context_maker.make_context())
        folder_path = self.__document_maker.make_documents_in_folder(folder_path)
        if folder_path:
            self.message_information()

    def message_information(self):
        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setText("Документи створені!")
        message.setWindowTitle('Повідомлення')
        message.setStandardButtons(QMessageBox.Ok)
        return message.exec()
