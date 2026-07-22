#################################################venv

import cv2
import numpy as np

# YOLO 모델 및 설정 파일 경로 (실제 경로로 변경 필요)
model_cfg = r"E:\code\learnPy\260716\yolo\darknet\cfg\yolov3.cfg"
model_weights = r"E:\code\learnPy\260716\yolo\yolov3.weights" #객체 탐지 성능을 좌우함
net = cv2.dnn.readNetFromDarknet(model_cfg, model_weights) #

# 클래스 이름 파일 (coco names)
classes = []
with open(r"E:\code\learnPy\260716\yolo\darknet\data\coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
colors = [(0, 0, 255)] # 바운딩 박스 색깔 (빨간색)

# 비디오 캡쳐 또는 이미지 읽기
#cap = cv2.VideoCapture(r"E:\code\learnPy\260716\yolo\darknet\data\highway.mp4") # 또는 cv2.imread("image.jpg")
cap = cv2.VideoCapture(0) # 또는 cv2.imread("image.jpg")
while True:
    ret, frame = cap.read() # 또는 frame = 이미지
    if not ret: break

    height, width, channels = frame.shape

    # YOLO 입력으로 사용할 이미지 전처리 (크기 조정, 정규화 등)
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # 검출 결과 처리
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5: # 신뢰도 0.5 이상만 검출
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Non-Maximum Suppression (겹치는 바운딩 박스 제거)
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # 검출된 객체 화면에 표시
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[0] # 빨간색
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, label, (x, y - 10), font, 0.5, color, 1)

    cv2.imshow("Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == 27: # ESC 키 종료
        break

cap.release()
cv2.destroyAllWindows()