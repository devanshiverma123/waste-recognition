# Recommending Reusing and Recycling DIY Ideas using Object Recognition

This project focuses on collaboration between various
This project will help you explore various domains like Image Recognition using Convolutional Neural Networks, Computer Vision, Web Scraping and Web Development using Flask. 
The Image Recognition will help identify the waste object in the image with the help of Convolutional Neural Networks. Using OpenCV, a popular library used for solving Computer
Vision problems, the objects can be idenitified in real-time using the web cam of the system. 
Using Web Scraping Module, Reusing and Recycling DIY recommendations will be fetched based on the results produced from the Image Recognition Module(IRM).
Using Flask, these two modules will be combined and using HTML, CSS and Bootstrap, an interface will be created for the user to upload a image and get recommendation results.

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

* Image Preprocessing

The images need to be converted into an array. All the images are converted into 224 x 224 x 3, where 3 represents the RGB channel. We can also use built-in functions to do
the same. The labels of the classes need to be encoded. The data is then divided into training and validation data, with a split of 80% and 20% respectively. The testing is 
done in real-time. 
As the number of images is uneven in every class, it is important that the data is divided into training and validation data in an equal proportion for every class. 

* Building the Model

ResNet50 is a transfer learning model, which is a very deep network. This model has been pre-trained on ImageNet dataset. The ouput layers for this project is different so we 
make a few changes. A drop out layer is introduced to avoid overfitting. Adam optimizer is used with a learning rate of 0.0001. Imagenet weights work well in the model. 


* Training the Model

The model is trained on 50 epochs with a callback function, with the condition of setting the base accuracy as 83%. Once a validation accuracy of 83% is achieved, the model
will stop training if in any epoch, the accuracy goes below this point.

* Testing the Model

With this aspect of the project, we venture into the Computer Vision domain. Using the ability of the computer to "see", the input image is classified into various waste classes.
Once the model is trained, the testing of the model is done in real-time using OpenCV. The webcam is used to capture the image. A mask is created to enclose the object that 
needs to be detected. The results are stored and also displayed back on the screen. The results are stored in the form of string so that they can further be used in the 
Web Scraping Module to get reusing and recycling DIY recommendations.
![alt text](https://github.com/[devanshiverma123]/[waste-recognition]/blob/r4 (2).png?raw=true)

## Web Scraping Module

Web Scraping is done using Python. 

