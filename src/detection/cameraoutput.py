from picamera2 import Picamera2
import numpy as np
class rpicam:
	def __init__(self):
		self.camera = Picamera2()
		self.fps = 30
		self.resolution = (640 , 640)
		
	def setup_camera(self):
		main={"size": self.resolution, "format": "RGB888"}
		#controls={"FrameRate": self.fps,"ExposureTime": 33000,"AnalogueGain": 1.0,"AwbEnable": True}
		config = self.camera.create_preview_configuration(main= main)
		try:
			self.camera.configure(config)
			self.camera.start()
		#time.sleep(1)
		except Exception as e:
			print(e)
		return True
	def capture_frames(self):
		try:
			frame = self.camera.capture_array()
			#img_resized = frame.astype(np.float32)
			#img_final = np.expand_dims(img_resized , axis = 0)
			return frame
		except Exception as e:
			print(e)
		
