import os
from docxtpl import InlineImage
from PyQt5.QtWidgets import QComboBox
from docx.shared import Mm

MODEL_SRC = "model_src"


def load_models():
    names: list[str] = list()
    for filename in os.listdir(MODEL_SRC):
        names.append(filename)
    return names


def set_models(combo_box: QComboBox):
    names = load_models()
    for i in range(len(names)):
        combo_box.addItem(names[i][0:-4])


def get_model_image(doc, name: str) -> InlineImage:
    return InlineImage(doc, image_descriptor=MODEL_SRC + "/" + name + ".jpg", width=Mm(105), height=Mm(90))
