import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QRadioButton,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QFormLayout,
    QDialog,
    QDialogButtonBox,
    QMainWindow,
    QToolBar,
    QStatusBar,
)
from functools import partial
appl = QApplication(sys.argv)

# layout = QGridLayout()
# layout.addWidget(QPushButton("Button"), 0, 0)
# layout.addWidget(QPushButton("Button"), 0, 1)
# layout.addWidget(QPushButton("Button"), 0, 2)
# layout.addWidget(QPushButton("Button"), 1, 0)
# layout.addWidget(QPushButton("Button"), 1, 1)
# layout.addWidget(QPushButton("Button"), 1, 2)
# layout.addWidget(QPushButton("Button"), 2, 0, 1, 3)
#
# window = QWidget()
# window.setWindowTitle("First Window")
# window.setGeometry(50, 50, 300, 500)
#
# massage = QLabel("Hello", parent=window)
# massage.move(0, 20)
#
# button = QPushButton('Button', parent=window)
# button.move(0, 60)
#
# edit = QLineEdit('', parent=window)
# edit.move(50, 20)
#
# box = QComboBox(parent=window)
# box.addItems(['python', 'java', 'go', 'java script'])
# box.move(150, 60)
#
# radio = QRadioButton('Python', parent=window)
# radio.move(0, 100)
#
# layout = QVBoxLayout()
# layout.addWidget(QPushButton('sdfdf', parent=window))
# layout.addWidget(QPushButton('jkjk', parent=window))
# layout.addWidget(QPushButton('432525', parent=window))
# layout.addWidget(QPushButton('00000', parent=window))
#
# window.setLayout(layout)


# layout.addWidget(QPushButton("Button"), 2, 1, 1, 2)

# window.setLayout(layout)

# button = QPushButton('click', parent=window)
# button.move(50, 100)
#
# edit = QLineEdit('', parent=window)
# edit.move(50, 150)
#
# combo = QComboBox(parent=window)
# combo.addItems(['python', 'java', 'go', 'java script'])
# combo.move(200, 50)
#
# radio = QRadioButton('python', parent=window)
# radio.move(200, 150)
#
# window = QDialog()
# window.setWindowTitle('3 win')
# f_layout = QFormLayout()
# b_layout = QGridLayout()
# f_layout.addRow('1', QLineEdit())
# f_layout.addRow('2', QLineEdit())
# f_layout.addRow('3', QLineEdit())
# f_layout.addRow('4', QLineEdit())
#
# b_layout.addLayout(f_layout, 0, 0)
# # b_layout.
#
# buttons = QDialogButtonBox()
# buttons.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
# b_layout.addWidget(buttons)
#
# window.setLayout(b_layout)

window = QMainWindow()
window.setWindowTitle('My window')
window.setGeometry(50, 50, 200, 200)
window.menu = window.menuBar().addMenu('Menu')
window.edit = window.menuBar().addMenu('Edit')
window.menu.addAction('exit', window.close)
window.edit.addAction('stile', window.adjustSize)

tools = QToolBar()
tools.addAction('close', window.close)
window.addToolBar(tools)

status = QStatusBar()
status.showMessage("I'm massage")
window.setStatusBar(status)

layout = QVBoxLayout()

central_widget = QWidget(window)
window.setCentralWidget(central_widget)
central_widget.setLayout(layout)

edit = QLineEdit(parent=window)
layout.addWidget(edit)


def build_expression(button):
    if edit.text() == "error":
        edit.setText('')
    expr = edit.text() + button.text()
    edit.setText(expr)


def eval_expr():
    try:
        res = str(eval(edit.text()))
    except:
        res = "error"
    edit.setText(res)


grid_layout = QGridLayout()

# grid_layout.addWidget(QPushButton('1/x'), 0, 0)
# grid_layout.addWidget(QPushButton('x^2'), 0, 1)
# grid_layout.addWidget(QPushButton('<-'), 0, 2)
# grid_layout.addWidget(QPushButton('%'), 0, 3)
_1 = QPushButton('1')
grid_layout.addWidget(_1, 1, 0)
_1.clicked.connect(partial(build_expression, _1))

_2 = QPushButton('2')
grid_layout.addWidget(_2, 1, 1)
_2.clicked.connect(partial(build_expression, _2))

_3 = QPushButton('3')
grid_layout.addWidget(_3, 1, 2)
_3.clicked.connect(partial(build_expression, _3))

# grid_layout.addWidget(QPushButton('/'), 1, 3)
# grid_layout.addWidget(QPushButton('4'), 2, 0)
# grid_layout.addWidget(QPushButton('5'), 2, 1)
# grid_layout.addWidget(QPushButton('6'), 2, 2)
# grid_layout.addWidget(QPushButton('x'), 2, 3)
# grid_layout.addWidget(QPushButton('7'), 3, 0)
# grid_layout.addWidget(QPushButton('8'), 3, 1)
# grid_layout.addWidget(QPushButton('9'), 3, 2)
_m = QPushButton('-')
grid_layout.addWidget(_m, 3, 3)
_m.clicked.connect(partial(build_expression, _m))
# grid_layout.addWidget(QPushButton('+/-'), 4, 0)
# grid_layout.addWidget(QPushButton('0'), 4, 1)
# grid_layout.addWidget(QPushButton(','), 4, 2)
_equal = QPushButton('=')
grid_layout.addWidget(_equal, 4, 3)
# _equal.clicked.connect(partial(eval_expr, edit.text()))
layout.addLayout(grid_layout)
window.setLayout(layout)


_equal.clicked.connect(eval_expr)

window.show()

sys.exit(appl.exec_())