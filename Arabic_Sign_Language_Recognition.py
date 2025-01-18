import cv2
from ultralytics import YOLO
import functions

# we got these weights from training YOLO model on custom dataset on kaggle
yolo_model = YOLO('best_ASL.pt')  # Replace with your model path

yolo_names = yolo_model.names
print(yolo_names[27])

# we will rename this keys with arabic letters and some words
yolo_arabic_index = {0: 'ع', 1: 'ال', 2: 'ا', 3: 'ب', 4: 'د', 5: 'ظ', 6: 'ض', 7: 'ف', 8: 'ق', 9: 'غ', 10: 'ه',
 11: 'ح', 12: 'ج', 13: 'ك', 14: 'خ', 15: ' ', 16: 'ل', 17: 'م', 18: 'ن', 19: 'ر', 20: 'ص',
 21: 'س', 22: 'ش', 23: 'ت', 24: 'ط', 25: 'ث', 26: 'ذ', 27: 'مرحبا بكم', 28: 'و',
 29: '', 30: 'ي', 31: 'ز'}  # to build words and sentences

yolo_arabic_names = {0: 'ع', 1: 'ال', 2: 'ا', 3: 'ب', 4: 'د', 5: 'ظ', 6: 'ض', 7: 'ف', 8: 'ق', 9: 'غ', 10: 'ه',
                     11: 'ح', 12: 'ج', 13: 'ك', 14: 'خ', 15: 'مسافه', 16: 'ل', 17: 'م', 18: 'ن', 19: 'ر', 20: 'ص',
                     21: 'س', 22: 'ش', 23: 'ت', 24: 'ط', 25: 'ث', 26: 'ذ', 27: 'مرحبا بكم', 28: 'و',
                     29: 'مسح', 30: 'ي', 31: 'ز'} # to show them above bounding box

captured_letters = []   # contains all the captured chars
formatted_sentence = ''   # after connecting captured arabic letters
shot_counter = 0
char_check_dic = {'previous':0 ,'current':0}  # previous and current char id and are assigned to dummy values

#######################################################################################################################

cap = cv2.VideoCapture(0)
cap.set(3,1200)     # set the width and high of the window
cap.set(4,720)

while True:
    ret, frame = cap.read()

    yolo_result = yolo_model.predict(frame, device='cuda')

    # draw arabic text on frame , return the drawn frame
    frame =  functions.Draw_arabic_text(frame , (100,20) , formatted_sentence , 35 , (0,255,255))


    if len(yolo_result[0].boxes.xyxy) > 0:  # Ensure there are detected boxes
        boxes = yolo_result[0].boxes.xyxy
        class_ids = [int(i) for i in yolo_result[0].boxes.cls]
        confidence = [float(i) for i in yolo_result[0].boxes.conf]

        # Loop through detected boxes and draw them
        for box,conf,id in zip(boxes, confidence, class_ids):
            x1, y1, x2, y2 = map(int, box)  # Convert coordinates to integers
            char_on_box = yolo_arabic_names[id]
            predicted_char = yolo_arabic_index[id]

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 3)  # Draw the bounding box
            # draw char on bounding box
            word_on_box = functions.reshape(char_on_box)
            
            frame = functions.Draw_arabic_text(frame, (x1 , y1 - 50), word_on_box, 45, (0, 0, 0))
            # do we capture the sign based on shot_counter(number of same sequential sign frames)  or not ?
            char_check_dic , shot_counter = functions.Sequence_char_checker(id , char_check_dic, shot_counter)

            if shot_counter >= 12 :  # if the same sign (same letter) is in 15 sequential frames
                # take this hand sign(letter) , then update the entire captured letters
                captured_letters = functions.Update_sentence(id , captured_letters ,predicted_char)  # add or remove char from list ?
                # update predicted word
                formatted_sentence  = functions.Formate_arabic_text(captured_letters)
                # add affect on bounding box when capturing the sign
                functions.Add_affect(frame,(x1,y1),(x2,y2))
                shot_counter = 0

    if cv2.waitKey(1) == ord('q'):
        break

    cv2.waitKey(1)
    cv2.imshow('Arabic Sign language (ASL)', frame)

print(f'The predicted word : {formatted_sentence}')

cap.release()
cv2.destroyAllWindows()
