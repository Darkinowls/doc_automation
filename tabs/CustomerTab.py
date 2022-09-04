from formatting_helper import format_settle_type, format_pib, format_date, format_checked
from ui.UiMainWindow import UiMainWindow


class CustomerTab(UiMainWindow):

    def setupUi(self, main_window):
        UiMainWindow.setupUi(self, main_window)

    def get_context(self) -> dict[str]:
        context = dict()
        context['area'] = format_checked(self.area.text(), self.area.text() + " р-н.,")
        context['date_birth'] = format_date(self.date_birth.date().toPyDate(), "dots")
        context['phone'] = self.phone.text()
        context['pib_buyer_dots'] = format_pib(self.pib_buyer.text())
        context['pib_buyer'] = self.pib_buyer.text()
        context['pib_receiver'] = self.pib_receiver.text()
        context['region'] = format_checked(self.region.text(), self.region.text() + " обл.,")
        context['settle_name'] = self.settle_name.text() + ","
        context['settle_type'] = format_settle_type(self.settle_type.itemText(self.settle_type.currentIndex()))
        context['street'] = self.street.text()
        return context
