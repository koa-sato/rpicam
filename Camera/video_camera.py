import cv2
from base_camera import BaseCamera
import time

class VideoCamera(BaseCamera):
    @staticmethod
    def frames():
        cap = cv2.VideoCapture(0)
        if not cam.isOpened():
            raise RuntimeError('Could not start camera.')
        while(True):
            ret, frame = cam.read()
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
            yield cv2.imencode('.jpg', frame)[1].tobytes()