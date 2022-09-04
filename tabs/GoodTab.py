from formatting_helper import format_checked
from ui.UiMainWindow import UiMainWindow


class GoodTab(UiMainWindow):

    def setupUi(self, main_window):
        UiMainWindow.setupUi(self, main_window)

    def get_context(self) -> dict[str]:
        context = dict()
        context['advance'] = self.advance.isChecked()
        context['alarm'] = format_checked(self.alarm.isChecked(), "Сигналізація.")
        context['battery_type'] = self.battery_type.currentText()
        context['capacity'] = self.capacity.text()
        context['charger'] = format_checked(self.charger.isChecked(), "Зарядний пристрій.")
        context['color'] = self.color.text()
        context['free_delivery'] = format_checked(self.alarm.isChecked(), "безкоштовна")
        context['lamp'] = format_checked(self.alarm.isChecked(), "Габаритні ліхтарі.")
        context['mirror'] = format_checked(self.mirror.isChecked(), "Дзеркало заднього виду.")
        context['model'] = self.model.text()
        context['name'] = self.name.text()
        context['power'] = self.power.text()
        context['warranty'] = format_checked(self.warranty.isChecked(),
                                             "Гарантія 12 місяців (двигун, акумулятор, контролер).")

        context['price'] = self.price.value()
        return context
