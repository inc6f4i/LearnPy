import glob
import os
import time
import cv2
import numpy as np

# 1. 측정 시작
start_total_time = time.time()

# 2. 기본 경로 및 YOLO 모델 설정
base_dir = r"E:\code\learnPy\260722\yolo"
data_dir = os.path.join(base_dir, r"darknet\data")

model_cfg = os.path.join(base_dir, r"darknet\cfg\yolov3.cfg")
model_weights = os.path.join(base_dir, "yolov3.weights")
net = cv2.dnn.readNetFromDarknet(model_cfg, model_weights)
#net = cv2.readNetFromDarknet(model_cfg, model_weights)

# 3. 클래스 및 레이어 설정
classes = []
names_path = os.path.join(data_dir, "coco.names")
with open(names_path, "r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
colors = [(0, 0, 255) if i == 0 else (255, 0, 0) if i == 17 else (0, 0, 0) for i in range(len(classes))]

# 4. 자동 파일 목록 추출 (하드코딩 제거)
video_paths = sorted(glob.glob(os.path.join(data_dir, "*.mp4")))
all_results = []

print(f"🚀 총 {len(video_paths)}개 영상 분석을 시작합니다... (OpenCV CPU 전용)\n")

# 5. 영상 루프
font = cv2.FONT_HERSHEY_SIMPLEX

for idx, video_path in enumerate(video_paths, 1):
    video_name = os.path.basename(video_path)
    print(f"[{idx}/{len(video_paths)}] {video_name} 처리 중...")

    cap = cv2.VideoCapture(video_path)
    
    # 10초 지점 이동
    start_minute, start_second = 0, 10
    start_time_ms = (start_minute * 60 + start_second) * 1000
    cap.set(cv2.CAP_PROP_POS_MSEC, start_time_ms)

    total_frames = 0
    detections_log = []  # (클래스명, 확신도%) 저장용

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        total_frames += 1
        height, width, _ = frame.shape

        # YOLO 입력 이미지 전처리
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # 검출 결과 정리
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # NMS 적용
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.1, 0.4)

        # 통계용 수집 (화면 그리기 포함)
        if len(indexes) > 0:
            for i in indexes.flatten():
                cls_name = str(classes[class_ids[i]])
                conf_percent = confidences[i] * 100
                detections_log.append((cls_name, conf_percent))

                # (원하실 경우 화면 박스 렌더링)
                x, y, w, h = boxes[i]
                color = colors[class_ids[i]]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, f"{cls_name} {conf_percent:.1f}%", (x, y - 10), font, 0.5, color, 1)

        # 💡 화면으로 영상을 보면서 진행하고 싶다면 아래 주석을 해제하세요.
        # cv2.imshow("Object Detection", frame)
        # if cv2.waitKey(1) & 0xFF == 27: break

    cap.release()

    # 분석 데이터 누적
    all_results.append({
        'video_name': video_name,
        'total_frames': total_frames,
        'detections': detections_log
    })

cv2.destroyAllWindows()

# ----------------------------------------------------
# 📌 모든 분석 완료 후 마지막 요약 통계 출력
# ----------------------------------------------------
print("\n" + "=" * 50)
print("              🎉 전체 분석 완료 요약 보고서              ")
print("=" * 50)

for item in all_results:
    video_name = item['video_name']
    total_frames = item['total_frames']
    detections = item['detections']

    print(f"\n📊 [{video_name}] (총 {total_frames} Frame)")
    
    if not detections:
        print("   └─ ⚠️ 탐지된 객체 없음")
        continue

    # 통계 계산
    stats = {}
    for cls_name, conf in detections:
        if cls_name not in stats:
            stats[cls_name] = {'count': 0, 'conf_sum': 0.0}
        stats[cls_name]['count'] += 1
        stats[cls_name]['conf_sum'] += conf

    for cls_name, info in stats.items():
        count = info['count']
        avg_conf = info['conf_sum'] / count
        print(f"   └─ {cls_name:<12}: 총 {count:>4}회 검출 | 평균 확신도: {avg_conf:.2f}%")

print("\n" + "=" * 50)

# 6. 소요 시간 출력
end_total_time = time.time()
total_seconds = end_total_time - start_total_time
minutes = int(total_seconds // 60)
seconds = total_seconds % 60

print(f"⏱️ 전체 총 소요 시간: {minutes}분 {seconds:.2f}초 ({total_seconds:.2f}초)")