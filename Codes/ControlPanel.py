from PyQt6.QtGui import QFont, QFontMetrics, QColor
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFrame, QLabel, QHBoxLayout, QCheckBox, QTableWidget, QTableWidgetItem, QScrollArea

class ControlPanel(QWidget):
    def __init__(self, notification, parent=None):
        super().__init__(parent)
        self.notification = notification
        self.layout = QVBoxLayout(self)

        detection_frame = QFrame()
        detection_frame.setFrameShape(QFrame.Shape.Box)
        detection_layout = QVBoxLayout(detection_frame)
        detection_label = QLabel("REAL-TIME DETECTION MONITOR")
        detection_label.setStyleSheet("color: #FF0000; font-weight: bold; font-size: 25px;")
        detection_label.setWordWrap(True)
        detection_layout.addWidget(detection_label)

        self.detection_items = [
            {"name": "helmet", "icon": "⛑️", "checkbox": QCheckBox("Helmet Detection"), "status": QLabel()},
            {"name": "smoking_cigarette", "icon": "🚬", "checkbox": QCheckBox("Smoking/Cigarette Detection"), "status": QLabel()},
            {"name": "with_mask", "icon": "😷", "checkbox": QCheckBox("Mask Detection"), "status": QLabel()},
            {"name": "fire", "icon": "🔥", "checkbox": QCheckBox("Fire Detection"), "status": QLabel()},
            {"name": "smoke", "icon": "💨", "checkbox": QCheckBox("Smoke Detection"), "status": QLabel()},
        ]

        for item in self.detection_items:
            item_layout = QHBoxLayout()
            icon_label = QLabel(item["icon"])
            icon_label.setStyleSheet("font-size: 20px; padding-right: 5px;")
            item_layout.addWidget(icon_label)
            checkbox = item["checkbox"]
            checkbox.setStyleSheet("""
                QCheckBox { color: white; font-size: 16px; padding: 5px; }
                QCheckBox:checked { color: #00FF00; background-color: rgba(0, 255, 0, 50); border-radius: 5px; }
            """)
            item_layout.addWidget(checkbox)
            status = item["status"]
            status.setFixedSize(15, 15)
            status.setStyleSheet("background-color: %s; border-radius: 7px;" % QColor(128, 128, 128).name())
            item_layout.addWidget(status)
            item_layout.addStretch()
            detection_layout.addLayout(item_layout)

        self.layout.addWidget(detection_frame)

        status_frame = QFrame()
        status_frame.setFrameShape(QFrame.Shape.Box)
        status_layout = QVBoxLayout(status_frame)
        status_label = QLabel("YOU CAN CONTROL YOUR MEMBERS STATUS")
        status_label.setStyleSheet("color: #00FF00; font-weight: bold; font-size: 25px;")
        status_label.setWordWrap(True)
        status_layout.addWidget(status_label)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("""
            QScrollArea { background: transparent; border: none; }
            QScrollBar:vertical {
                border: none;
                background: #555555;
                width: 8px;
                margin: 0px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: #FF0000;
                border-radius: 4px;
                min-height: 15px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
                background: none;
            }
            QScrollBar:horizontal {
                border: none;
                background: #555555;
                height: 8px;
                margin: 0px;
                border-radius: 4px;
            }
            QScrollBar::handle:horizontal {
                background: #FF0000;
                border-radius: 4px;
                min-width: 15px;
            }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                width: 0px;
                background: none;
            }
        """)

        self.status_table = QTableWidget()
        self.status_table.setRowCount(5)
        self.status_table.setColumnCount(2)
        self.status_table.setHorizontalHeaderLabels(["👥(MEM)", "Detected"])
        self.status_table.setStyleSheet("""
            QTableWidget { background-color: #222; color: white; border: 1px solid #555; }
            QTableWidget::item { border: 1px solid #FFFFFF; border-radius: 15px; padding: 5px; text-align: center; }
        """)
        self.status_table.setItem(0, 0, QTableWidgetItem("⛑️ Helmet"))
        self.status_table.setItem(0, 1, QTableWidgetItem("0"))
        self.status_table.setItem(1, 0, QTableWidgetItem("🚬 Smoking/Cigarette"))
        self.status_table.setItem(1, 1, QTableWidgetItem("0"))
        self.status_table.setItem(2, 0, QTableWidgetItem("😷 Mask"))
        self.status_table.setItem(2, 1, QTableWidgetItem("0"))
        self.status_table.setItem(3, 0, QTableWidgetItem("🔥 Fire"))
        self.status_table.setItem(3, 1, QTableWidgetItem("0"))
        self.status_table.setItem(4, 0, QTableWidgetItem("💨 Smoke"))
        self.status_table.setItem(4, 1, QTableWidgetItem("0"))
        for row in range(self.status_table.rowCount()):
            for col in range(self.status_table.columnCount()):
                item = self.status_table.item(row, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

        self.scroll_area.setWidget(self.status_table)
        status_layout.addWidget(self.scroll_area)
        self.layout.addWidget(status_frame)

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        separator.setStyleSheet("color: %s;" % QColor(255, 255, 255).name())
        self.layout.addWidget(separator)

        self.table_frame = QFrame()
        self.table_frame.setFrameShape(QFrame.Shape.Box)
        table_layout = QVBoxLayout(self.table_frame)
        table_label = QLabel("Future_Plan")
        table_label.setStyleSheet("color: #FFFFFF; font-weight: bold; font-size: 20px;")
        table_layout.addWidget(table_label)
        self.table = QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Item", "Value"])
        self.table.setStyleSheet("""
            QTableWidget { background-color: #222; color: white; border: 1px solid #555; }
            QTableWidget::item { border: 1px solid #FFFFFF; border-radius: 15px; padding: 5px; }
        """)
        table_layout.addWidget(self.table)
        self.layout.addWidget(self.table_frame)

        self.update_sizes()
        self.notification.show_notification("Please select a camera")

    def resizeEvent(self, event):
        self.update_sizes()
        super().resizeEvent(event)

    def update_sizes(self):
        font_size_large = max(10, int(self.parent().width() * 0.015))
        font_size_small = max(8, int(self.parent().width() * 0.01))
        font = QFont()
        font.setPointSize(font_size_small)
        metrics = QFontMetrics(font)
        for col in range(self.status_table.columnCount()):
            max_width = 0
            for row in range(self.status_table.rowCount()):
                item = self.status_table.item(row, col)
                if item:
                    text_width = metrics.horizontalAdvance(item.text()) + 80
                    max_width = max(max_width, text_width)
            header_item = self.status_table.horizontalHeaderItem(col)
            if header_item:
                header_width = metrics.horizontalAdvance(header_item.text()) + 80
                max_width = max(max_width, header_width)
            self.status_table.setColumnWidth(col, max_width)
        for col in range(self.table.columnCount()):
            max_width = 0
            for row in range(self.table.rowCount()):
                item = self.table.item(row, col)
                if item:
                    text_width = metrics.horizontalAdvance(item.text()) + 20
                    max_width = max(max_width, text_width)
            header_item = self.table.horizontalHeaderItem(col)
            if header_item:
                header_width = metrics.horizontalAdvance(header_item.text()) + 20
                max_width = max(max_width, header_width)
            self.table.setColumnWidth(col, max_width if max_width > 0 else 100)
        self.setMaximumWidth(int(self.parent().width() * 0.25))
        for label in self.findChildren(QLabel):
            if label.text() == "REAL-TIME DETECTION MONITOR":
                label.setStyleSheet(f"color: #FF0000; font-weight: bold; font-size: {font_size_large}px;")
            elif label.text() == "YOU CAN CONTROL YOUR MEMBERS STATUS":
                label.setStyleSheet(f"color: #00FF00; font-weight: bold; font-size: {font_size_large}px;")
            elif label.text() == "Future_Plan":
                label.setStyleSheet(f"color: #FFFFFF; font-weight: bold; font-size: {font_size_large}px;")

    def update_detection_status(self, detection_results):
        for item in self.detection_items:
            if item["name"] == "smoking_cigarette":
                result = detection_results.get("smoking", False) or detection_results.get("cigarette", False)
            else:
                result = detection_results.get(item["name"], False)
            item["checkbox"].setChecked(result)
            item["status"].setStyleSheet(
                "background-color: %s; border-radius: 7px;" % QColor(0, 255, 0).name() if result
                else "background-color: %s; border-radius: 7px;" % QColor(128, 128, 128).name()
            )

    def update_counts(self, helmet_count, smoking_cigarette_count, mask_count, fire_count, smoke_count):
        self.status_table.setItem(0, 1, QTableWidgetItem(str(helmet_count)))
        self.status_table.setItem(1, 1, QTableWidgetItem(str(smoking_cigarette_count)))
        self.status_table.setItem(2, 1, QTableWidgetItem(str(mask_count)))
        self.status_table.setItem(3, 1, QTableWidgetItem(str(fire_count)))
        self.status_table.setItem(4, 1, QTableWidgetItem(str(smoke_count)))
        self.update_sizes()
        self.status_table.setMinimumWidth(sum(self.status_table.columnWidth(col) for col in range(self.status_table.columnCount())) + 20)

    def add_to_table(self, item_name, value):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        self.table.setItem(row_count, 0, QTableWidgetItem(item_name))
        self.table.setItem(row_count, 1, QTableWidgetItem(str(value)))
        self.update_sizes()