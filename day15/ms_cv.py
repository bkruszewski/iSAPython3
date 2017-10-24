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
    body = {'url': f'{pic_url}'}

    r = requests.post(api_url, json=body, headers=headers, params=param)
    r.raise_for_status()
    response_json = json.loads(r.text)

    f_info = os.path.splitext(pic_name)

    with open(f"{f_info[0]}.json", 'w') as file:
        json.dump(response_json, file, indent=4, ensure_ascii=False)

    return response_json


def has_faces(data: dict):
    if len(data['faces']) != 0:
        return True
    else:
        return False


def get_face_rect(face_data: dict):
    rect = face_data['faceRectangle']

    return [rect['left'],
            rect['top'],
            rect['left'] + rect['width'],
            rect['top'] + rect['height']
            ]


def get_caption(data):
    captions = data['description']['captions']

    if len(captions) > 0:
        return captions[0]['text']
    else:
        return "No caption"


def main():
    print("Uruchom plik foto_opis.py (jedno zdjęcie przykładowe), "
          "lub plik opisuj_fotki z kilkoma zdjęciami :)")


if __name__ == '__main__':
    main()
