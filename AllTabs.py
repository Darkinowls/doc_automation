from docxtpl import DocxTemplate

from tabs.CustomerTab import CustomerTab
from tabs.DocumentTab import DocumentTab
from tabs.GoodTab import GoodTab


class AllTabs(CustomerTab, DocumentTab, GoodTab):
    context: dict[str]

    def setupUi(self, main_window):
        CustomerTab.setupUi(self, main_window)
        DocumentTab.setupUi(self, main_window)
        GoodTab.setupUi(self, main_window)
        self.done_button.clicked.connect(self.make_documents)

    def make_documents(self):
        doc = DocxTemplate("templates/Template.docx")
        context = self.__get_context()
        doc.render(context)
        doc.save("output/generated_doc.docx")

    def __get_context(self) -> dict[str]:
        context = CustomerTab.get_context(self)
        context.update(DocumentTab.get_context(self))
        context.update(GoodTab.get_context(self))
        return context
