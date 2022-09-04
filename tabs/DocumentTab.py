import datetime
from datetime import date

from formatting_helper import format_date
from ui.UiMainWindow import UiMainWindow
from babel.dates import format_datetime


class DocumentTab(UiMainWindow):
    context: dict

    def setupUi(self, main_window):
        UiMainWindow.setupUi(self, main_window)

    def get_context(self) -> dict:
        context = dict()
        contract_date = date.today() if self.contract_date.currentIndex() == 0 \
            else date.today() + datetime.timedelta(days=1)
        context['contract_date'] = format_date(contract_date, "plain")
        context['contract_date_dots'] = format_date(contract_date, "dots")
        context['contract_date_ua'] = format_date(contract_date, "ua")
        context['contract_number'] = self.contract_number.value()
        context['odesa_date'] = format_date(self.odesa_date.date(), "dots")
        context['dollar_rate'] = self.dollar_rate.value()

        return context
