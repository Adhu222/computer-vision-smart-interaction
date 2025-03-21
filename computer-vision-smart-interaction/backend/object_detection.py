import cv2
import torch
from ultralytics import YOLO

MODEL_PATH = "models/yolov8n.pt"  # Pretrained YOLOv8 model
OUTPUT_FOLDER = "static"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

model = YOLO(MODEL_PATH)

def detect_objects(image_path):
    image = cv2.imread(image_path)
    results = model(image)[0]

    for box in results.boxes.xyxy:
        x1, y1, x2, y2 = map(int, box[:4])
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    output_path = os.path.join(OUTPUT_FOLDER, "detected.jpg")
    cv2.imwrite(output_path, image)
    return output_path
