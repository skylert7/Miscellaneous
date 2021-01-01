from ScreenProcessor import *
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
try:
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

except:
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
# creating an image object
im1 = cv2.imread("image1.png")
height, width, channels = im1.shape
print(height, width)
# ROI = image[y1:y2, x1:x2]
ai_card_region_img = im1[math.floor(height*10/100):math.floor(height*80/100),
                         math.floor(width*5/100):math.floor(width*10.5/100)]

ai_area_h, ai_area_w, channels = ai_card_region_img.shape
computer_card1 = ai_card_region_img[0:math.floor(ai_area_h*18/100),
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

# for i in computer_card_array:
#     cv2.imshow('card', i)
#     cv2.waitKey(0)

player_card_region_img = im1[math.floor(height*10/100):math.floor(height*80/100),
                             math.floor(width*75/100):math.floor(width*83.5/100)]

player_area_h, player_area_w, channels = player_card_region_img.shape

player_card1 = player_card_region_img[0:math.floor(player_area_h*18/100),
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

# for i in player_card_array:
#     cv2.imshow('card', i)
#     cv2.waitKey(0)
computer_card1 = cv2.cvtColor(computer_card1, cv2.COLOR_BGR2GRAY)
cv2.imshow('computer_card1', computer_card1)
cv2.waitKey(0)
text = pytesseract.image_to_string(computer_card1,  config='digits')
print(text)