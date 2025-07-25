from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon
from WelcomeScreen import WelcomeScreen

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P8GP-G01 Dashboard")
        self.setMinimumSize(1000, 700)
        self.setStyleSheet("background-color: #1e1e1e;")
        self.welcome_screen = WelcomeScreen(self)
        self.setCentralWidget(self.welcome_screen)
        self.setWindowIcon(QIcon("Imgs/icon.png"))

    def closeEvent(self, event):
        print("Closing MainWindow")
        if self.centralWidget():
            self.centralWidget().closeEvent(event)
        super().closeEvent(event)

