import tensorflow as tf
import numpy as np
from keras.applications.resnet50 import preprocess_input
import pickle

def get_prediction(image_file):
    pkl_filename = 'mainmodel.pkl'
    with open(pkl_filename, 'rb') as file:
        model = pickle.load(file)
    image = tf.keras.preprocessing.image.load_img(
        image_file, target_size=(224,224)
    )
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.array(image)
    image = np.expand_dims(image, axis = 0)
    image = preprocess_input(image)

    prediction = model.predict(image)
    class_prediction = np.argmax(prediction)
    waste_classes = {
    '0' : 'Book/Magazine',
    '1' : 'Cardboard',
    '2' : 'Cutlery/Utensils',
    '3' : 'Electrical Device',
    '4' : 'Glass Bottle',
    '5' : 'Glass Jar',
    '6' : 'Metal Cans',
    '7' : 'Newspaper',
    '8' : 'Paper',
    '9' : 'Plastic Bag',
    '10' : 'Plastic Bottle',
    '11' : 'Plate/ Tray',
    '12' : 'Toiletry',
    '13' : 'Vegetable/Fruit'
     }
    result = [v for k,v in waste_classes.items() if k== str(class_prediction)][0]
    accuracy = prediction[0][class_prediction]*100
    return result,accuracy
