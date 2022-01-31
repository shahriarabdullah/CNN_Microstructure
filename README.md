# CNN_Microstructure
**Abdullah Shahriar**<br>
**31.01.2022**<br><br>
A convolutional neural network (initially trained on schematic microstructure) built with TensorFlow to predict if the microstructure belongs to coarse or finer class.


## USAGE
1. Train the model using
```bash
  python train.py
```
2. When training is finished a file named *trained_model.h5* will appear in the same directory
3. Call the *predict.py* script with image file name as argument to predict the result
```bash
  python predict.py test_image.png
```
NOTE: Image file should be in the same directory as the *predicty.py* and *trained_model.h5*). This is specifically designed to run on Windows machine.

The directory structure should be as following-
```
CNN_Microstructure
│   train.py
│   predict.py
│
└───train
│   └───coarse
│       │   image1.png
│       │   image2.png
│       │   ...
│   └───fine
│       │   image1.png
│       │   image2.png
│       │   ...
│   
└───test
│   └───coarse
│       │   image1.png
│       │   image2.png
│       │   ...
│   └───fine
│       │   image1.png
│       │   image2.png
│       │   ...
```

## DETAILS
This model was built with a view to distinguish coarse microstructure image from finer one. After starting the project, I realized there's not enough microstructure images (needed around 1000-4000 images) available for public use to train my model. So I decided to generate schematic coarse and fine microstructures using MicroStructPy, a python library. The train and test dataset was split into 6:1 ratio with very few images (28 images only). So the hyperparameters might change and the model might require tweaking if trained with actual data with a large dataset. (I've a plan to do that if I can manage/create an appropriate dataset). 
All input images has dimension *432x288*. So while prediction, image of same size is required to be fed.

* Hyperparameters were tuned by trial & error and continuous visualization.
* Seed was set for reproducibility.
* The loss curve (seed 45) is-<br>
 ![image](https://user-images.githubusercontent.com/12016642/151752310-1ed902e7-0c9d-4c69-986d-5c7454d44bf6.png)


* The model has the following structure -

![image](https://user-images.githubusercontent.com/12016642/151747008-2cab7dc7-ef86-4ecf-8a94-ec0a8b070eb6.png)


