from PyQt6.QtGui import QPixmap, QFont, QColor, QDesktopServices
from PyQt6.QtCore import Qt, QUrl, QPropertyAnimation
from PyQt6.QtWidgets import QDialog, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QScrollArea, QGridLayout, QRadioButton, QButtonGroup, QCheckBox
from CameraManager import get_available_cameras
import os

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=None)
        self.setWindowTitle("About P8GP-G01")
        self.setMinimumSize(500, 600)
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowMinMaxButtonsHint)
        self.setStyleSheet("background-color: #222; color: white; border: 1px solid #555; border-radius: 10px;")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        title_label = QLabel("P8GP-G01")
        title_label.setFont(QFont("Agency FB", 24, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #FF0000;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        team_info = QLabel(
            "💼 Team and Responsibilities 💼\n\n"
            "All Responsibilities and Development:\n"
            "- Amin Moniry  🎨🖥️🔧📈🌐🛠️✔️\n\n"
            "Supervision and Guidance:\n"
            "- Saeed Shokraneh  🎓"
        )

        team_info.setStyleSheet("font-size: 16px;")
        team_info.setWordWrap(True)
        layout.addWidget(team_info)

        version_info = QLabel("Version: 2.5\nDate: April 25, 2025\nLocation: Tabriz, Iran 🇮🇷")
        version_info.setStyleSheet("font-size: 14px; color: #AAAAAA;")
        version_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(version_info)

        readme_link = QPushButton("View README")
        readme_link.setStyleSheet("""
            QPushButton { color: #33FF00; background: transparent; text-decoration: underline; font-size: 14px; border: none; }
            QPushButton:hover { color: #66FF33; }
        """)
        readme_link.clicked.connect(self.open_readme)
        layout.addWidget(readme_link, alignment=Qt.AlignmentFlag.AlignCenter)

        readme_path_label = QLabel(f"README File: {os.path.abspath('README.md')}")
        readme_path_label.setStyleSheet("font-size: 12px; color: #AAAAAA;")
        readme_path_label.setWordWrap(True)
        layout.addWidget(readme_path_label, alignment=Qt.AlignmentFlag.AlignCenter)

        close_button = QPushButton("Close")
        close_button.setStyleSheet("""
            QPushButton { background-color: #FF0000; color: white; border-radius: 10px; padding: 5px; font-size: 16px; font-weight: bold; }
            QPushButton:hover { background-color: #CC0000; }
        """)
        close_button.setFixedSize(100, 40)
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addStretch()

        self.is_dragging = False
        self.is_resizing = False
        self.resize_edge = None
        self.drag_position = None
        self.setMouseTracking(True)
        self.center_on_screen()

    def open_readme(self):
        readme_path = "README.md"
        if os.path.exists(readme_path):
            QDesktopServices.openUrl(QUrl.fromLocalFile(readme_path))
        else:
            error_label = QLabel("README.md not found!")
            error_label.setStyleSheet("color: #FF0000; font-size: 14px;")
            self.layout().addWidget(error_label, alignment=Qt.AlignmentFlag.AlignCenter)

    def center_on_screen(self):
        screen = self.screen().geometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.pos()
            edge_margin = 10
            pos = event.position().toPoint()
            if pos.x() <= edge_margin:
                self.is_resizing = True
                self.resize_edge = "left"
            elif pos.x() >= self.width() - edge_margin:
                self.is_resizing = True
                self.resize_edge = "right"
            elif pos.y() <= edge_margin:
                self.is_resizing = True
                self.resize_edge = "top"
            elif pos.y() >= self.height() - edge_margin:
                self.is_resizing = True
                self.resize_edge = "bottom"
            else:
                self.is_dragging = True
            event.accept()

    def mouseMoveEvent(self, event):
        pos = event.globalPosition().toPoint()
        if self.is_dragging:
            self.move(pos - self.drag_position)
            event.accept()
        elif self.is_resizing:
            if self.resize_edge == "left":
                delta = self.pos().x() - pos.x()
                self.setGeometry(pos.x(), self.y(), self.width() + delta, self.height())
            elif self.resize_edge == "right":
                delta = pos.x() - (self.x() + self.width())
                self.resize(self.width() + delta, self.height())
            elif self.resize_edge == "top":
                delta = self.pos().y() - pos.y()
                self.setGeometry(self.x(), pos.y(), self.width(), self.height() + delta)
            elif self.resize_edge == "bottom":
                delta = pos.y() - (self.y() + self.height())
                self.resize(self.width(), self.height() + delta)
            event.accept()
        else:
            edge_margin = 10
            cursor_pos = event.position().toPoint()
            if cursor_pos.x() <= edge_margin:
                self.setCursor(Qt.CursorShape.SizeHorCursor)
            elif cursor_pos.x() >= self.width() - edge_margin:
                self.setCursor(Qt.CursorShape.SizeHorCursor)
            elif cursor_pos.y() <= edge_margin:
                self.setCursor(Qt.CursorShape.SizeVerCursor)
            elif pos.y() >= self.height() - edge_margin:
                self.is_resizing = True
                self.resize_edge = "bottom"
            else:
                self.is_dragging = True
            event.accept()

    def mouseMoveEvent(self, event):
        pos = event.globalPosition().toPoint()
        if self.is_dragging:
            self.move(pos - self.drag_position)
            event.accept()
        elif self.is_resizing:
            if self.resize_edge == "left":
                delta = self.pos().x() - pos.x()
                self.setGeometry(pos.x(), self.y(), self.width() + delta, self.height())
            elif self.resize_edge == "right":
                delta = pos.x() - (self.x() + self.width())
                self.resize(self.width() + delta, self.height())
            elif self.resize_edge == "top":
                delta = self.pos().y() - pos.y()
                self.setGeometry(self.x(), pos.y(), self.width(), self.height() + delta)
            elif self.resize_edge == "bottom":
                delta = pos.y() - (self.y() + self.height())
                self.resize(self.width(), self.height() + delta)
            event.accept()
        else:
            edge_margin = 10
            cursor_pos = event.position().toPoint()
            if cursor_pos.x() <= edge_margin:
                self.setCursor(Qt.CursorShape.SizeHorCursor)
            elif cursor_pos.x() >= self.width() - edge_margin:
                self.setCursor(Qt.CursorShape.SizeHorCursor)
            elif cursor_pos.y() <= edge_margin:
                self.setCursor(Qt.CursorShape.SizeVerCursor)
            elif cursor_pos.y() >= self.height() - edge_margin:
                self.setCursor(Qt.CursorShape.SizeVerCursor)
            else:
                self.setCursor(Qt.CursorShape.ArrowCursor)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = False
            self.is_resizing = False
            self.resize_edge = None
            event.accept()

class ActiveCamsDialog(QDialog):
    def __init__(self, video_player, parent=None):
        super().__init__(parent=None)
        self.video_player = video_player
        self.setWindowTitle("Select Camera")
        self.setMinimumSize(500, 320)
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowMinMaxButtonsHint)
        self.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:gitigonre, y2:gitigonre, stop:0 #1e1e1e, stop:gitigonre #333333);
            border-radius: 15px;
            border: 2px solid #FF0000;
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        self.title_label = QLabel("Choose Your Camera")
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #FF0000; font-family: 'Arial'; background: transparent;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title_label)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("""
            QScrollArea { background: transparent; border: none; }
            QScrollBar:vertical { border: none; background: #555555; width: 11px; margin: 0px; border-radius: 5px; }
            QScrollBar::handle:vertical { background: #FF0000; border-radius: 5px; min-height: 21px; }
        """)
        self.camera_widget = QWidget()
        self.camera_layout = QVBoxLayout(self.camera_widget)
        self.camera_layout.setSpacing(10)
        self.button_group = QButtonGroup(self)

        active_cams = get_available_cameras()
        if active_cams and active_cams[0][1] != "No cameras detected":
            for index, cam_name in active_cams:
                radio = QRadioButton(cam_name)
                radio.setStyleSheet("""
                    QRadioButton { color: white; font-size: 16px; padding: 10px; background: #444444; border-radius: 12px; spacing: 10px; }
                    QRadioButton:hover { background: #666666; color: #33FF00; }
                    QRadioButton::indicator { width: 24px; height: 24px; }
                    QRadioButton::indicator:unchecked { background-color: #777777; border: 2px solid #FFFFFF; border-radius: 12px; }
                    QRadioButton::indicator:checked { background-color: #FF0000; border: 2px solid #FFFFFF; border-radius: 12px; }
                """)
                radio.camera_index = index
                self.button_group.addButton(radio)
                self.camera_layout.addWidget(radio)
            self.button_group.buttons()[0].setChecked(True)
        else:
            no_cam_label = QLabel("No cameras detected")
            no_cam_label.setStyleSheet("color: #AAAAAA; font-size: 16px;")
            self.camera_layout.addWidget(no_cam_label)

        self.scroll_area.setWidget(self.camera_widget)
        layout.addWidget(self.scroll_area)

        self.select_button = QPushButton("Activate Camera")
        self.select_button.setStyleSheet("""
            QPushButton { background-color: #FF0000; color: white; font-size: 16px; font-weight: bold; padding: 10px; border-radius: 8px; border: 2px solid #FFFFFF; }
            QPushButton:hover { background-color: #CC0000; border: 2px solid #33FF00; }
        """)
        self.select_button.clicked.connect(self.select_camera)
        layout.addWidget(self.select_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.close_button = QPushButton("Close")
        self.close_button.setStyleSheet("""
            QPushButton { background-color: #555555; color: white; font-size: 14px; padding: 8px; border-radius: 8px; }
            QPushButton:hover { background-color: #777777; }
        """)
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.is_dragging = False
        self.is_resizing = False
        self.resize_edge = None
        self.drag_position = None
        self.setMouseTracking(True)
        self.center_on_screen()

    def center_on_screen(self):
        screen = self.screen().geometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2)

    def select_camera(self):
        selected_button = self.button_group.checkedButton()
        if selected_button:
            camera_index = selected_button.camera_index
            self.video_player.start_camera(camera_index)
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.pos()
            edge_margin = 10
            pos = event.position().toPoint()
            if pos.x() <= edge_margin:
                self.is_resizing = True
                self.resize_edge = "left"
            elif pos.x() >= self.width() - edge_margin:
                self.is_resizing = True
                self.resize_edge = "right"
            elif pos.y() <= edge_margin:
                self.is_resizing = True
                self.resize_edge = "top"
            elif pos.y() >= self.height() - edge_margin:
                self.is_resizing = True
                self.resize_edge = "bottom"
            else:
                self.is_dragging = True
            event.accept()

    def mouseMoveEvent(self, event):
        pos = event.globalPosition().toPoint()
        if self.is_dragging:
            self.move(pos - self.drag_position)
            event.accept()
        elif self.is_resizing:
            if self.resize_edge == "left":
                delta = self.pos().x() - pos.x()
                self.setGeometry(pos.x(), self.y(), self.width() + delta, self.height())
            elif self.resize_edge == "right":
                delta = pos.x() - (self.x() + self.width())
                self.resize(self.width() + delta, self.height())
            elif self.resize_edge == "top":
                delta = self.pos().y() - pos.y()
                self.setGeometry(self.x(), pos.y(), self.width(), self.height() + delta)
            elif self.resize_edge == "bottom":
                delta = pos.y() - (self.y() + self.height())
                self.resize(self.width(), self.height() + delta)
            event.accept()
        else:
            edge_margin = 10
            cursor_pos = event.position().toPoint()
            if cursor_pos.x() <= edge_margin:
                self.setCursor(Qt.CursorShape.SizeHorCursor)
            elif cursor_pos.x() >= self.width() - edge_margin:
                self.setCursor(Qt.CursorShape.SizeHorCursor)
            elif cursor_pos.y() <= edge_margin:
                self.setCursor(Qt.CursorShape.SizeVerCursor)
            elif cursor_pos.y() >= self.height() - edge_margin:
                self.setCursor(Qt.CursorShape.SizeVerCursor)
            else:
                self.setCursor(Qt.CursorShape.ArrowCursor)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = False
            self.is_resizing = False
            self.resize_edge = None
            event.accept()

class GalleryDialog(QDialog):
    def __init__(self, folder_path, class_name, parent=None):
        super().__init__(parent=None)
        self.setWindowTitle(f"{class_name} Images Gallery")
        self.setMinimumSize(1000, 800)
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowMinMaxButtonsHint)
        self.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:gitigonre, y2:gitigonre, stop:0 #1e1e1e, stop:gitigonre #333333);
            border-radius: 20px;
            border: 2px solid #FF0000;
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        title_label = QLabel(f"{class_name} Images Gallery")
        title_label.setStyleSheet("font-size: 28px; font-weight: bold; color: #FF0000; font-family: 'Arial'; background: transparent; padding: 10px;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("""
            QScrollArea { background: transparent; border: none; }
            QScrollBar:vertical { border: none; background: #555555; width: 11px; margin: 0px; border-radius: 5px; }
            QScrollBar::handle:vertical { background: #FF0000; border-radius: 5px; min-height: 21px; }
        """)
        gallery_widget = QWidget()
        gallery_layout = QGridLayout(gallery_widget)
        gallery_layout.setSpacing(10)

        image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if not image_files:
            no_image_label = QLabel("No Images found in this folder!")
            no_image_label.setStyleSheet("color: #AAAAAA; font-size: 16px;")
            gallery_layout.addWidget(no_image_label, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        else:
            for i, image_file in enumerate(image_files):
                image_path = os.path.join(folder_path, image_file)
                pixmap = QPixmap(image_path).scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                image_label = QLabel()
                image_label.setPixmap(pixmap)
                image_label.setStyleSheet("QLabel { border-radius: 10px; background: #444444; padding: 5px; } QLabel:hover { background: #666666; }")
                image_label.setCursor(Qt.CursorShape.PointingHandCursor)
                image_label.mousePressEvent = lambda event, path=image_path: self.show_preview(path)
                row = i // 4
                col = i % 4
                gallery_layout.addWidget(image_label, row, col)

        scroll_area.setWidget(gallery_widget)
        layout.addWidget(scroll_area)

        close_button = QPushButton("Close")
        close_button.setStyleSheet("""
            QPushButton { background-color: #555555; color: white; font-size: 14px; padding: 10px; border-radius: 8px; }
            QPushButton:hover { background-color: #777777; }
        """)
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.preview_label = QLabel(self)
        self.preview_label.setStyleSheet("background: rgba(0, 0, 0, 0.9); border-radius: 10px;")
        self.preview_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preview_label.hide()

        self.is_dragging = False
        self.is_resizing = False
        self.resize_edge = None
        self.drag_position = None
        self.setMouseTracking(True)

        self.center_on_screen()

    def center_on_screen(self):
        screen = self.screen().geometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2)

    def show_preview(self, image_path):
        pixmap = QPixmap(image_path).scaled(500, 500, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.preview_label.setPixmap(pixmap)
        self.preview_label.resize(pixmap.size())
        self.preview_label.move(self.rect().center() - self.preview_label.rect().center())
        self.preview_label.show()
        self.fade_animation = QPropertyAnimation(self.preview_label, b"windowOpacity")
        self.fade_animation.setDuration(300)
        self.fade_animation.setStartValue(0.0)
        self.fade_animation.setEndValue(1.0)
        self.fade_animation.start()
        self.preview_label.mousePressEvent = lambda event: self.hide_preview()

    def hide_preview(self):
        self.fade_animation = QPropertyAnimation(self.preview_label, b"windowOpacity")
        self.fade_animation.setDuration(300)
        self.fade_animation.setStartValue(1.0)
        self.fade_animation.setEndValue(0.0)
        self.fade_animation.finished.connect(self.preview_label.hide)
        self.fade_animation.start()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.pos()
            edge_margin = 10
            pos = event.position().toPoint()
            if pos.x() <= edge_margin:
                self.is_resizing = True
                self.resize_edge = "left"
            elif pos.x() >= self.width() - edge_margin:
                self.is_resizing = True
                self.resize_edge = "right"
            elif pos.y() <= edge_margin:
                self.is_resizing = True
                self.resize_edge = "top"
            elif pos.y() >= self.height() - edge_margin:
                self.is_resizing = True
                self.resize_edge = "bottom"
            else:
                self.is_dragging = True
            event.accept()

    def mouseMoveEvent(self, event):
        pos = event.globalPosition().toPoint()
        if self.is_dragging:
            self.move(pos - self.drag_position)
            event.accept()
        elif self.is_resizing:
            if self.resize_edge == "left":
                delta = self.pos().x() - pos.x()
                self.setGeometry(pos.x(), self.y(), self.width() + delta, self.height())
            elif self.resize_edge =="right":
                delta = pos.x() - (self.x() + self.width())
                self.resize(self.width() + delta, self.height())
            elif self.resize_edge == "top":
                delta = self.pos().y() - pos.y()
                self.setGeometry(self.x(), pos.y(), self.width(), self.height() + delta)
            elif self.resize_edge == "bottom":
                delta = pos.y() - (self.y() + self.height())
                self.resize(self.width(), self.height() + delta)
            event.accept()
        else:
            edge_margin = 10
            cursor_pos = event.position().toPoint()
            if cursor_pos.x() <= edge_margin:
                self.setCursor(Qt.CursorShape.SizeHorCursor)
            elif cursor_pos.x() >= self.width() - edge_margin:
                self.setCursor(Qt.CursorShape.SizeHorCursor)
            elif cursor_pos.y() <= edge_margin:
                self.setCursor(Qt.CursorShape.SizeVerCursor)
            elif cursor_pos.y() >= self.height() - edge_margin:
                self.setCursor(Qt.CursorShape.SizeVerCursor)
            else:
                self.setCursor(Qt.CursorShape.ArrowCursor)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = False
            self.is_resizing = False
            self.resize_edge = None
            event.accept()

class ImagesDialog(QDialog):
    def __init__(self, video_player, parent=None):
        super().__init__(parent=None)
        self.video_player = video_player
        self.setWindowTitle("Member's Images Gallery")
        self.setMinimumSize(850, 650)
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowMinMaxButtonsHint)
        self.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:gitigonre, y2:gitigonre, stop:0 #1e1e1e, stop:gitigonre #333333);
            border-radius: 20px;
            border: 2px solid #FF0000;
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        self.title_label = QLabel("Member's Images Gallery")
        self.title_label.setStyleSheet("font-size: 28px; font-weight: bold; color: #FF0000; font-family: 'Arial'; background: transparent; padding: 10px;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title_label)

        self.toggle_switch = QCheckBox("Save Detected Images")
        self.toggle_switch.setStyleSheet("""
            QCheckBox { color: white; font-size: 18px; padding: 10px; background: #444444; border-radius: 12px; }
            QCheckBox:hover { background: #666666; color: #FF0000; }
            QCheckBox::indicator { width: 30px; height: 30px; }
            QCheckBox::indicator:unchecked { background-color: #777777; border: 2px solid #FFFFFF; border-radius: 15px; }
            QCheckBox::indicator:checked { background-color: #FF0000; border: 2px solid #FFFFFF; border-radius: 15px; }
        """)
        self.toggle_switch.stateChanged.connect(self.toggle_saving)
        layout.addWidget(self.toggle_switch, alignment=Qt.AlignmentFlag.AlignCenter)

        self.folder_buttons = {
            "with_mask": QPushButton("Open Masks Gallery"),
            "helmet": QPushButton("Open Helmets Gallery"),
            "smoking": QPushButton("Open Smoking Gallery"),
            "cigarette": QPushButton("Open Cigarettes Gallery"),
            "fire": QPushButton("Open Fire Gallery"),
            "smoke": QPushButton("Open Smoke Gallery"),
        }
        button_style = """
            QPushButton { background-color: #FF0000; color: white; font-size: 16px; font-weight: bold; padding: 12px; border-radius: 10px; border: 2px solid #FFFFFF; }
            QPushButton:hover { background-color: #CC00CC; border: 2px solid #FF66FF; }
        """
        for class_name, button in self.folder_buttons.items():
            button.setStyleSheet(button_style)
            button.clicked.connect(lambda _, cn=class_name: self.show_gallery(cn))
            layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.close_button = QPushButton("Close")
        self.close_button.setStyleSheet("""
            QPushButton { background-color: #555555; color: white; font-size: 14px; padding: 10px; border-radius: 8px; }
            QPushButton:hover { background-color: #777777; }
        """)
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addStretch()

        self.is_dragging = False
        self.is_resizing = False
        self.resize_edge = None
        self.drag_position = None
        self.setMouseTracking(True)

        self.center_on_screen()

    def center_on_screen(self):
        screen = self.screen().geometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2)

    def toggle_saving(self, state):
        self.video_player.save_images = (state == Qt.CheckState.Checked.value)
        status = "enabled" if self.video_player.save_images else "disabled"
        if hasattr(self.video_player.parent(), 'control_panel'):
            self.video_player.parent().control_panel.notification.show_notification(f"Image saving {status}", "#FF0000")

    def show_gallery(self, class_name):
        folder_path = os.path.abspath(self.video_player.output_dirs[class_name])
        if os.path.exists(folder_path):
            gallery_dialog = GalleryDialog(folder_path, class_name, None)
            gallery_dialog.exec()
        else:
            if hasattr(self.video_player.parent(), 'control_panel'):
                self.video_player.parent().control_panel.notification.show_notification(f"Folder {class_name} not found!", "#FF0000")

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint() - self.pos()
            edge_margin = 10
            pos = event.position().toPoint()
            if pos.x() <= edge_margin:
                self.is_resizing = True
                self.resize_edge = "left"
            elif pos.x() >= self.width() - edge_margin:
                self.is_resizing = True
                self.resize_edge = "right"
            elif pos.y() <= edge_margin:
                self.is_resizing = True
                self.resize_edge = "top"
            elif pos.y() >= self.height() - edge_margin:
                self.is_resizing = True
                self.resize_edge = "bottom"
            else:
                self.is_dragging = True
            event.accept()

    def mouseMoveEvent(self, event):
        pos = event.globalPosition().toPoint()
        if self.is_dragging:
            self.move(pos - self.drag_position)
            event.accept()
        elif self.is_resizing:
            if self.resize_edge == "left":
                delta = self.pos().x() - pos.x()
                self.setGeometry(pos.x(), self.y(), self.width() + delta, self.height())
            elif self.resize_edge == "right":
                delta = pos.x() - (self.x() + self.width())
                self.resize(self.width() + delta, self.height())
            elif self.resize_edge == "top":
                delta = self.pos().y() - pos.y()
                self.setGeometry(self.x(), pos.y(), self.width(), self.height() + delta)
            elif self.resize_edge == "bottom":
                delta = pos.y() - (self.y() + self.height())
                self.resize(self.width(), self.height() + delta)
            event.accept()
        else:
            edge_margin = 10
            cursor_pos = event.position().toPoint()
            if cursor_pos.x() <= edge_margin:
                self.setCursor(Qt.CursorShape.SizeHorCursor)
            elif cursor_pos.x() >= self.width() - edge_margin:
                self.setCursor(Qt.CursorShape.SizeHorCursor)
            elif cursor_pos.y() <= edge_margin:
                self.setCursor(Qt.CursorShape.SizeVerCursor)
            elif cursor_pos.y() >= self.height() - edge_margin:
                self.setCursor(Qt.CursorShape.SizeVerCursor)
            else:
                self.setCursor(Qt.CursorShape.ArrowCursor)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_dragging = False
            self.is_resizing = False
            self.resize_edge = None
            event.accept()