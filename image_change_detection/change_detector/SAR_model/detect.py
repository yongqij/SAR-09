from change_detector.SAR_model import make_test_sample
from change_detector.SAR_model.model import inference
import os

def process_images():
    make_test_sample.main()
    inference.main()