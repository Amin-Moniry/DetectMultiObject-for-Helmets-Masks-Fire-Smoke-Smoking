from PyQt6.QtCore import QPoint, QPropertyAnimation, QEasingCurve
from PyQt6.QtWidgets import QWidget, QHBoxLayout
from PyQt6.QtGui import QGuiApplication
from ControlPanel import ControlPanel
from VideoPlayer import VideoPlayer
from Notification import NotificationBar

class Dashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.notification_bar = NotificationBar(self.parent())
        self.control_panel = ControlPanel(self.notification_bar, self)
        self.video_player = VideoPlayer(self)
        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self.control_panel)
        main_layout.addWidget(self.video_player)
        main_layout.setStretch(0, 1)
        main_layout.setStretch(1, 2)
        self.show_with_animation()

    def show_with_animation(self):
        desktop = QGuiApplication.primaryScreen().geometry()
        start_pos = QPoint(-self.width(), self.y())
        end_pos = self.pos()
        self.move(start_pos)
        self.show()
        self.pos_animation = QPropertyAnimation(self, b"pos")
        self.pos_animation.setDuration(600)
        self.pos_animation.setStartValue(start_pos)
        self.pos_animation.setEndValue(end_pos)
        self.pos_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.pos_animation.start()
        self.opacity_animation = QPropertyAnimation(self, b"windowOpacity")
        self.opacity_animation.setDuration(600)
        self.opacity_animation.setStartValue(0.0)
        self.opacity_animation.setEndValue(1.0)
        self.opacity_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.opacity_animation.start()

    def resizeEvent(self, event):
        self.video_player.update_sizes()
        self.control_panel.update_sizes()
        self.notification_bar.move(self.width() - self.notification_bar.width() - 10, 10)
        super().resizeEvent(event)

    def closeEvent(self, event):
        print("Closing Dashboard")
        self.video_player.close()
        super().closeEvent(event)

