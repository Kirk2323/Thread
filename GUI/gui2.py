import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel, QGridLayout, QWidget, QMainWindow, QApplication,QComboBox, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        temp = QLabel("Température       ")
        self.text = QLineEdit("")
        self.labtemp = QLabel("")
        self.c = QLabel("        C°")
        self.k = QLabel("        K")
        conv = QLabel("Conversion        ")
        box = QComboBox()
        box.addItems(["C° --> K","K --> C°"])
        ok = QPushButton("Convertir")
        aide = QPushButton("?")


        # Ajouter les composants au grid layout
        grid.addWidget(temp, 0, 0, 1, 1)
        grid.addWidget(self.text, 0, 1, 1, 1)
        grid.addWidget(self.c, 0, 2, 1, 1)
        grid.addWidget(ok, 3, 1,1, 1)
        grid.addWidget(box, 3, 2, 1, 1)
        grid.addWidget(self.labtemp, 4, 1,1,1)
        grid.addWidget(conv, 4, 0, 1, 1)
        grid.addWidget(self.k, 4, 2, 1, 1)
        grid.addWidget(aide, 4,4,1,1)


        #grid.addWidget(quit, 4, 0,1, 2)

        aide.clicked.connect(self.__aide)
        ok.clicked.connect(self.__actionconvertir)
        box.activated.connect(self.__change)
       # quit.clicked.connect(self.__actionQuitter)
        self.setWindowTitle("Une première fenêtre")

    def __actionconvertir(self):
        if self.text.text().isnumeric():
            rep = self.text.text()
            self.labtemp.setText(f"{int(rep)+273,15}")
        else:
            self.labtemp.setText("Merci d'entrer un nombre")


    def __change(self):
        if box.currentIndex() == 1:
            self.c.setText("         K")
            self.k.setText("        C°")
        else:
            self.k.setText("         K")
            self.c.setText("        C°")



    def __aide(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message Box")
        msg.setText("Réalisé par moi même")
        msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()