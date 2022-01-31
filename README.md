# CNN_Microstructure
**Abdullah Shahriar**<br>
<br>
A convolutional neural network (initially trained on schematic microstructure) built with TensorFlow to predict if the microstructure belongs to coarse or finer class.


## USAGE

To run the model virtually, [Click here](https://github.com/shahriarabdullah/CNN_Microstructure/blob/main/GoogleColab/CNN_Microstructure_Final.ipynb). Open this in GoogleColab and you can run easily.

If you are using a Windows machine, follow this-

1. Train the model using
```bash
  python train.py
```
2. When training is finished a file named *trained_model.h5* will appear in the same directory
3. Call the *predict.py* script with image file name as argument to predict the result
```bash
  python predict.py test_image.png
```
**NOTE:** Image file should be in the same directory as the *predicty.py* and *trained_model.h5*). This is specifically designed to run on Windows machine. 

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

## RESULT
* When fed with an unseen coarse grain microstructure, the output was-<br>
![image](https://user-images.githubusercontent.com/12016642/151815678-e0584fe0-7785-4a72-93a0-5a1c084de7c6.png)
* When fed with an unseen fine grain microstructure, the output was-<br>
* ![image](https://user-images.githubusercontent.com/12016642/151815835-e6dec89a-b384-4640-bf5e-d27c168f9f4c.png)



## DETAILS
This model was built with a view to distinguish coarse microstructure image from finer one. After starting the project, I realized there's not enough microstructure images (needed around 1000-4000 images) available for public use to train my model. So I decided to generate schematic coarse and fine microstructures using MicroStructPy, a python library. The train and test dataset was split into 10:3 ratio with very few images (78 images only). So the hyperparameters might change and the model might require tweaking if trained with actual data with a large dataset. (I've a plan to do that if I can manage/create an appropriate dataset). 
All input images has dimension *432x288*. So while prediction, image of same size is required to be fed.

* Hyperparameters were tuned by trial & error and continuous visualization.
* Seed was set for reproducibility.
* The loss curve (seed 45) is-<br>
 ![image](https://user-images.githubusercontent.com/12016642/151816630-59be2927-96ee-438d-9f73-bb3d864d2d03.png)


* The model summary - <br>
```
Model: "sequential_1"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d_16 (Conv2D)          (None, 430, 286, 8)       224       
                                                                 
 max_pooling2d_16 (MaxPoolin  (None, 215, 143, 8)      0         
 g2D)                                                            
                                                                 
 conv2d_17 (Conv2D)          (None, 213, 141, 16)      1168      
                                                                 
 max_pooling2d_17 (MaxPoolin  (None, 106, 70, 16)      0         
 g2D)                                                            
                                                                 
 conv2d_18 (Conv2D)          (None, 104, 68, 32)       4640      
                                                                 
 max_pooling2d_18 (MaxPoolin  (None, 52, 34, 32)       0         
 g2D)                                                            
                                                                 
 conv2d_19 (Conv2D)          (None, 50, 32, 32)        9248      
                                                                 
 max_pooling2d_19 (MaxPoolin  (None, 25, 16, 32)       0         
 g2D)                                                            
                                                                 
 flatten_4 (Flatten)         (None, 12800)             0         
                                                                 
 dense_8 (Dense)             (None, 128)               1638528   
                                                                 
 dense_9 (Dense)             (None, 1)                 129       
                                                                 
=================================================================
Total params: 1,653,937
Trainable params: 1,653,937
Non-trainable params: 0
_________________________________________________________________
```
* Structure in graphical form <br><br>
![image](https://user-images.githubusercontent.com/12016642/151747008-2cab7dc7-ef86-4ecf-8a94-ec0a8b070eb6.png)


