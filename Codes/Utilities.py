import cv2
import os
import time


def hex_to_bgr(hex_color):
    hex_color = hex_color.lstrip('#')
    rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    return (rgb[2], rgb[1], rgb[0])

def save_detected_image(frame, class_name, box, output_dirs):
    if frame is None or class_name not in output_dirs:
        return
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    cropped_img = frame[y1:y2, x1:x2]
    if cropped_img.size == 0:
        return
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dirs[class_name], f"{class_name}_{timestamp}.jpg")
    cv2.imwrite(output_path, cropped_img)
    print(f"Saved {class_name} image to {output_path}")

