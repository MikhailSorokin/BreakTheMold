import io
from google.cloud import vision
from google.cloud.vision import types

import numpy as np
import argparse
import requests

def getFungusStatus(labels):
	status = 0
	for label in labels:
		print(label.description)
		if ("mold" in label.description or "fung" in label.description):
			status = 1

	return status



def create_ImageRequest(bStatus, colorList):
	payload = {}
	payload['fungusStatus'] = bStatus
	payload['colors'] = []
	for (color in colorList):
		payload['colors'].append({
		    'color': color
		})

	print(json.dumps(payload)))

    #makeImageRequest = requests.post('https://slewando.wixsite.com/',
	#		json.dumps(payload))

	print(makeImageRequest.url)
	#makeImageRequest = requests.post('https://slewando.wixsite.com/', data = {'key': 'val'})

    #print(makeImageRequest.url)
# [END create_instance]

if __name__ == '__main__':
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

	status = getFungusStatus(labels)

	# Detect the color
	response = vision_client.image_properties(image=image)
	props = response.image_properties_annotation
	print('Color properties:')

	colorList = []
	color_amnt_percentage = 0.10
	for color in props.dominant_colors.colors:
		if (color.pixel_fraction >= color_amnt_percentage):
			colorList.append(color.color)

	print(colorList)

	create_ImageRequest(status, colorList)
