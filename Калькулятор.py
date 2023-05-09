import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 350, 200, 350)
        self.setWindowTitle('Калькулятор')

        self.label1 = QLabel(self)
        self.label1.setText('')
        self.label1.move(1, 10)
        self.label1.resize(200, 30)
        self.label1.setFont(QFont('Arial', 13))
        self.label1.setAlignment(Qt.AlignRight)

        self.label2 = QLabel(self)
        self.label2.setText('')
        self.label2.move(1, 40)
        self.label2.resize(200, 60)
        self.label2.setFont(QFont('Arial', 40))
        self.label2.setAlignment(Qt.AlignRight)

        self.seven = QPushButton('7', self)
        self.seven.resize(50, 50)
        self.seven.move(0, 100)
        self.seven.clicked.connect(self.number)

        self.eight = QPushButton('8', self)
        self.eight.resize(50, 50)
        self.eight.move(50, 100)
        self.eight.clicked.connect(self.number)

        self.nine = QPushButton('9', self)
        self.nine.resize(50, 50)
        self.nine.move(100, 100)
        self.nine.clicked.connect(self.number)

        self.div = QPushButton('/', self)
        self.div.resize(50, 50)
        self.div.move(150, 100)
        self.div.clicked.connect(self.division)

        self.four = QPushButton('4', self)
        self.four.resize(50, 50)
        self.four.move(0, 150)
        self.four.clicked.connect(self.number)

        self.five = QPushButton('5', self)
        self.five.resize(50, 50)
        self.five.move(50, 150)
        self.five.clicked.connect(self.number)

        self.six = QPushButton('6', self)
        self.six.resize(50, 50)
        self.six.move(100, 150)
        self.six.clicked.connect(self.number)

        self.mul = QPushButton('*', self)
        self.mul.resize(50, 50)
        self.mul.move(150, 150)
        self.mul.clicked.connect(self.multiplication)

        self.one = QPushButton('1', self)
        self.one.resize(50, 50)
        self.one.move(0, 200)
        self.one.clicked.connect(self.number)

        self.two = QPushButton('2', self)
        self.two.resize(50, 50)
        self.two.move(50, 200)
        self.two.clicked.connect(self.number)

        self.three = QPushButton('3', self)
        self.three.resize(50, 50)
        self.three.move(100, 200)
        self.three.clicked.connect(self.number)

        self.sub = QPushButton('-', self)
        self.sub.resize(50, 50)
        self.sub.move(150, 200)
        self.sub.clicked.connect(self.subtraction)

        self.c = QPushButton('C', self)
        self.c.resize(50, 50)
        self.c.move(0, 250)
        self.c.clicked.connect(self.remove)

        self.zero = QPushButton('0', self)
        self.zero.resize(50, 50)
        self.zero.move(50, 250)
        self.zero.clicked.connect(self.number)

        self.ce = QPushButton('CE', self)
        self.ce.resize(50, 50)
        self.ce.move(100, 250)
        self.ce.clicked.connect(self.remove)

        self.add = QPushButton('+', self)
        self.add.resize(50, 50)
        self.add.move(150, 250)
        self.add.clicked.connect(self.addiction)

        self.point = QPushButton('.', self)
        self.point.resize(50, 50)
        self.point.move(0, 300)
        self.point.clicked.connect(self.number)

        self.pm = QPushButton('+-', self)
        self.pm.resize(50, 50)
        self.pm.move(50, 300)
        self.pm.clicked.connect(self.plus_and_minus)

        self.equally = QPushButton('=', self)
        self.equally.resize(100, 50)
        self.equally.move(100, 300)
        self.equally.clicked.connect(self.result)

    def number(self):
        self.label2.setText(self.label2.text() + self.sender().text())

    def division(self):
        self.label1.setText('{} {}'.format(self.label2.text(), '/'))
        self.label2.setText('')

    def addiction(self):
        self.label1.setText('{} {}'.format(self.label2.text(), '+'))
        self.label2.setText('')

    def subtraction(self):
        self.label1.setText('{} {}'.format(self.label2.text(), '-'))
        self.label2.setText('')

    def multiplication(self):
        self.label1.setText('{} {}'.format(self.label2.text(), '*'))
        self.label2.setText('')

    def remove(self):
        if self.sender().text() == 'C':
            self.label1.setText('')
            self.label2.setText('0')
        else:
            self.label2.setText('0')

    def plus_and_minus(self):
        self.label2.setText(str(int(self.label2.text()) * -1))

    def result(self):
        self.label2.setText(str(eval(self.label1.text() + ' ' + self.label2.text())))
        self.label1.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
