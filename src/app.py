# import detection
# from detection.cameraoutput import rpicam
# from detection.hailoio import hailomodel
# from queue import Queue
# A = Queue(maxsize= 10)
# B = Queue(maxsize=3)

# #b = hailomodel()
# #b.hailoconfigure()
# a = rpicam()
# a.setup_camera()
# #print(a.capture_frames())
# for i in range(1):
#     print(a.capture_frames())
import postprocess.example as p
import numpy as np
arr = np.array([1.0, 2.0, 3.0], dtype=np.float32)
print(p.scale_array(arr, 5.0))
