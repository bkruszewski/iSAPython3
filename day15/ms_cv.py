# Microsoft Cognitive services
#
# https://azure.microsoft.com/en-us/services/cognitive-services/
# Get API key: https://azure.microsoft.com/en-us/try/cognitive-services/?api=computer-vision
# CV API Documentation: https://goo.gl/sc2Rb3

import json
import os
import requests


api_key = "3e144c5294d645269b5982201687b3bd"
api_url = "https://westeurope.api.cognitive.microsoft.com/vision/v1.0/analyze"

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': api_key
}

param = {
    'visualFeatures': 'Categories,Description,Faces,Adult',
    'details': 'Celebrities'
}


def get_pic_info(pic_url, pic_name):
   pass


def has_faces(data: dict):
    pass


def get_face_rect(face_data: dict):
    pass


def get_caption(data):
    pass
