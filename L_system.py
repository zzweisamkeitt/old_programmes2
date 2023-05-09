import sys
from math import sin, sqrt, fabs, ceil

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog


class Lsystem(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('L_system.ui', self)

        self.setGeometry(200, 200, 470, 450)
        self.setWindowTitle('L-системы')

        self.file_name = QFileDialog.getOpenFileName(self, 'Выбрать файл', '')[0]
        self.data = open(self.file_name, encoding='utf8').read()
        self.name_of_system = self.data.split('\n')[0]
        self.one_part_of_corner = 180 / int(self.data.split('\n')[1])
        self.axiom = self.data.split('\n')[2]
        self.theorem = self.data.split('\n')[3]

        self.a = 20
        self.startcoordx = 275
        self.startcoordy = 400

        self.value = 1
        self.slider.valueChanged[int].connect(self.paint)

    def paint(self, value):
        self.value = value
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.lstroka()
        self.draw_system(qp)
        qp.end()

    def lstroka(self):
        for i in range(self.value):
            stroka = ''
            for elem in self.axiom:
                if elem == '+':
                    stroka += '+'
                elif elem == '-':
                    stroka += '-'
                else:
                    stroka += self.theorem
            self.axiom = stroka
        # print(self.axiom)

    def draw_system(self, qp):
        for elem in list(self.axiom):
            if elem == 'F':
                if self.angle > 0:
                    b = fabs(self.a * sin(self.angle) / sin(90))
                    c = sqrt(fabs(self.a ** 2 - b ** 2))
                    qp.setPen(QColor(0, 0, 0))
                    qp.drawLine(self.startcoordx, self.startcoordy, self.startcoordx + ceil(c),
                                self.startcoordy + ceil(b))
                elif self.angle < 0:
                    b = fabs(self.a * sin(fabs(self.angle)) / sin(90))
                    c = sqrt(fabs(self.a ** 2 - b ** 2))
                    qp.setPen(QColor(0, 0, 0))
                    qp.drawLine(self.startcoordx, self.startcoordy, self.startcoordx - ceil(c),
                                self.startcoordy - ceil(b))
            elif elem == '+':
                self.angle += self.one_part_of_corner
            elif elem == '-':
                self.angle -= self.one_part_of_corner
        # b = fabs(self.a * sin(self.one_part_of_corner) / sin(90))
        # c = sqrt(fabs(self.a ** 2 - b ** 2))
        # qp.setPen(QColor(0, 0, 0))
        # qp.drawLine(self.startcoordx, self.startcoordy, self.startcoordx - ceil(c), self.startcoordy - ceil(b))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Lsystem()
    ex.show()
    sys.exit(app.exec())
