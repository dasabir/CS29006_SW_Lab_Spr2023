import en_core_web_sm
nlp = en_core_web_sm.load()

import torch
from lavis.models import load_model_and_preprocess
from PIL import Image

# setup device to use
device = torch.device("cpu")

# Class definition for the model
class ImageCaptioningModel(object):
	'''
		The blackbox image captioning model (LAVIS).
		Given an image path, it generates the required number of captions.
	'''

	# __init__ function
	def __init__(self):
		self.model, self.vis_processors, _ = load_model_and_preprocess(
			name="blip_caption", model_type="large_coco", is_eval=True, device=device
		)
		self.vis_processors.keys()
	
	# function for calling the caption model
	def __call__(self, input_path, num_captions):
		raw_image = Image.open(input_path).convert("RGB")
		image = self.vis_processors["eval"](raw_image).unsqueeze(0).to(device)
		return self.model.generate({"image": image}, use_nucleus_sampling=True, num_captions=num_captions)