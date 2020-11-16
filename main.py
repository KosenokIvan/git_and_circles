import sys
from random import randrange
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from Ui import Ui_MainWindow


class GitAndCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.add_circle_btn.clicked.connect(self.add_circle)

    def add_circle(self):
        radius = randrange(25, 200)
        x_coord = randrange(0, 640 - radius * 2)
        y_coord = randrange(40, 480 - radius * 2)
        color = QColor(randrange(0, 256), randrange(0, 256), randrange(0, 256))
        self.circles.append((radius, x_coord, y_coord, color))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        qp = QPainter(self)
        qp.begin(self)
        for radius, x_coord, y_coord, color in self.circles:
            qp.setBrush(color)
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
