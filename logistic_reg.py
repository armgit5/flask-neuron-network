# -*- coding: utf-8 -*-

import pickle
from functions import predict
from scipy import ndimage
import numpy as np
import scipy
import matplotlib.pyplot as plt

## Read Model
file = open("model.pickle", "rb")
d = pickle.load(file)

## Predict fuction
def predictImage(imageName):
    
    num_px = 64
    my_image = imageName   # change this to the name of your image file 
    ## END CODE HERE ##
    
    # We preprocess the image to fit your algorithm.
    fname = "images/" + my_image
    image = np.array(ndimage.imread(fname, flatten=False))
    my_image = scipy.misc.imresize(image, size=(num_px,num_px)).reshape((1, num_px*num_px*3)).T
    my_predicted_image = predict(d["w"], d["b"], my_image)
    # plt.imshow(my_image.reshape((num_px, num_px, 3)))
    output = int(np.squeeze(my_predicted_image))
    print(output)
    if (output == 1):
        print("the picture is a cat")
    else:
        print("it's not a cat")
    
#predictImage("cat.jpg")