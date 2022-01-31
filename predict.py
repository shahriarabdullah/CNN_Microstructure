from sys import argv
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import cv2

file_path = os.path.abspath(os.path.dirname(__file__))
model=tf.keras.models.load_model(file_path+"\\trained_model.h5")

def main(filename=file_path+"\\"+argv[1]):
    img = tf.keras.preprocessing.image.load_img(filename,target_size=(432,288))
    
    plt.imshow(img)
 
    Y = tf.keras.preprocessing.image.img_to_array(img)
    
    X = np.expand_dims(Y,axis=0)
    val = model.predict(X)
    print(val)
    if val == 1:
        print("FINE MICROSTRUCTURE")
        plt.xlabel("FINE",fontsize=20)
        
    
    elif val == 0:
        print("COARSE MICROSTRUCTURE")
        plt.xlabel("COARSE",fontsize=20)

if __name__ == "__main__":
    main()