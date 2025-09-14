from multiprocessing import Process
import numpy as np
import cv2
from hailo_platform import (HEF , ConfigureParams , FormatType , HailoSchedulingAlgorithm , HailoStreamInterface ,
InferVStreams , InputVStreamParams , InputVStreams , OutputVStreamParams , OutputVStreams , VDevice)
					
class hailomodel():
	def __init__(self , model_path = "/home/av/AK/hailo-rpi5-examples/resources/models/hailo8/yolov8m.hef"):
		self.model_path = model_path
		self.params = VDevice.create_params()
		self.params.scheduling_algorithm = HailoSchedulingAlgorithm.NONE
		self.target = VDevice(params = self.params)
		self.hef = HEF(model_path)
		self.configure_params = ConfigureParams.create_from_hef(hef = self.hef , interface = HailoStreamInterface.PCIe)
		self.network_groups = self.target.configure(self.hef , self.configure_params)
		self.network_group = self.network_groups[0]
		self.network_group_params= self.network_group.create_params()
		self.input_vstreams_params = InputVStreamParams.make(self.network_group , quantized = False , format_type = FormatType.FLOAT32)
		self.output_vstreams_params = OutputVStreamParams.make(self.network_group , quantized = False , format_type = FormatType.FLOAT32)
		self.input_vstream_info = self.hef.get_input_vstream_infos()[0]
		self.output_vstream_info =self.hef.get_output_vstream_infos()[0]
		self.image_height , self.image_width , self.channels = self.input_vstream_info.shape
		#self.infer_pipeline = None
		self.infer_results = None
		self.input_data = {self.input_vstream_info.name : None}
		
	def hailoconfigure(self):
		try:
			self.infer_pipeline = InferVStreams(self.network_group , self.input_vstreams_params , self.output_vstreams_params)
			self.network_group.activate(self.network_group_params)
		except Exception as e:
			print(e)
			
	def getresult(self, frame):
		img_resized = frame.astype(np.float32)
		img_final = np.expand_dims(img_resized , axis = 0)
		self.input_data[self.input_vstream_info.name] = img_final
		try:
			with InferVStreams(self.network_group , self.input_vstreams_params , self.output_vstreams_params) as infer_pipeline:
				with self.network_group.activate(self.network_group_params):
					self.infer_results = infer_pipeline.infer(self.input_data)
		except Exception as e:
			print(e)
		#return self.infer_results
		print("done")
		
