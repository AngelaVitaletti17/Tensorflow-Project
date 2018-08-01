import tensorflow as tf
import numpy as np
import wget
import os
import subprocess
import re

#This script will use a tutorial found on douglasduhaime.com
#It will be a continuation of my tensorflow practices with my own exercise

#The goal of this script is to preform an experiment:

'''
Given a source image of a house with a known price, can we do the following:
1. Use tensorflow image recognition to find similiar houses in a set of images
	a. How will tensorflow indentify similarities?
2. Once we have found similar images, determine how similar they are to the original
3. Using this percentage, calculate an assumed price using basic mathematics
4. Perform training on a model using these data points to determine a function for
   linear regression
5. Compare: What are the actual prices of the houses?
'''
#First we need to borrow a script as stated in the tutorial
#THIS IS NOT ENTIRELY MY SCRIPT

targetHousePath = os.getcwd()
targets = []
if not os.path.isfile(os.path.join(targetHousePath, "classify_image.py")):
	file = wget.download('https://raw.githubusercontent.com/tensorflow/models/master/tutorials/image/imagenet/classify_image.py')

for file in os.listdir(targetHousePath):
	if os.path.isfile(os.path.join(targetHousePath, file)) and file.endswith('.jpg'):
		targets.append(file)

#Update: So as it turns out, the tutorial finds similarities between different images, not just matches to an original
#For now, we will do that, but keep in mind that the first image will be the known price house.

#Note: First image is $599,999 @ 2,975 sqft
#Note 2: I chose not to make the modifications listed in the tutorial for simplicity; I may change this later

#output = os.system("python classify_image.py *.jpg")
output = subprocess.check_output(['python', 'classify_image.py', '*.jpg'], shell=True)
regex = re.findall('score = (.+?)\)', output.decode("utf-8"))

#Now that we have similarity indices, let's compute some stuff
