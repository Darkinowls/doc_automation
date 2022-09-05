import os
from docxtpl import DocxTemplate
from docx2pdf import convert


class DocumentMaker:
    __context: dict
    __folder_path: str
    __unique_name: str

    def __init__(self, context: dict, ):
        self.__context = context

    def make_documents_in_folder(self, path: str) -> str:
        self.__folder_path = path
        self.__make_folder()
        self.__render_docx()
        return self.__folder_path

    def __make_folder(self):
        self.__unique_name = self.__context['model'] + " " + self.__context['pib_buyer'] + " " + self.__context[
            'settle_type'] + " " + self.__context['settle_name']
        self.__folder_path = self.__folder_path + '/' + self.__unique_name
        os.mkdir(self.__make_unique_folder_name())

    def __make_unique_folder_name(self):
        if not os.path.exists(self.__folder_path):
            return self.__folder_path
        i = 1
        while os.path.exists(self.__folder_path + '_' + str(i)):
            i += 1
        return self.__folder_path + '_' + str(i)

    def __render_docx(self):
        doc = DocxTemplate("templates/Template.docx")
        doc.render(self.__context)
        document_name = self.__folder_path + '/' + self.__unique_name + ".docx"
        doc.save(document_name)
        convert(document_name)

    def __render_excel(self):
        pass
