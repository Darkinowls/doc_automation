# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 571)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 541))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.pib_buyer = QtWidgets.QLineEdit(self.tab_1)
        self.pib_buyer.setGeometry(QtCore.QRect(150, 50, 321, 38))
        self.pib_buyer.setObjectName("pib_buyer")
        self.label = QtWidgets.QLabel(self.tab_1)
        self.label.setGeometry(QtCore.QRect(40, 60, 121, 24))
        self.label.setObjectName("label")
        self.date_birth = QtWidgets.QDateEdit(self.tab_1)
        self.date_birth.setGeometry(QtCore.QRect(260, 120, 111, 38))
        self.date_birth.setDateTime(QtCore.QDateTime(QtCore.QDate(1979, 3, 23), QtCore.QTime(0, 0, 0)))
        self.date_birth.setCalendarPopup(True)
        self.date_birth.setObjectName("date_birth")
        self.label_2 = QtWidgets.QLabel(self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 211, 24))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_1)
        self.label_3.setGeometry(QtCore.QRect(40, 200, 81, 24))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_1)
        self.label_4.setGeometry(QtCore.QRect(410, 200, 181, 24))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_1)
        self.label_5.setGeometry(QtCore.QRect(40, 270, 51, 24))
        self.label_5.setObjectName("label_5")
        self.pib_receiver = QtWidgets.QLineEdit(self.tab_1)
        self.pib_receiver.setGeometry(QtCore.QRect(180, 400, 291, 38))
        self.pib_receiver.setObjectName("pib_receiver")
        self.area = QtWidgets.QLineEdit(self.tab_1)
        self.area.setGeometry(QtCore.QRect(100, 260, 271, 38))
        self.area.setObjectName("area")
        self.label_6 = QtWidgets.QLabel(self.tab_1)
        self.label_6.setGeometry(QtCore.QRect(410, 270, 91, 24))
        self.label_6.setObjectName("label_6")
        self.settle_name = QtWidgets.QLineEdit(self.tab_1)
        self.settle_name.setGeometry(QtCore.QRect(500, 260, 251, 38))
        self.settle_name.setObjectName("settle_name")
        self.label_7 = QtWidgets.QLabel(self.tab_1)
        self.label_7.setGeometry(QtCore.QRect(410, 130, 141, 24))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_1)
        self.label_8.setGeometry(QtCore.QRect(40, 410, 161, 24))
        self.label_8.setObjectName("label_8")
        self.phone = QtWidgets.QLineEdit(self.tab_1)
        self.phone.setGeometry(QtCore.QRect(560, 120, 191, 38))
        self.phone.setObjectName("phone")
        self.label_9 = QtWidgets.QLabel(self.tab_1)
        self.label_9.setGeometry(QtCore.QRect(40, 340, 201, 24))
        self.label_9.setObjectName("label_9")
        self.street = QtWidgets.QLineEdit(self.tab_1)
        self.street.setGeometry(QtCore.QRect(250, 330, 321, 38))
        self.street.setObjectName("street")
        self.region = QtWidgets.QLineEdit(self.tab_1)
        self.region.setGeometry(QtCore.QRect(120, 190, 251, 38))
        self.region.setObjectName("region")
        self.settle_type = QtWidgets.QComboBox(self.tab_1)
        self.settle_type.setGeometry(QtCore.QRect(600, 190, 151, 38))
        self.settle_type.setObjectName("settle_type")
        self.settle_type.addItem("")
        self.settle_type.addItem("")
        self.settle_type.addItem("")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(40, 60, 91, 24))
        self.label_14.setObjectName("label_14")
        self.name = QtWidgets.QLineEdit(self.tab_2)
        self.name.setGeometry(QtCore.QRect(140, 50, 281, 38))
        self.name.setObjectName("name")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(480, 60, 121, 24))
        self.label_15.setObjectName("label_15")
        self.model = QtWidgets.QLineEdit(self.tab_2)
        self.model.setGeometry(QtCore.QRect(610, 50, 141, 38))
        self.model.setObjectName("model")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(40, 130, 91, 24))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(390, 130, 171, 24))
        self.label_17.setObjectName("label_17")
        self.power = QtWidgets.QLineEdit(self.tab_2)
        self.power.setGeometry(QtCore.QRect(140, 120, 191, 38))
        self.power.setObjectName("power")
        self.capacity = QtWidgets.QLineEdit(self.tab_2)
        self.capacity.setGeometry(QtCore.QRect(570, 120, 181, 38))
        self.capacity.setObjectName("capacity")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(40, 200, 91, 24))
        self.label_18.setObjectName("label_18")
        self.battery_type = QtWidgets.QComboBox(self.tab_2)
        self.battery_type.setGeometry(QtCore.QRect(120, 190, 191, 38))
        self.battery_type.setObjectName("battery_type")
        self.battery_type.addItem("")
        self.battery_type.addItem("")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(360, 200, 61, 24))
        self.label_19.setObjectName("label_19")
        self.color = QtWidgets.QLineEdit(self.tab_2)
        self.color.setGeometry(QtCore.QRect(420, 190, 191, 38))
        self.color.setObjectName("color")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(40, 270, 381, 24))
        self.label_20.setObjectName("label_20")
        self.price = QtWidgets.QSpinBox(self.tab_2)
        self.price.setGeometry(QtCore.QRect(420, 260, 171, 38))
        self.price.setMaximum(500000)
        self.price.setProperty("value", 1500)
        self.price.setObjectName("price")
        self.free_delivery = QtWidgets.QCheckBox(self.tab_2)
        self.free_delivery.setGeometry(QtCore.QRect(40, 330, 211, 28))
        self.free_delivery.setChecked(True)
        self.free_delivery.setObjectName("free_delivery")
        self.warranty = QtWidgets.QCheckBox(self.tab_2)
        self.warranty.setGeometry(QtCore.QRect(40, 370, 211, 28))
        self.warranty.setChecked(True)
        self.warranty.setTristate(False)
        self.warranty.setObjectName("warranty")
        self.advance = QtWidgets.QCheckBox(self.tab_2)
        self.advance.setGeometry(QtCore.QRect(40, 410, 251, 28))
        self.advance.setObjectName("advance")
        self.lamp = QtWidgets.QCheckBox(self.tab_2)
        self.lamp.setGeometry(QtCore.QRect(310, 330, 211, 28))
        self.lamp.setChecked(True)
        self.lamp.setObjectName("lamp")
        self.alarm = QtWidgets.QCheckBox(self.tab_2)
        self.alarm.setGeometry(QtCore.QRect(310, 370, 211, 28))
        self.alarm.setChecked(True)
        self.alarm.setObjectName("alarm")
        self.charger = QtWidgets.QCheckBox(self.tab_2)
        self.charger.setGeometry(QtCore.QRect(530, 330, 211, 28))
        self.charger.setChecked(True)
        self.charger.setObjectName("charger")
        self.mirror = QtWidgets.QCheckBox(self.tab_2)
        self.mirror.setGeometry(QtCore.QRect(530, 370, 231, 28))
        self.mirror.setChecked(True)
        self.mirror.setObjectName("mirror")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(40, 60, 211, 24))
        self.label_10.setObjectName("label_10")
        self.contract_date = QtWidgets.QComboBox(self.tab)
        self.contract_date.setGeometry(QtCore.QRect(250, 50, 121, 38))
        self.contract_date.setObjectName("contract_date")
        self.contract_date.addItem("")
        self.contract_date.addItem("")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(40, 140, 141, 24))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(40, 290, 321, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(40, 220, 51, 24))
        self.label_13.setObjectName("label_13")
        self.dollar_rate = QtWidgets.QDoubleSpinBox(self.tab)
        self.dollar_rate.setGeometry(QtCore.QRect(90, 210, 161, 38))
        self.dollar_rate.setPrefix("")
        self.dollar_rate.setMaximum(199.99)
        self.dollar_rate.setProperty("value", 40.0)
        self.dollar_rate.setObjectName("dollar_rate")
        self.contract_number = QtWidgets.QSpinBox(self.tab)
        self.contract_number.setGeometry(QtCore.QRect(180, 130, 56, 38))
        self.contract_number.setMinimum(1)
        self.contract_number.setObjectName("contract_number")
        self.odesa_date = QtWidgets.QDateEdit(self.tab)
        self.odesa_date.setGeometry(QtCore.QRect(370, 280, 131, 38))
        self.odesa_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 12, 1), QtCore.QTime(0, 0, 0)))
        self.odesa_date.setCalendarPopup(True)
        self.odesa_date.setDate(QtCore.QDate(2022, 12, 1))
        self.odesa_date.setObjectName("odesa_date")
        self.done_button = QtWidgets.QPushButton(self.tab)
        self.done_button.setGeometry(QtCore.QRect(40, 360, 711, 81))
        self.done_button.setObjectName("done_button")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 36))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pib_buyer.setText(_translate("MainWindow", "Голосіїв Петро Іванович"))
        self.pib_buyer.setPlaceholderText(_translate("MainWindow", "Голосіїв Петро Іванович"))
        self.label.setText(_translate("MainWindow", "ПІБ покупця"))
        self.date_birth.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.label_2.setText(_translate("MainWindow", "Дата народження покупця"))
        self.label_3.setText(_translate("MainWindow", "Область"))
        self.label_4.setText(_translate("MainWindow", "Тип населеного пункту"))
        self.label_5.setText(_translate("MainWindow", "Район"))
        self.pib_receiver.setText(_translate("MainWindow", "Терновик Степан Ігорович"))
        self.pib_receiver.setPlaceholderText(_translate("MainWindow", "Терновик Степан Ігорович"))
        self.area.setText(_translate("MainWindow", "Горолівський"))
        self.area.setPlaceholderText(_translate("MainWindow", "Горолівський"))
        self.label_6.setText(_translate("MainWindow", "Назва н.п."))
        self.settle_name.setText(_translate("MainWindow", "Вишневе"))
        self.settle_name.setPlaceholderText(_translate("MainWindow", "Вишневе"))
        self.label_7.setText(_translate("MainWindow", "Номер телефону"))
        self.label_8.setText(_translate("MainWindow", "ПІБ Отримувуча"))
        self.phone.setText(_translate("MainWindow", "+380957243825"))
        self.phone.setPlaceholderText(_translate("MainWindow", "+380957243825"))
        self.label_9.setText(_translate("MainWindow", "Вулиця/відділення почти"))
        self.street.setText(_translate("MainWindow", "відділення Нова Пошта №1 "))
        self.street.setPlaceholderText(_translate("MainWindow", "відділення Нова Пошта №1 "))
        self.region.setText(_translate("MainWindow", "Дніпропетровська"))
        self.region.setPlaceholderText(_translate("MainWindow", "Дніпропетровська"))
        self.settle_type.setItemText(0, _translate("MainWindow", "Смт"))
        self.settle_type.setItemText(1, _translate("MainWindow", "Село"))
        self.settle_type.setItemText(2, _translate("MainWindow", "Місто"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Покупець"))
        self.label_14.setText(_translate("MainWindow", "Тип товару"))
        self.name.setText(_translate("MainWindow", "Електроскутер"))
        self.name.setPlaceholderText(_translate("MainWindow", "Електроскутер"))
        self.label_15.setText(_translate("MainWindow", "Модель товару"))
        self.model.setText(_translate("MainWindow", "ETB-122"))
        self.model.setPlaceholderText(_translate("MainWindow", "ETB-122"))
        self.label_16.setText(_translate("MainWindow", "Потужність"))
        self.label_17.setText(_translate("MainWindow", "Ємність акумулятора"))
        self.power.setText(_translate("MainWindow", "1000 Вт"))
        self.power.setPlaceholderText(_translate("MainWindow", "1000 Вт"))
        self.capacity.setText(_translate("MainWindow", "60В, 20А"))
        self.capacity.setPlaceholderText(_translate("MainWindow", "60В, 20А"))
        self.label_18.setText(_translate("MainWindow", "Батарея"))
        self.battery_type.setItemText(0, _translate("MainWindow", "свинцево-кислотна"))
        self.battery_type.setItemText(1, _translate("MainWindow", "літій-іонна"))
        self.label_19.setText(_translate("MainWindow", "Колір"))
        self.color.setText(_translate("MainWindow", "бордовий"))
        self.color.setPlaceholderText(_translate("MainWindow", "бордовий"))
        self.label_20.setText(_translate("MainWindow", "Повна ціна товару при відкритому порту Одеси"))
        self.price.setSuffix(_translate("MainWindow", "$"))
        self.free_delivery.setText(_translate("MainWindow", "Безкоштовна доставка"))
        self.warranty.setText(_translate("MainWindow", "Гарантія"))
        self.advance.setText(_translate("MainWindow", "Вся сума вноситься авансом"))
        self.lamp.setText(_translate("MainWindow", "Габаритні ліхтарі"))
        self.alarm.setText(_translate("MainWindow", "Сигналізація"))
        self.charger.setText(_translate("MainWindow", "Зарядний пристрій"))
        self.mirror.setText(_translate("MainWindow", "Дзеркала заднього виду"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Товар"))
        self.label_10.setText(_translate("MainWindow", "Дата укладання договору"))
        self.contract_date.setItemText(0, _translate("MainWindow", "Сьогодні"))
        self.contract_date.setItemText(1, _translate("MainWindow", "Завтра"))
        self.label_11.setText(_translate("MainWindow", "Номер договору"))
        self.label_12.setText(_translate("MainWindow", "\"В разі відкриття порту Одеси до дати ...\""))
        self.label_13.setText(_translate("MainWindow", "Курс "))
        self.dollar_rate.setSuffix(_translate("MainWindow", " грн/дол"))
        self.odesa_date.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.done_button.setText(_translate("MainWindow", "Зробити папку з документами"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Документ"))
