from ScreenProcessor import *
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from matplotlib import pyplot as plt
from skimage import transform
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split
import PIL.ImageOps
try:
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

except:
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
# creating an image object



def get_card_info():
    im1 = cv2.imread("./assets/image1.png")
    height, width, channels = im1.shape
    print(height, width)
    # ROI = image[y1:y2, x1:x2]
    ai_card_region_img = im1[math.floor(height*10/100):math.floor(height*80/100),
                             math.floor(width*5/100):math.floor(width*10.5/100)]

    ai_area_h, ai_area_w, channels = ai_card_region_img.shape
    computer_card1 = ai_card_region_img[math.floor(ai_area_h*2/100):math.floor(ai_area_h*18/100),
                                        math.floor(ai_area_w*20/100):math.floor(ai_area_w)]
    computer_card2 = ai_card_region_img[math.floor(ai_area_h*22/100):math.floor(ai_area_h*37/100),
                                        math.floor(ai_area_w*20/100):math.floor(ai_area_w)]
    computer_card3 = ai_card_region_img[math.floor(ai_area_h*42/100):math.floor(ai_area_h*57/100),
                                        math.floor(ai_area_w*20/100):math.floor(ai_area_w)]
    computer_card4 = ai_card_region_img[math.floor(ai_area_h*62/100):math.floor(ai_area_h*77/100),
                                        math.floor(ai_area_w*20/100):math.floor(ai_area_w)]
    computer_card5 = ai_card_region_img[math.floor(ai_area_h*81/100):math.floor(ai_area_h*96/100),
                                        math.floor(ai_area_w*20/100):math.floor(ai_area_w)]

    computer_card_array = [computer_card1,
                           computer_card2,
                           computer_card3,
                           computer_card4,
                           computer_card5]
    s = 0
    for i in computer_card_array:
        s = s + 1
        cv2.imshow('card', i)
        cv2.imwrite('./assets/computercard{}.png'.format(s), i)
        cv2.waitKey(0)

    player_card_region_img = im1[math.floor(height*10/100):math.floor(height*80/100),
                                 math.floor(width*75/100):math.floor(width*83.5/100)]

    player_area_h, player_area_w, channels = player_card_region_img.shape

    player_card1 = player_card_region_img[math.floor(player_area_h*2/100):math.floor(player_area_h*18/100),
                                          0:math.floor(player_area_w)]
    player_card2 = player_card_region_img[math.floor(player_area_h*22/100):math.floor(player_area_h*37/100),
                                          0:math.floor(player_area_w)]
    player_card3 = player_card_region_img[math.floor(player_area_h*42/100):math.floor(player_area_h*57/100),
                                          0:math.floor(player_area_w)]
    player_card4 = player_card_region_img[math.floor(player_area_h*62/100):math.floor(player_area_h*77/100),
                                          0:math.floor(player_area_w)]
    player_card5 = player_card_region_img[math.floor(player_area_h*81/100):math.floor(player_area_h*96/100),
                                          0:math.floor(player_area_w)]

    player_card_array = [player_card1,
                         player_card2,
                         player_card3,
                         player_card4,
                         player_card5]

    s = 0
    for i in player_card_array:
        s = s + 1
        cv2.imshow('card', i)
        cv2.imwrite('./assets/playercard{}.png'.format(s), i)
        cv2.waitKey(0)

def predictimage(file):
    #Load in the query instance
    img = Image.open(file)
    img =img.convert("L")
    img =PIL.ImageOps.invert(img)
    img =img.resize((32,32), Image.ANTIALIAS)
    imgplot =plt.imshow(img)


    query=np.array(img).flatten()
    query=(query/16).round()



    #Plot query digit
    plt.imshow(query.reshape((32,32)))

    #Load in the training dataset

    digits=datasets.load_digits()
    features=digits.data
    targets=digits.target

    #Expand 8*8 image to a 32*32 image (64 to 1024)
    newfeatures=[transform.resize(features[i].reshape(8,8),(32,32)) for i in range(len(features))]
    newfeatures=np.array(newfeatures).reshape((1797,1024)).round()


    #Instantiate, Train and predict
    clf=svm.SVC(gamma=0.001,C=100)
    clf.fit(newfeatures,targets)

    prediction=clf.predict(query)

    plt.show()
    return prediction

def classification():
    digits=datasets.load_digits()
    features=digits.data
    targets=digits.target
    # flatten the images
    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))

    # Create a classifier: a support vector classifier
    clf = svm.SVC(gamma=0.001)

    # Split data into 50% train and 50% test subsets
    X_train, X_test, y_train, y_test = train_test_split(
        data, digits.target, test_size=0.5, shuffle=False)

    # Learn the digits on the train subset
    clf.fit(X_train, y_train)

    # Predict the value of the digit on the test subset
    predicted = clf.predict(X_test)
    print(predicted)
    _, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
    for ax, image, prediction in zip(axes, digits.images, predicted):
        ax.set_axis_off()
        ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        ax.set_title(f'Prediction: {prediction}')

    plt.show()
    return
# print(predictimage("./assets/computercard1.png"))
classification()