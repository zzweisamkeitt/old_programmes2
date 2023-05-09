import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Films(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadui('searching_films.ui', self)
        self.setWindowTitle('Поиск фильмов')
        self.cb_whatsearch.activated[str].connect(self.onActivated)
        self.btn_searching(self.searching)

        self.year = 0
        self.title = ''
        self.duration = 0
        self.cb_value = 'Год выпуска'

    def onActivated(self, text):
        self.cb_value = text

    def searching(self):
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        if self.cb_value == 'Год выпуска':
            year = self.le_input.text()
            result = cur.execute('''SELECT * FROM films
                        WHERE year = {}''').fetchall()
            for elem in result:
                print(elem)

            con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Films()
    ex.show()
    sys.exit(app.exec())


# import sqlite3
# import sys
#
# from PyQt5 import uic
# from PyQt5.QtWidgets import QApplication, QWidget
#
#
# class MyWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#         uic.loadUi('ui.ui', self)
#         self.params = {"Год выпуска": "year", "Название": "title", "Продолжительность": "duration"}
#         self.comboBox.addItems(list(self.params.keys()))
#         self.con = sqlite3.connect("films_db.sqlite")
#         self.pushButton.clicked.connect(self.select)
#
#     def select(self):
#         try:
#             req = "SELECT * FROM films WHERE {} = {}".format(self.params.get(self.comboBox.currentText()),
#                                                              self.lineEdit.text())
#             cur = self.con.cursor()
#             result = cur.execute(req).fetchone()
#             if not result:
#                 self.errorLabel.setText("Ничего не найдено")
#                 return
#             self.idEdit.setText(str(result[0]))
#             self.titleEdit.setText(result[1])
#             self.yearEdit.setText(str(result[2]))
#             self.genreEdit.setText(str(result[3]))
#             self.durationEdit.setText(str(result[4]))
#         except sqlite3.OperationalError:
#             self.errorLabel.setText("Неправильный запрос")
#
#
# def except_hook(cls, exception, traceback):
#     sys.__excepthook__(cls, exception, traceback)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     sys.excepthook = except_hook
#     ex = MyWidget()
#     ex.show()
#     sys.exit(app.exec())
