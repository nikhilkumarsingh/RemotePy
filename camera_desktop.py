import sys
import cv2
import numpy as np 
import pyautogui
if sys.platform == 'linux':
    import pyscreenshot as ImageGrab
else:
    from PIL import ImageGrab
from PIL import ImageDraw
from base_camera import BaseCamera


class Camera(BaseCamera):

    @staticmethod
    def frames():
        while True:
            # capture computer screen
            img = ImageGrab.grab()
            # draw mouse pointer
            img = Camera.draw_mouse(img)
            # convert image to numpy array
            img_np = np.array(img)
            # convert color space from BGR to RGB
            frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            # convert image to jpg format
            ret, jpeg = cv2.imencode('.jpg', frame)
            yield jpeg.tobytes()


    @staticmethod
    def draw_mouse(img):
        """
        utility function to draw mouse pointer
        """
        # generate Draw object for PIL image
        draw = ImageDraw.Draw(img)
        # find current position of mouse pointer
        pos = pyautogui.position()
        # coordinates of ellipse
        ax, ay, bx, by = pos[0], pos[1], pos[0]+10, pos[1]+10
        # draw ellipse on image
        draw.ellipse((ax,ay,bx,by), fill="yellow")
        return img
