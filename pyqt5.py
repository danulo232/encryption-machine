import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("Machine")
        self.resize(450, 330)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.slovnuk_slova_y_shufr = {
            "а": "е",
            "б": "н",
            "в": "б",
            "г": "р",
            "д": "и",
            "е": "у",
            "є": "в",
            "ж": "ї",
            "з": "ч",
            "и": "г",
            "ї": "о",
            "й": "є",
            "к": "л",
            "л": "д",
            "м": "щ",
            "н": "й",
            "о": "ю",
            "п": "а",
            "р": "с",
            "с": "м",
            "т": "я",
            "у": "п",
            "ф": "ж",
            "х": "ц",
            "ц": "х",
            "ч": "к",
            "ш": "т",
            "щ": "ш",
            "ь": "з",
            "ю": "ь",
            "я": "ф",
        }

        self.slovnuk_shufr_y_slova = {
                    "е":"а",
                    "н":"б",
                    "б":"в",
                    "р":"г",
                    "и":"д",
                    "у":"е",
                    "в":"є",
                    "ї":"ж",
                    "ч":"з",
                    "г":"и",
                    "о":"ї",
                    "є":"й",
                    "л":"к",
                    "д":"л",
                    "щ":"м",
                    "й":"н",
                    "ю":"о",
                    "а":"п",
                    "с":"р",
                    "м":"с",
                    "я":"т",
                    "п":"у",
                    "ж":"ф",
                    "ц":"х",
                    "х":"ц",
                    "к":"ч",
                    "т":"ш",
                    "ш":"щ",
                    "з":"ь",
                    "ь":"ю",
                    "ф":"я",
                    " ":" ",
                    "'":"'"}

        self.label_1 = QtWidgets.QLabel(self)
        self.label_1.setText("Введіть букву, слово, речення")
        self.label_1.setFixedHeight(31)
        self.label_1.setFont(QFont("Arial", 12))
        self.label_1.setStyleSheet("color: rgb(255, 255, 0); color: rgb(255, 5, 17);  font-weight: 700")


        self.text_edit = QtWidgets.QPlainTextEdit(self)
        self.text_edit.setFont(QFont("Arial", 12))
        self.text_edit.setStyleSheet("background-color: rgb(59, 59, 59); color: rgb(255, 73, 57);")

        self.text_otvet = QtWidgets.QTextBrowser()
        self.text_otvet.setFont(QFont("Arial", 12))
        self.text_otvet.setStyleSheet("background-color: rgb(59, 59, 59); color: rgb(255, 73, 57);")

        #кнопка - текст у шифр
        self.btn_1 = QtWidgets.QPushButton(self)
        self.btn_1.setText("Текст у шифр")
        self.btn_1.setFixedWidth(191)
        self.btn_1.setFixedHeight(31)
        self.btn_1.setFont(QFont("Arial", 12))
        self.btn_1.setStyleSheet("background-color: rgb(44, 44, 44); color: rgb(217, 1, 5);  font-weight: 700")
        self.btn_1.clicked.connect(self.btn_1_cliked)

        #кнопка - шифр y текст
        self.btn_2 = QtWidgets.QPushButton(self)
        self.btn_2.setText("Шифр у текст")
        self.btn_2.setFixedWidth(191)
        self.btn_2.setFixedHeight(31)
        self.btn_2.setFont(QFont("Arial", 12))
        self.btn_2.setStyleSheet("background-color: rgb(44, 44, 44); color: rgb(217, 1, 5);  font-weight: 700")
        self.btn_2.clicked.connect(self.btn_2_cliked)

        #розташування віджетів
        self.geometry_ = QtWidgets.QGridLayout(self.centralwidget)
        self.geometry_.addWidget(self.label_1, 1, 1)
        self.geometry_.addWidget(self.text_edit, 2, 1, 1, 2)
        self.geometry_.addWidget(self.btn_1, 3, 1)
        self.geometry_.addWidget(self.text_otvet, 4, 1, 1, 2)
        self.geometry_.addWidget(self.btn_2, 3, 2)

    #відповідь "Текст у шифр"
    def btn_1_cliked(self):
        text = self.text_edit.toPlainText()
        self.text_otvet.clear()
        for char in text:
            prin = self.slovnuk_slova_y_shufr.get(char)
            if not prin:
                prin = char
            self.text_otvet.insertPlainText(prin)

    #відповідь "Шифр у текст"
    def btn_2_cliked(self):
        text = self.text_edit.toPlainText()
        self.text_otvet.clear()
        for char in text:
            prin = self.slovnuk_shufr_y_slova.get(char)
            if not prin:
                prin = char
            self.text_otvet.insertPlainText(prin)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("icon.png"))
    w = Window()
    w.show()
    sys.exit(app.exec_())
