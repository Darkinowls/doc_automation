from PyQt5.QtWidgets import QDateEdit
from datetime import date
from babel.dates import format_datetime


def format_settle_type(settle_type) -> str:
    if settle_type == "Смт":
        return "смт."
    if settle_type == "Місто":
        return "м."
    if settle_type == "Село":
        return "с."


def format_pib(pib: str) -> str:
    words: list = pib.split(" ")
    return words[0] + words[1][0] + words[2][0]


def format_date(wild_date: date, format_type: str) -> str:
    if format_type == "dots":
        return wild_date.strftime("%d.%m.%Y")
    if format_type == "ua":
        return format_datetime(wild_date, format="d MMMM Y", locale="uk_UA")
    if format_type == "plain":
        return wild_date.strftime("%d%m%Y")


def format_checked(checked: bool, name: str) -> str:
    return name if checked else ""



