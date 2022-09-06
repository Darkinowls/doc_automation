import datetime
import num2words
from app.formatting_helper import format_checked, format_date, format_settle_type, format_pib
from ui.UiMainWindow import UiMainWindow


class ContextMaker:

    def __init__(self, single_ui: UiMainWindow):
        self.__context = dict()
        self.__single_ui = single_ui

    def __get_context_customer(self) -> dict[str]:
        self.__context['area'] = format_checked(self.__single_ui.area.text(), self.__single_ui.area.text() + " р-н.")
        self.__context['date_birth'] = format_date(self.__single_ui.date_birth.date().toPyDate(), "dots")
        self.__context['phone'] = self.__single_ui.phone.text()
        self.__context['pib_buyer_dots'] = format_pib(self.__single_ui.pib_buyer.text())
        self.__context['pib_buyer'] = self.__single_ui.pib_buyer.text()
        self.__context['pib_receiver'] = self.__single_ui.pib_receiver.text()
        self.__context['region'] = format_checked(self.__single_ui.region.text(),
                                                  self.__single_ui.region.text() + " обл.")
        self.__context['settle_name'] = self.__single_ui.settle_name.text()
        self.__context['settle_type'] = format_settle_type(
            self.__single_ui.settle_type.itemText(self.__single_ui.settle_type.currentIndex()))
        self.__context['street'] = self.__single_ui.street.text()
        return self.__context

    def __get_context_document(self) -> dict[str]:
        contract_date = datetime.date.today() if self.__single_ui.contract_date.currentIndex() == 0 \
            else datetime.date.today() + datetime.timedelta(days=1)
        self.__context['contract_date'] = format_date(contract_date, "plain")
        self.__context['contract_date_dots'] = format_date(contract_date, "dots")
        self.__context['contract_date_ua'] = format_date(contract_date, "ua")
        self.__context['contract_number'] = self.__single_ui.contract_number.value()
        self.__context['odesa_date'] = format_date(self.__single_ui.odesa_date.date().toPyDate(), "dots")
        self.__context['dollar_rate'] = self.__single_ui.dollar_rate.value()
        self.__context['unload_num'] = self.__single_ui.unload.value()
        self.__context['unload_words'] = num2words.num2words(self.__single_ui.unload.value(), lang='uk')
        return self.__context

    def __get_context_good(self) -> dict[str]:
        self.__context['advance'] = self.__single_ui.advance.isChecked()
        self.__context['alarm'] = format_checked(self.__single_ui.alarm.isChecked(), "Сигналізація")
        self.__context['battery_type'] = self.__single_ui.battery_type.currentText()
        self.__context['capacity'] = self.__single_ui.capacity.text()
        self.__context['charger'] = format_checked(self.__single_ui.charger.isChecked(), "Зарядний пристрій")
        self.__context['color'] = self.__single_ui.color.text()
        self.__context['free_delivery'] = format_checked(self.__single_ui.alarm.isChecked(), "безкоштовна")
        self.__context['lamp'] = format_checked(self.__single_ui.alarm.isChecked(), "Габаритні ліхтарі")
        self.__context['mirror'] = format_checked(self.__single_ui.mirror.isChecked(), "Дзеркало заднього виду")
        self.__context['model'] = self.__single_ui.model.currentText()
        self.__context['shortname'] = self.__single_ui.model.currentText().split("Elwinn ")[1]
        self.__context['power'] = self.__single_ui.power.text()
        self.__context['warranty'] = format_checked(self.__single_ui.warranty.isChecked(),
                                                    "Гарантія 12 місяців (двигун, акумулятор, контролер)")
        self.__context['price'] = self.__single_ui.price.value()
        return self.__context

    def __calculate_money(self) -> dict:
        self.__context['true_price'] = round(self.__context['price'] * 1.1, 2)
        self.__context['true_price_uah'] = round(self.__context['true_price'] * self.__context['dollar_rate'], 2)
        self.__context['true_price_10'] = round(self.__context['true_price'] * 0.1, 2)
        self.__context['true_price_10_uah'] = round(self.__context['true_price_uah'] * 0.1, 2)
        self.__context['true_price_90'] = round(self.__context['true_price'] * 0.9, 2)
        self.__context['true_price_90_uah'] = round(self.__context['true_price_uah'] * 0.9, 2)
        return self.__context

    def make_context(self) -> dict[str]:
        self.__context = self.__get_context_good()
        self.__context.update(self.__get_context_customer())
        self.__context.update(self.__get_context_document())
        self.__context = self.__calculate_money()
        return self.__context
