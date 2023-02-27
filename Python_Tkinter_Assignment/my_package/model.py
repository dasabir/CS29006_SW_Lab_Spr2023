from PIL import Image
from lavis.models import load_model_and_preprocess
from lavis.processors.blip_processors import BlipCaptionProcessor
import torch
import en_core_web_sm
nlp = en_core_web_sm.load()

class_names = [
    "person",
    "bicycle",
    "car",
    "motorcycle",
    "airplane",
    "bus",
    "train",
    "truck",
    "boat",
    "trafficlight",
    "firehydrant",
    "stopsign",
    "parkingmeter",
    "bench",
    "bird",
    "cat",
    "dog",
    "horse",
    "sheep",
    "cow",
    "elephant",
    "bear",
    "zebra",
    "giraffe",
    "backpack",
    "umbrella",
    "handbag",
    "tie",
    "suitcase",
    "frisbee",
    "skis",
    "snowboard",
    "sportsball",
    "kite",
    "baseballbat",
    "baseballglove",
    "skateboard",
    "surfboard",
    "tennisracket",
    "bottle",
    "wineglass",
    "cup",
    "fork",
    "knife",
    "spoon",
    "bowl",
    "banana",
    "apple",
    "sandwich",
    "orange",
    "broccoli",
    "carrot",
    "hotdog",
    "pizza",
    "donut",
    "cake",
    "chair",
    "couch",
    "pottedplant",
    "bed",
    "diningtable",
    "toilet",
    "tv",
    "laptop",
    "mouse",
    "remote",
    "keyboard",
    "cellphone",
    "microwave",
    "oven",
    "toaster",
    "sink",
    "refrigerator",
    "book",
    "clock",
    "vase",
    "scissors",
    "teddybear",
    "hairdrier",
    "toothbrush"
]


# setup device to use
device = torch.device("cpu")

# Class definitions for the models


class ImageCaptioningModel(object):
    '''
        The blackbox image captioning model (LAVIS).
        Given an image path, it generates the required number of captions.
    '''

    def __init__(self):
        self.model, self.vis_processors, _ = load_model_and_preprocess(
            name="blip_caption", model_type="large_coco", is_eval=True, device=device
        )
        self.vis_processors.keys()

    def __call__(self, input_path, num_captions=3):
        raw_image = Image.open(input_path).convert("RGB")
        image = self.vis_processors["eval"](raw_image).unsqueeze(0).to(device)
        return self.model.generate({"image": image}, use_nucleus_sampling=True, num_captions=num_captions)


class ImageClassificationModel(object):
    '''
        The blackbox image classification model (LAVIS).
        Given an image path, it generates the required number of top classes.
    '''

    def __init__(self):
        self.model, self.vis_processors, _ = load_model_and_preprocess(
            "blip_feature_extractor", model_type="base", is_eval=True, device=device)
        self.cls_names = class_names
        self.text_processor = BlipCaptionProcessor(prompt="A picture of ")
        self.cls_prompt = [self.text_processor(
            cls_nm) for cls_nm in self.cls_names]

    def __call__(self, input_path, num_classes=3):
        raw_image = Image.open(input_path).convert("RGB")
        image = self.vis_processors["eval"](raw_image).unsqueeze(0).to(device)
        sample = {"image": image, "text_input": self.cls_prompt}
        image_features = self.model.extract_features(
            sample, mode="image").image_embeds_proj[:, 0]
        text_features = self.model.extract_features(
            sample, mode="text").text_embeds_proj[:, 0]
        sims = (image_features @ text_features.t())[0] / self.model.temp
        probs = torch.nn.Softmax(dim=0)(sims).tolist()
        res = []
        for i in range(0, 80):
            res.append((probs[i], self.cls_names[i]))
        res = sorted(res, reverse=True)
        return res[0:num_classes]
