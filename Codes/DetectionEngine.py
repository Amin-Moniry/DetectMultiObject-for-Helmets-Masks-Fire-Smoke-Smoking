from ultralytics import YOLO
import cv2
import numpy as np
from Utilities import hex_to_bgr

class DetectionEngine:
    def __init__(self):
        self.models = [
            {"path": "Models/Mask_Detection.pt", "color": "#00FF00"},
            {"path": "Models/Helmet_Detection.pt", "color": "#FFFF00"},
            {"path": "Models/Smoking_Detection.pt", "color": "#FF4500"},
            {"path": "Models/Fire_Detection.pt", "color": "#FF0000"},
        ]
        self.allowed_classes = ["with_mask", "helmet", "smoking", "cigarette", "fire", "smoke"]
        self.confidence_thresholds = {
            "with_mask": 0.4,
            "helmet": 0.8,
            "cigarette": 0.62,
            "smoking": 0.7,
            "fire": 0.2,
            "smoke": 0.5,
        }
        self.tracked_objects = {}
        self.previous_positions = {}
        self.colors = {}
        self.load_models()

    def load_models(self):
        for model_info in self.models:
            model = YOLO(model_info["path"])
            model_info["model"] = model
            color = hex_to_bgr(model_info["color"])
            for class_name in model.names.values():
                if class_name in self.allowed_classes:
                    self.colors[class_name] = color
                    self.tracked_objects[class_name] = set()
                    self.previous_positions[class_name] = {}

    def detect_objects(self, frame):
        results = []
        for model_info in self.models:
            model = model_info["model"]
            result = model(frame, conf=0.1, verbose=False)[0]
            filtered_result = self.filter_results(result)
            results.append(filtered_result)
        return results

    def filter_results(self, result):
        filtered_boxes = []
        for box in result.boxes:
            class_name = result.names[int(box.cls.item())]
            confidence = box.conf.item()
            if class_name in self.allowed_classes and confidence >= self.confidence_thresholds.get(class_name, 0.5):
                filtered_boxes.append(box)
        filtered_result = result
        filtered_result.boxes = filtered_boxes
        return filtered_result

    def draw_boxes(self, frame, results):
        output_frame = frame.copy()
        for result in results:
            for box in result.boxes:
                class_name = result.names[int(box.cls.item())]
                if class_name not in self.allowed_classes:
                    continue
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = box.conf.item()
                color = self.colors.get(class_name, (255, 255, 255))
                cv2.rectangle(output_frame, (x1, y1), (x2, y2), color, 2)
                label = f"{class_name}: {confidence:.2f}"
                cv2.putText(output_frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                self.update_tracking(class_name, (x1, y1, x2, y2))
        return output_frame

    def update_tracking(self, class_name, box):
        if class_name not in self.allowed_classes:
            return
        x1, y1, x2, y2 = box
        center = ((x1 + x2) // 2, (y1 + y2) // 2)
        object_id = None
        min_distance = float("inf")
        for obj_id, prev_center in self.previous_positions.get(class_name, {}).items():
            distance = np.sqrt((center[0] - prev_center[0]) ** 2 + (center[1] - prev_center[1]) ** 2)
            if distance < min_distance and distance < 50:
                min_distance = distance
                object_id = obj_id
        if object_id is None:
            object_id = len(self.tracked_objects[class_name]) + 1
            self.tracked_objects[class_name].add(object_id)
        self.previous_positions.setdefault(class_name, {})[object_id] = center

    def get_detection_status(self, results):
        status = {class_name: False for class_name in self.allowed_classes}
        for result in results:
            for box in result.boxes:
                class_name = result.names[int(box.cls.item())]
                if class_name in self.allowed_classes:
                    status[class_name] = True
        return status

    def reset_tracking(self):
        self.tracked_objects = {class_name: set() for class_name in self.allowed_classes}
        self.previous_positions = {class_name: {} for class_name in self.allowed_classes}


