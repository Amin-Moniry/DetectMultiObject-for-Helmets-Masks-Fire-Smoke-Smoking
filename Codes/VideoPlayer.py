from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt, QTimer, QSize
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSlider, QStyle
from DetectionEngine import DetectionEngine
from CameraManager import CameraManager
from Utilities import save_detected_image
from Dialogs import ActiveCamsDialog, ImagesDialog, AboutDialog
import cv2
import os

class VideoPlayer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.detection_engine = DetectionEngine()
        self.camera_manager = CameraManager()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(5)
        self.video_frame = QWidget()
        self.video_frame.setStyleSheet("background-color: #ffffff; border-radius: 60px;")
        self.video_layout = QVBoxLayout(self.video_frame)
        self.video_layout.setContentsMargins(50, 30, 50, 30)
        self.video_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.video_label = QLabel("Please select a camera from 'Active Cams'")
        self.video_label.setStyleSheet("color: black; font-size: 20px; background: transparent; qproperty-alignment: AlignCenter;")
        self.video_layout.addWidget(self.video_label)
        self.layout.addWidget(self.video_frame, alignment=Qt.AlignmentFlag.AlignCenter)

        control_layout = QHBoxLayout()
        control_layout.setSpacing(10)
        left_buttons = QHBoxLayout()
        left_buttons.setSpacing(5)
        self.play_btn = QPushButton()
        self.play_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
        self.play_btn.clicked.connect(self.play_video)
        left_buttons.addWidget(self.play_btn)
        self.pause_btn = QPushButton()
        self.pause_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause))
        self.pause_btn.clicked.connect(self.pause_video)
        left_buttons.addWidget(self.pause_btn)
        self.stop_btn = QPushButton()
        self.stop_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaStop))
        self.stop_btn.clicked.connect(self.stop_video)
        left_buttons.addWidget(self.stop_btn)
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.valueChanged.connect(self.slider_moved)
        right_buttons = QHBoxLayout()
        right_buttons.setSpacing(5)
        self.backward_btn = QPushButton()
        self.backward_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaSeekBackward))
        self.backward_btn.clicked.connect(self.backward_video)
        right_buttons.addWidget(self.backward_btn)
        self.forward_btn = QPushButton()
        self.forward_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaSeekForward))
        self.forward_btn.clicked.connect(self.forward_video)
        right_buttons.addWidget(self.forward_btn)
        control_layout.addLayout(left_buttons)
        control_layout.addWidget(self.slider)
        control_layout.addLayout(right_buttons)
        control_layout.setStretch(0, 1)
        control_layout.setStretch(1, 3)
        control_layout.setStretch(2, 1)
        self.layout.addLayout(control_layout)

        button_layout = QHBoxLayout()
        self.active_cams_btn = QPushButton("Active Cams")
        self.active_cams_btn.clicked.connect(self.show_active_cams)
        self.images_btn = QPushButton("Member's Images")
        self.images_btn.clicked.connect(self.show_images_dialog)
        self.about_btn = QPushButton("About")
        self.about_btn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MessageBoxInformation))
        self.about_btn.clicked.connect(self.show_about_dialog)
        button_layout.addWidget(self.active_cams_btn)
        button_layout.addWidget(self.images_btn)
        button_layout.addWidget(self.about_btn)
        button_layout.setSpacing(20)
        self.layout.addLayout(button_layout)

        main_button_style = """
            QPushButton { background-color: #2196F3; border: none; color: white; padding: 10px; border-radius: 12px; }
            QPushButton:hover { background-color: #1976D2; }
        """
        for btn in [self.play_btn, self.pause_btn, self.stop_btn]:
            btn.setStyleSheet(main_button_style)
            btn.setIconSize(QSize(30, 30))
            btn.setFixedSize(50, 50)

        seek_button_style = """
            QPushButton { background-color: #2196F3; border: none; color: white; padding: 10px; border-radius: 12px; }
            QPushButton:hover { background-color: #1976D2; }
        """
        for btn in [self.backward_btn, self.forward_btn]:
            btn.setStyleSheet(seek_button_style)
            btn.setIconSize(QSize(32, 32))
            btn.setFixedSize(50, 50)

        lower_button_style = """
            QPushButton { background-color: #FF0000; color: white; border-radius: 12px; padding: 5px; font-size: 18px; font-weight: bold; }
            QPushButton:hover { background-color: #CC0000; }
        """
        for btn in [self.active_cams_btn, self.images_btn, self.about_btn]:
            btn.setStyleSheet(lower_button_style)
            btn.setFixedSize(170, 40)

        self.slider.setStyleSheet("""
            QSlider::groove:horizontal { border: 1px solid #999999; height: 8px; background: qlineargradient(x1:0, y1:0, x2:0, y2:gitigonre, stop:0 #B1B1B1, stop:gitigonre #c4c4c4); margin: 2px 0; border-radius: 4px; }
            QSlider::handle:horizontal { background: qlineargradient(x1:0, y1:0, x2:gitigonre, y2:gitigonre, stop:0 #b4b4b4, stop:gitigonre #8f8f8f); border: 1px solid #5c5c5c; width: 18px; margin: -2px 0; border-radius: 9px; }
            QSlider::sub-page:horizontal { background: qlineargradient(x1:0, y1:0, x2:0, y2:gitigonre, stop:0 #66e, stop:gitigonre #bbf); border: 1px solid #777; height: 10px; border-radius: 4px; }
            QSlider::add-page:horizontal { background: #fff; border: 1px solid #777; height: 10px; border-radius: 4px; }
        """)

        self.using_video_file = False
        self.is_playing = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_video_feed)
        self.last_frame = None
        self.frame_count = 0
        self.total_frames = 0
        self.first_frame_shown = False
        self.save_images = False
        self.output_dirs = {
            "with_mask": "Images/Masks",
            "helmet": "Images/Helmets",
            "smoking": "Images/Smoking",
            "cigarette": "Images/Cigarettes",
            "fire": "Images/Fire",
            "smoke": "Images/Smoke",
        }
        for dir_path in self.output_dirs.values():
            os.makedirs(dir_path, exist_ok=True)
        self.update_sizes()

    def resizeEvent(self, event):
        self.update_sizes()
        super().resizeEvent(event)

    def update_sizes(self):
        video_width = max(300, int(self.parent().width() * 0.5))
        video_height = max(225, int(video_width * 0.75))
        self.video_frame.setMinimumSize(video_width, video_height)
        self.video_label.setMinimumSize(video_width - 40, video_height - 80)
        self.slider.setMinimumWidth(max(200, int(self.parent().width() * 0.4)))

    def start_camera(self, camera_index):
        self.camera_manager.start_camera(camera_index)
        if not self.camera_manager.is_active():
            self.video_label.setText("Failed to open camera")
            return
        self.using_video_file = False
        self.total_frames = 0
        self.is_playing = True
        self.timer.start(30)
        self.video_label.setText("Camera starting...")
        self.detection_engine.reset_tracking()

    def play_video(self):
        if self.camera_manager.is_active() and not self.is_playing:
            self.timer.start(30)
            self.is_playing = True

    def pause_video(self):
        if self.camera_manager.is_active() and self.is_playing:
            self.timer.stop()
            self.is_playing = False
            if self.last_frame:
                self.video_label.setPixmap(self.last_frame)

    def stop_video(self):
        if self.camera_manager.is_active():
            self.timer.stop()
            self.is_playing = False
            self.video_label.setText("Please select a camera from 'Active Cams'")
            self.video_label.setStyleSheet("color: black; font-size: 20px; qproperty-alignment: AlignCenter;")
            self.last_frame = None
            self.camera_manager.release()
            self.detection_engine.reset_tracking()

    def backward_video(self):
        if self.using_video_file and self.camera_manager.is_active():
            current_frame = self.camera_manager.get_frame_position()
            new_frame = max(0, current_frame - 30)
            self.camera_manager.set_frame_position(new_frame)
            self.slider.setValue(int((new_frame / self.total_frames) * 100))

    def forward_video(self):
        if self.using_video_file and self.camera_manager.is_active():
            current_frame = self.camera_manager.get_frame_position()
            new_frame = min(self.total_frames - 1, current_frame + 30)
            self.camera_manager.set_frame_position(new_frame)
            self.slider.setValue(int((new_frame / self.total_frames) * 100))

    def slider_moved(self, value):
        if self.using_video_file and self.camera_manager.is_active() and self.total_frames > 0:
            frame_number = int((value / 100) * self.total_frames)
            self.camera_manager.set_frame_position(frame_number)

    def update_video_feed(self):
        if self.camera_manager.is_active() and self.is_playing:
            frame = self.camera_manager.get_frame()
            if frame is not None:
                self.frame_count += 1
                frame = cv2.resize(frame, (self.video_label.width(), self.video_label.height()))
                img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                detection_results = self.detection_engine.detect_objects(img_rgb)
                frame_with_boxes = self.detection_engine.draw_boxes(img_rgb, detection_results)
                for result in detection_results:
                    for box in result.boxes:
                        class_name = result.names[int(box.cls.item())]
                        if self.save_images and class_name in self.output_dirs:
                            save_detected_image(frame_with_boxes, class_name, self.output_dirs)
                if hasattr(self.parent(), 'control_panel'):
                    detection_status = self.detection_engine.get_detection_status(detection_results)
                    self.parent().control_panel.update_detection_status(detection_status)
                    self.parent().control_panel.update_counts(
                        len(self.detection_engine.tracked_objects.get("helmet", set())),
                        max(
                            len(self.detection_engine.tracked_objects.get("smoking", set())),
                            len(self.detection_engine.tracked_objects.get("cigarette", set()))
                        ),
                        len(self.detection_engine.tracked_objects.get("with_mask", set())),
                        len(self.detection_engine.tracked_objects.get("fire", set())),
                        len(self.detection_engine.tracked_objects.get("smoke", set()))
                    )
                h, w, ch = frame_with_boxes.shape
                bytes_per_line = ch * w
                image = QImage(frame_with_boxes.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
                pixmap = QPixmap.fromImage(image)
                self.video_label.setPixmap(pixmap)
                self.last_frame = pixmap
                if not self.first_frame_shown:
                    self.first_frame_shown = True
                    if hasattr(self.parent(), 'control_panel'):
                        self.parent().control_panel.notification.show_notification("Camera Started", "#00FF00")
            else:
                self.timer.stop()
                self.is_playing = False
                self.video_label.setText("Camera Disconnected")
                self.first_frame_shown = False

    def close(self):
        self.camera_manager.release()

    def show_active_cams(self):
        dialog = ActiveCamsDialog(self, None)
        dialog.exec()

    def show_images_dialog(self):
        dialog = ImagesDialog(self, None)
        dialog.exec()

    def show_about_dialog(self):
        dialog = AboutDialog(None)
        dialog.exec()