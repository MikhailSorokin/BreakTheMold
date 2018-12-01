import io
from google.cloud import vision
from google.cloud.vision import types

import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

#Detect the image and then use google cloud's vision API

vision_client = vision.ImageAnnotatorClient()
file_name = args["image"]

with io.open(file_name, 'rb') as image_file:
	content = image_file.read()

image = types.Image(content=content)

response = vision_client.label_detection(image=image)
labels = response.label_annotations

for label in labels:
	print(label.description)

# Detect the color
props = response.image_properties_annotation
print('Properties:')

colorAnnotations = types.DominantColorsAnnotation()
for color in colorAnnotations.colors:
	print('fraction: {}'.format(color.pixel_fraction))

for color in props.dominant_colors.colors:
	print('fraction: {}'.format(color.pixel_fraction))
	print('\tr: {}'.format(color.color.red))
	print('\tg: {}'.format(color.color.green))
	print('\tb: {}'.format(color.color.blue))
	print('\ta: {}'.format(color.color.alpha))
