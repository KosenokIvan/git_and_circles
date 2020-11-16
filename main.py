import sys
from random import randrange
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class GitAndCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.initUI()

    def initUI(self):
        uic.loadUi("Ui.ui", self)
        self.add_circle_btn.clicked.connect(self.add_circle)

    def add_circle(self):
        radius = randrange(25, 200)
        x_coord = randrange(0, 640 - radius * 2)
        y_coord = randrange(40, 480 - radius * 2)
        self.circles.append((radius, x_coord, y_coord))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        qp = QPainter(self)
        qp.begin(self)
        qp.setBrush(QColor("#FFFF00"))
        for radius, x_coord, y_coord in self.circles:
            qp.drawEllipse(x_coord, y_coord, radius * 2, radius * 2)
        qp.end()


def excepthook(cls, value, traceback):
    sys.__excepthook__(cls, value, traceback)


if __name__ == "__main__":
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    ex = GitAndCircles()
    ex.show()
    sys.exit(app.exec())
