import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from design import Ui_MainWindow
from currency_converter import CurrencyConverter

class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.design = Ui_MainWindow()
        self.design.setupUi(self)
        self.init_UI()
        print("Я изменил тут")

    def init_UI(self):
        self.setWindowTitle("Конвертер Валют")
        self.setWindowIcon(QIcon('exchanging.png'))

        self.design.input_currency.setPlaceholderText('Из валюты:')
        self.design.input_amount.setPlaceholderText('У меня есть:')
        self.design.output_currency.setPlaceholderText('В валюту:')
        self.design.output_amount.setPlaceholderText('Я получу:')
        self.design.pushButton.clicked.connect(self.converter)

    def converter(self):
        c = CurrencyConverter()
        input_currency = self.design.input_currency.text()
        input_amount = int(self.design.input_amount.text())
        output_currency = self.design.output_currency.text()

        output_amount = round(c.convert(input_amount, '%s' % (input_currency), '%s' % (output_currency)), 2)

        self.design.output_amount.setText(str(output_amount))

app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())