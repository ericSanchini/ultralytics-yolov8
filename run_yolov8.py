import torch
import cv2
from ultralytics import YOLO

#load the model
model = YOLO('yolov8x.pt')

#Load the image

img = cv2.imread('C:/Users/erics/Desktop/yolov8/data/images/zidane.jpg')

#perform detection
results = model.predict(image, show=True)

# Extracting results and saving to a text file
results_path = "results.txt"
with open(results_path, "w") as file:
    for result in results.xyxy[0]:
        x1, y1, x2, y2, conf, cls = result
        file.write(f'{x1.item()}, {y1.item()}, {x2.item()}, {y2.item()}, {conf.item()}, {cls.item()}\n')

#Save the image with detection boxes
output_image_path = 'detected_image.jpg'
cv2.imwrite(output_image_path, img)

print(f'Results saved to {results_path} and image saved to {output_image_path}')