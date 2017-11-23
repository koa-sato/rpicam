import cv2
from base_camera import BaseCamera


class Camera(BaseCamera):

    video_source = 0
    camera = cv2.VideoCapture(video_source)

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        if not Camera.camera.isOpened():
            raise RuntimeError('Could not start camera.')
        while True:
            # read current frame
            _, img = Camera.camera.read()

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()