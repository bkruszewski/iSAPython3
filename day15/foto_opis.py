# Describes picture with data received form Microsoft CV Api

import json
import os
from PIL import Image, ImageDraw, ImageFont


def describe_picture(image, img_data):
    """
    Creates copy of image with information from data(json)
    :param image: Image
    :param img_data: Json information about image
    :return: None
    """
    with Image.open(image) as img:
        assert isinstance(img, Image.Image)

        temp = img.copy()
        drawer = ImageDraw.ImageDraw(temp)

        for i, face in enumerate(img_data['faces']):
            print(f'Checking face {i + 1}')

            face_rect = get_face_rect(face)
            drawer.rectangle(face_rect)

            # prepare font for face info
            f_size = round((face_rect[3] - face_rect[1]) / 8)
            text_font = ImageFont.truetype("arial.ttf", f_size)

            # print face info
            face_description = f"Płeć: {face['gender']},\nwiek: {face['age']}"
            drawer.text((face_rect[0], face_rect[1] - f_size * 2),
                        face_description, font=text_font, fill=(123,104,238))

        # caption - font 1/25 of img height
        t_size = round(img_data['metadata']['height'] / 25)
        cap_font = ImageFont.truetype("calibri.ttf", t_size)
        drawer.text((20, 20), f"{get_caption(img_data)}", font=cap_font, fill=(41, 178, 39))

        file_ext = os.path.splitext(image)
        described_pic = f"{file_ext[0]}_faces{file_ext[1]}"
        with open(described_pic, 'wb') as faces_file:
            temp.save(faces_file)


def main():
    # test
    with open("response2.json") as file:
        pic_data = json.load(file)

    if has_faces(pic_data):
        print('Checking faces on image...')
        describe_picture("pic2.jpg", pic_data)
        print('Done.')
    else:
        print('No faces!')


if __name__ == '__main__':
    main()
