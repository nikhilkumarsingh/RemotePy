import sys
import pyautogui
if sys.platform == 'linux':
	import Xlib.threaded
from flask import Flask, render_template, Response, request
from camera_desktop import Camera

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n' + b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
	return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/mouse', methods=['POST'])
def mouse_event():
	# co-ordinates of browser image event
	ex, ey = float(request.form.get('x')), float(request.form.get('y'))
	# size of browser image
	imx, imy = float(request.form.get('X')), float(request.form.get('Y'))
	# size of desktop
	dx, dy = pyautogui.size()
	# co-ordinates of desktop event
	x, y = dx*(ex/imx), dy*(ey/imy)
	# mouse event
	event = request.form.get('type')

	if event == 'click':
		pyautogui.click(x, y)
	elif event == 'dblclick':
		pyautogui.doubleClick(x, y)
	elif event == 'rightclick':
		pyautogui.click(x, y, button='right')

	return Response("success")


@app.route('/keyboard', methods=['POST'])
def keyboard_event():
	# keyoard event
	event = request.form.get('type')
	print(event)
	if event == "text":
		text = request.form.get("text")
		pyautogui.typewrite(text)
	else:
		pyautogui.press(event)
	return Response("success")


if __name__ == "__main__":
	app.run(host='0.0.0.0', threaded=True)