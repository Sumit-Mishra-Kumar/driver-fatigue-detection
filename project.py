import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import uuid   # Unique identifier
import os
import time

# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# # cap = cv2.VideoCapture(0)
# # while cap.isOpened():
# #     ret, frame = cap.read()
# #     results = model(frame)
    
# #     cv2.imshow('YOLO', np.squeeze(results.render()))
    
# #     if cv2.waitKey(10) & 0xFF == ord('q'):
# #         break
# # cap.release()
# # cv2.destroyAllWindows()
# IMAGES_PATH = os.path.join('data', 'images') #/data/images
# labels = ['awake', 'drowsy']
# number_imgs = 20
# cap = cv2.VideoCapture(0)
# # Loop through labels
# for label in labels:
#     print('Collecting images for {}'.format(label))
#     time.sleep(5)
#         # Loop through image range
#     for img_num in range(number_imgs):
#         print('Collecting images for {}, image number {}'.format(label, img_num))
#         # Webcam feed
#         ret, frame = cap.read()
#         # Naming out image path
#         imgname = os.path.join(IMAGES_PATH, label+'.'+str(uuid.uuid1())+'.jpg')
#         # Writes out image to file 
#         cv2.imwrite(imgname, frame)
        
#         # Render to the screen
#         cv2.imshow('Image Collection', frame)
        
#         # 2 second delay between captures
#         time.sleep(2)
        
#         if cv2.waitKey(10) & 0xFF == ord('q'):
#             break
# cap.release()
# cv2.destroyAllWindows()
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp/weights/best.pt', force_reload=True)
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)
    
    cv2.imshow('YOLO', np.squeeze(results.render()))
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()