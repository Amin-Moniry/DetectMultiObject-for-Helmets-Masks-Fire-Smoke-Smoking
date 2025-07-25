from PyQt6.QtGui import QPainter, QPainterPath, QColor
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class NotificationBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(320, 80)
        self.setMaximumWidth(400)
        self.message_label = QLabel(self)
        self.message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.message_label.setWordWrap(True)
        layout = QVBoxLayout(self)
        layout.addWidget(self.message_label)
        layout.setContentsMargins(20, 10, 20, 10)
        self.setWindowFlags(Qt.WindowType.SubWindow | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowOpacity(0.0)
        self.hide()

    def show_notification(self, message, color="#FFFF00"):
        print(f"Showing notification: {message} with color {color}")
        self.message_label.setText(message)
        self.message_label.setStyleSheet(f"""
            color: {color};
            font-size: 18px;
            font-weight: bold;
            font-family: "Arial";
            background: transparent;
            padding: 5px;
        """)
        self.setWindowOpacity(1.0)
        if self.parent():
            self.move(self.parent().width() - self.width() - 10, 10)
        self.show()
        self.raise_()
        if hasattr(self, 'timer') and self.timer.isActive():
            self.timer.stop()
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.fade_out)
        self.timer.start(5000)

    def fade_out(self):
        print("Fading out notification")
        if hasattr(self, 'animation') and self.animation.state() == QPropertyAnimation.State.Running:
            self.animation.stop()
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(700)
        self.animation.setStartValue(1.0)
        self.animation.setEndValue(0.0)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.animation.finished.connect(self.hide)
        self.animation.start()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        path = QPainterPath()
        w, h = self.width(), self.height()
        path.addRoundedRect(0, 0, w, h, 10, 10)
        painter.setBrush(QColor(173, 216, 230, 220))
        painter.setPen(QColor(0, 0, 139, 180))
        painter.drawPath(path)