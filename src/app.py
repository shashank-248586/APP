import detection
from detection.cameraoutput import rpicam
from detection.hailoio import hailomodel
#b = hailomodel()
#b.hailoconfigure()
a = rpicam()
a.setup_camera()
#print(a.capture_frames())
for i in range(1):
    print(a.capture_frames())