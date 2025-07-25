import cv2
import subprocess
import platform
try:
    from pygrabber.dshow_graph import FilterGraph
except ImportError:
    FilterGraph = None

class CameraManager:
    def __init__(self):
        self.cap = None

    def get_available_cameras(self):
        active_cams = []
        system_os = platform.system()

        if system_os == "Windows" and FilterGraph is not None:
            try:
                graph = FilterGraph()
                camera_names = graph.get_input_devices()
                for i, name in enumerate(camera_names):
                    cap = cv2.VideoCapture(i, cv2.CAP_MSMF)
                    if cap.isOpened():
                        active_cams.append((i, name))
                        cap.release()
            except Exception as e:
                print(f"Error in Windows detection: {e}")
                index = 0
                while True:
                    cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
                    if cap.isOpened():
                        ret, _ = cap.read()
                        if ret:
                            active_cams.append((index, f"Camera {index} (Windows)"))
                        cap.release()
                        index += 1
                    else:
                        break
        elif system_os == "Linux":
            try:
                result = subprocess.run(["v4l2-ctl", "--list-devices"], capture_output=True, text=True)
                if result.returncode == 0:
                    devices = result.stdout.strip().split("\n")
                    camera_name = None
                    for line in devices:
                        if not line.startswith("\t"):
                            camera_name = line.strip()
                        else:
                            device_path = line.strip()
                            index = int(device_path.split("/video")[1])
                            cap = cv2.VideoCapture(index, cv2.CAP_V4L2)
                            if cap.isOpened():
                                active_cams.append((index, f"{camera_name} ({device_path})"))
                                cap.release()
            except FileNotFoundError:
                print("v4l2-ctl not found. Falling back to generic detection.")
                index = 0
                while True:
                    cap = cv2.VideoCapture(index, cv2.CAP_V4L2)
                    if cap.isOpened():
                        ret, _ = cap.read()
                        if ret:
                            active_cams.append((index, f"Camera {index} (Linux)"))
                        cap.release()
                        index += 1
                    else:
                        break
        else:
            index = 0
            while True:
                cap = cv2.VideoCapture(index, cv2.CAP_ANY)
                if not cap.isOpened():
                    for backend in [cv2.CAP_AVFOUNDATION, cv2.CAP_DSHOW]:
                        cap = cv2.VideoCapture(index, backend)
                        if cap.isOpened():
                            break
                if cap.isOpened():
                    ret, _ = cap.read()
                    if ret:
                        active_cams.append((index, f"Camera {index} ({platform.system()})"))
                    cap.release()
                    index += 1
                else:
                    break

        return active_cams if active_cams else [(0, "No cameras detected")]

    def start_camera(self, camera_index):
        if self.cap:
            self.cap.release()
        self.cap = cv2.VideoCapture(camera_index)

    def get_frame(self):
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            return frame if ret else None
        return None

    def is_active(self):
        return self.cap is not None and self.cap.isOpened()

    def get_frame_position(self):
        return self.cap.get(cv2.CAP_PROP_POS_FRAMES) if self.cap else 0

    def set_frame_position(self, frame_number):
        if self.cap:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    def release(self):
        if self.cap:
            self.cap.release()
            self.cap = None

def get_available_cameras():
    return CameraManager().get_available_cameras()

