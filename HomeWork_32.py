import functools
import math
import string
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QToolBar,
)
from functools import partial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Calc(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        self.display()
        self.add_buttons()
        # self.add_menu()
        # self.add_tool_bar()

    # def add_menu(self):
        # self.menu = self.menuBar().addMenu('trig')
        # self.edit = self.menuBar().addMenu('Expon')
        # self.menu.addAction('exit', self.close)
        # self.edit.addAction('stile', self.adjustSize)

    # def add_tool_bar(self):
    #     tools = QToolBar()
    #     self.addToolBar(tools)
    #     tools.addAction(
    #         'green', partial(
    #             self.setStyleSheet, "#MainWindow{background-color:green}"))


    def display(self):
        self.edit = QLineEdit()
        self.edit.setFixedHeight(150)
        self.edit.setAlignment(Qt.AlignLeft)
        self.edit.setReadOnly(True)
        self.edit.setFont(QFont('Times', 32))
        self.layout.addWidget(self.edit)

    def add_buttons(self):
        self.buttons = {}
        grid = QGridLayout()
        buttons = {
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            '/': (0, 3),
            'C': (0, 4),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '*': (1, 3),
            '(': (1, 4),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '-': (2, 3),
            ')': (2, 4),
            '0': (3, 0),
            '00': (3, 1),
            '.': (3, 2),
            '+': (3, 3),
            '+/-': (3, 4),
            'sin': (4, 0),
            'cos': (4, 1),
            'tg': (4, 2),
            'x^2': (4, 3),
            '=': (4, 4),
            'x^y': (5, 0),
            'x!': (5, 1)
        }

        for text, position in buttons.items():

            if text in string.digits:
                self.buttons[text] = QPushButton(text)
                self.buttons[text].setFont(QFont('Times', 18))
                self.buttons[text].setFixedSize(80, 80)
                self.buttons[text].setStyleSheet('background: gray;')
                grid.addWidget(self.buttons[text], position[0], position[1])
            else:
                self.buttons[text] = QPushButton(text)
                self.buttons[text].setFont(QFont('Times', 18))
                self.buttons[text].setFixedSize(80, 80)
                self.buttons[text].setStyleSheet("color: rgb(170, 0, 255);")
                grid.addWidget(self.buttons[text], position[0], position[1])

            self.layout.addLayout(grid)

    def set_text(self, text):
        self.edit.setText(text)
        self.edit.setFocus()

    def get_text(self):
        return self.edit.text()

    def clear_text(self):
        self.edit.setText('')


class Controller:
    def __init__(self, window: Calc):
        self.window = window
        self.connect_buttons()

    def create_expr(self, symbol):
        if self.window.edit.text() == 'error':
            self.window.clear_text()
        expr = self.window.get_text() + symbol
        self.window.set_text(expr)

    def connect_buttons(self):
        self.func_dict = {'+/-': lambda x: -x,
                          'sin': math.sin,
                          'cos': math.cos,
                          'tg': math.tan,
                          'x^2': lambda x: x ** 2,
                          'x!': self.factorial}
        for text, button in self.window.buttons.items():
            match text:
                case '=':
                    button.clicked.connect(self.eval_equal)
                case 'C':
                    button.clicked.connect(self.window.clear_text)
                case item if item in self.func_dict.keys():
                    button.clicked.connect(partial(self.func_trig, text))
                case 'x^y':
                    button.clicked.connect(partial(self.create_expr, '**'))
                case _:
                    button.clicked.connect(partial(self.create_expr, text))

    def eval_equal(self):
        try:
            res = str(eval(self.window.get_text()))
        except Exception:
            res = 'error'
        self.window.set_text(res)

    def func_trig(self, text):
        res = str(self.func_dict[text](int(self.window.get_text())))
        self.window.set_text(res)

    @staticmethod
    def factorial(numb):
        res = functools.reduce(lambda x, y: x * y, range(1, numb + 1))
        return res


def main():
    calc = QApplication(sys.argv)
    window = Calc()
    window.show()
    Controller(window=window)
    sys.exit(calc.exec_())


if __name__ == '__main__':
    main()
