# Recommending Reusing and Recycling DIY Ideas using Object Recognition

With the easily availability and low cost of resources, the rate of waste production is constantly on the rise. Through our project we aim to slow down the rate of this waste production by engaging the user creatively. Our project provides a waste object recognition system and a recommendation system.
Through this project we experimented with various domains like Deep Learning, Computer Vision and a Recommender System. We brought them together through a web application using the Flask framework.

There are two main modules:
1. The Image Recognition Module consists of the Convolutional Neural Network which is trained on about 11000 images in order to classify waste objects into various classes. Further, the webcam of the computer system is used to capture the frame and identify objects in real time. 

2. In the Web Scraping Module, using the results from the Image Recognition Module, recommendations are made to the user to engage them creatively. The recommendations include DIY reusing ideas that aim at engaging the user creatively.

<img src="https://github.com/devanshiverma123/waste-recognition/blob/master/WSM1.png" width="600" height="350"/>

<img src="https://github.com/devanshiverma123/waste-recognition/blob/master/1.jpg" width="600" height="350"/>

## Image Recogntion Module

* Dataset Collection
The dataset consists of about 11000 images which are collected from various sources like TrashNet, Kaggle Dataset on Waste Objects and ImageNet. These images were classified into
12 classes on the basis of the requirement of the project. The organisation of the data is as follows-

|  Class          |  Number of Images  |
|  --- |  ---  |
|  Bottle         |  874               |
|  Cans           |  982               |
|  Cardboard      |  1061              |
|  Cups           |  614               |
|  Cutlery        |  996               |
|  Jars           |  1012              |
|  Accessories    |  1026              |
|  Organic Waste  |  1213              |
|  Paper          |  1008              |
|  Plastic Bag    |  671               |
|  Stationary     |  1309              |
|  Utensil        |  930               |

Due to less data, data augmentation is performed which will help to generalise the model better.  


<img src="https://github.com/devanshiverma123/waste-recognition/blob/master/Data%20Distribution.png" width="600" height="350"/>

<img src="https://github.com/devanshiverma123/waste-recognition/blob/master/cb1.png" width="600" height="350"/>


* Image Preprocessing

The images need to be converted into an array. All the images are converted into 224 x 224 x 3, where 3 represents the RGB channel. We can also use built-in functions to do
the same. The labels of the classes need to be encoded. The data is then divided into training and validation data, with a split of 80% and 20% respectively. The testing is 
done in real-time. 
As the number of images is uneven in every class, it is important that the data is divided into training and validation data in an equal proportion for every class. 


<img src="https://github.com/devanshiverma123/waste-recognition/blob/master/cb3.PNG" width="600" height="350"/>

* Building the Model

ResNet50 is a transfer learning model, which is a very deep network. This model has been pre-trained on ImageNet dataset. The ouput layers for this project is different so we 
make a few changes. A drop out layer is introduced to avoid overfitting. Adam optimizer is used with a learning rate of 0.0001. Imagenet weights work well in the model. 


* Training the Model

The model is trained on 50 epochs with a callback function, that will stop training the model if the validation accuracy decreases consecutively for 3 epochs. 

* Testing the Model

With this aspect of the project, we venture into the Computer Vision domain. Using the ability of the computer to "see", the input image is classified into various waste classes.
Once the model is trained, the testing of the model is done in real-time using OpenCV. The webcam is used to capture the image. A mask is created to enclose the object that 
needs to be detected. The results are stored and also displayed back on the screen. The results are stored in the form of string so that they can further be used in the 
Web Scraping Module to get reusing and recycling DIY recommendations.

<img src="https://github.com/devanshiverma123/waste-recognition/blob/master/r5%20(2).png" width="600" height="350"/>

<img src="https://github.com/devanshiverma123/waste-recognition/blob/master/r4%20(2).png" width="600" height="350"/>

* Results

The best model has the training accuracy of 93.63% and validation accuracy of 87.48%.

<img src="https://github.com/devanshiverma123/waste-recognition/blob/master/Accuracy.png" width="600" height="350"/>

<img src="https://github.com/devanshiverma123/waste-recognition/blob/master/Loss.png" width="600" height="350"/>


## Web Scraping Module

Web Scraping is done using Python and then a recommendation is made to the user. The recommendation provides reusing and recycling DIY ideas. The aim is to reduce the rate of waste production.

