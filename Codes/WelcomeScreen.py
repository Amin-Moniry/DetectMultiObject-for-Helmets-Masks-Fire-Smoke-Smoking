from PyQt6.QtGui import QPixmap, QGuiApplication
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QRectF
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from Dashboard import Dashboard

class WelcomeScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Welcome")
        desktop = QGuiApplication.primaryScreen().geometry()
        self.setMinimumSize(800, 600)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.background_label = QLabel(self)
        pixmap = QPixmap("Imgs/P1.png")
        if pixmap.isNull():
            print("Error: Could not load Imgs/P1.png.")
        else:
            self.pixmap = pixmap
            scaled_pixmap = self.pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding)
            self.background_label.setPixmap(scaled_pixmap)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.setStyleSheet("""
            QLabel#title { color: #FF0000; font-size: 80px; font-family: "Agency FB"; 
                qproperty-alignment: AlignCenter; padding-top: 130px; padding-bottom: 250px; 
                background: transparent; }
            QPushButton { background-color: transparent; color: white; padding: 10px 0px; 
                font-size: 25px; font-style: italic; font-weight: bold; padding-top: 100px; 
                border: none; outline: none; text-decoration: underline; }
            QPushButton:hover { color: #33ff00; }
        """)
        self.title_label = QLabel("P8GP-G01")
        self.title_label.setObjectName("title")
        layout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.start_button = QPushButton("Get Started")
        self.start_button.clicked.connect(self.show_dashboard)
        layout.addWidget(self.start_button, alignment=Qt.AlignmentFlag.AlignBottom)
        layout.addStretch(1)

        self.scale_animation = QPropertyAnimation(self, b"geometry")
        self.scale_animation.setDuration(800)
        start_rect = QRectF(self.geometry().center().x() - 50, self.geometry().center().y() - 50, 100, 100)
        end_rect = QRectF(self.geometry())
        self.scale_animation.setStartValue(start_rect)
        self.scale_animation.setEndValue(end_rect)
        self.scale_animation.setEasingCurve(QEasingCurve.Type.OutBounce)
        self.scale_animation.start()

    def resizeEvent(self, event):
        scaled_pixmap = self.pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.background_label.setPixmap(scaled_pixmap)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        font_size_title = max(20, int(self.width() * 0.08))
        font_size_button = max(14, int(self.width() * 0.02))
        self.setStyleSheet(f"""
            QLabel#title {{ color: #FF0000; font-size: {font_size_title}px; font-family: "Agency FB"; 
                qproperty-alignment: AlignCenter; padding-top: {int(self.height() * 0.1)}px; 
                padding-bottom: {int(self.height() * 0.3)}px; background: transparent; }}
            QPushButton {{ background-color: transparent; color: white; padding: 10px 0px; 
                font-size: {font_size_button}px; font-style: italic; font-weight: bold; 
                padding-top: {int(self.height() * 0.15)}px; border: none; outline: none; 
                text-decoration: underline; }}
            QPushButton:hover {{ color: #33ff00; }}
        """)
        super().resizeEvent(event)

    def show_dashboard(self):
        print("Switching to Dashboard")
        dashboard = Dashboard(self.parent())
        self.parent().setCentralWidget(dashboard)
        self.deleteLater()

