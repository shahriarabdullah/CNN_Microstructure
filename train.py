import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import cv2

tf.random.set_seed(45)
file_path = os.path.abspath(os.path.dirname(__file__)) #Gets current directory of the script
train = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1/255)
test = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1/255)

train_dataset = train.flow_from_directory(file_path+"\\train\\",
                                          target_size=(432,288),
                                          batch_size = 2,
                                          class_mode = 'binary')
                                         
test_dataset = test.flow_from_directory(file_path+"\\test\\",
                                          target_size=(432,288),
                                          batch_size =2,
                                          class_mode = 'binary')

test_dataset.class_indices

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(8,(3,3),activation='relu',input_shape=(432,288,3)),
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Conv2D(16,(3,3),activation='relu'),
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Conv2D(32,(3,3),activation='relu'),
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Conv2D(32,(3,3),activation='relu'),
    tf.keras.layers.MaxPool2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dense(1,activation='sigmoid')

])	

model.compile(
    loss=tf.keras.losses.BinaryCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(),
    metrics=["accuracy"]
)

history=model.fit_generator(train_dataset,
         steps_per_epoch = 12,
         epochs = 10,
         validation_data = test_dataset
         )

model.save(file_path+"\\trained_model.h5")

pd.DataFrame(history.history).plot()
