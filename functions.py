from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2
import arabic_reshaper



# draw a sentence or a char on a frame
def Draw_arabic_text(frame, coordinate, sentence, font_size, rgb_color):
    fontpath = "arial.ttf"  # For arabic
    font = ImageFont.truetype(fontpath, font_size)
    img_pil = Image.fromarray(frame)  # convert the passed frame to PIL image object
    draw = ImageDraw.Draw(img_pil)  # to draw with PIL's methods
    draw.text(coordinate, sentence, font=font, fill=rgb_color)
    frame = np.array(img_pil)
    return frame


def Add_affect(frame, coordinate1, coordinate2):
    overlay = frame.copy()
    cv2.rectangle(overlay, coordinate1, coordinate2, (255, 255, 255), -1)  # Fill the rectangle with white
    alpha = 1  # Transparency factor
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)


def Formate_arabic_text(captured_letters):
    reversed_text_list = captured_letters[::-1]
    word = ''.join(reversed_text_list )
    formated_sentence = arabic_reshaper.reshape(word)
    return formated_sentence


def Update_sentence(id, captured_letters, predicted_char):
    captured_letters = captured_letters
    if id != 29:
        captured_letters.insert(0, predicted_char)  # take the char
    else:
        del captured_letters[0]
    return captured_letters  # the updated one


# if the current char == previous char , increase shot_counter , else start again , if shot_counter arrived 10 , capture this sign
def Sequence_char_checker(id , char_check_dic , shot_counter):
    char_check_dic['current'] = id
    if char_check_dic['previous'] == char_check_dic['current']:
        shot_counter += 1
    else:
        shot_counter = 0
    char_check_dic['previous'] = char_check_dic['current']
    return char_check_dic , shot_counter






"""
model.names : 
{0: 'ain', 1: 'al', 2: 'aleff', 3: 'bb', 4: 'dal', 5: 'dha', 6: 'dhad', 7: 'fa', 8: 'gaaf', 9: 'ghain', 10: 'ha', 
11: 'haa', 12: 'jeem', 13: 'kaaf', 14: 'khaa', 15: 'la', 16: 'laam', 17: 'meem', 18: 'nun', 19: 'ra', 20: 'saad',
21: 'seen', 22: 'sheen', 23: 'ta', 24: 'taa', 25: 'thaa', 26: 'thal', 27: 'toot', 28: 'waw',
29: 'ya', 30: 'yaa', 31: 'zay'}


{0: 'ع', 1: 'ال', 2: 'ا', 3: 'ب', 4: 'د', 5: 'ظ', 6: 'ض', 7: 'ف', 8: 'ق', 9: 'غ', 10: 'ه', 
11: 'ح', 12: 'ج', 13: 'ك', 14: 'خ', 15: ' ', 16: 'ل', 17: 'م', 18: 'ن', 19: 'ر', 20: 'ص',
21: 'س', 22: 'ش', 23: 'ت', 24: 'ط', 25: 'ث', 26: 'ذ', 27: 'ة', 28: 'و',
29: 'ياء', 30: 'ي', 31: 'ز'}
"""


