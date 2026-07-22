import glob
import os
import time
from ultralytics import YOLO

# 1. 측정 시작
start_total_time = time.time()

# 2. 모델 및 경로 설정
model = YOLO("yolov8n.pt")
data_dir = r"E:\code\learnPy\260716\yolo\darknet\data"
video_paths = sorted(glob.glob(os.path.join(data_dir, "*.mp4")))

# 3. 통계 함수
def print_video_stats(video_name, total_frames, detections):
    print(f"\n==========================================")
    print(f"📊 [{video_name}] 탐지 결과 요약 통계")
    print(f"==========================================")
    print(f"• 총 분석 프레임: {total_frames} Frame")
    
    if not detections:
        print("• 탐지된 객체 없음")
        print(f"==========================================\n")
        return

    stats = {}
    for cls_name, conf in detections:
        if cls_name not in stats:
            stats[cls_name] = {'count': 0, 'conf_sum': 0.0}
        stats[cls_name]['count'] += 1
        stats[cls_name]['conf_sum'] += conf

    print(f"• 탐지된 객체 종수: {len(stats)}종")
    print("-" * 42)
    for cls_name, info in stats.items():
        count = info['count']
        avg_conf = info['conf_sum'] / count
        print(f"  - {cls_name:<12}: 총 {count:>4}회 검출 | 평균 확신도: {avg_conf:.2f}%")
    print(f"==========================================\n")


# 4. 영상별 추론 및 통계 수집
for video_path in video_paths:
    video_name = os.path.basename(video_path)
    
    # stream=True로 프레임 단위 처리
    results = model.predict(source=video_path, device=0, conf=0.25, stream=True)
    
    total_frames = 0
    detections_log = []  # (클래스명, 확신도%) 저장용

    for result in results:
        total_frames += 1
        boxes = result.boxes  # 이미 NMS가 완료된 박스들
        
        # 📌 기존의 if len(indexes) > 0: 역할을 수행
        if len(boxes) > 0:
            for box in boxes:
                cls_id = int(box.cls[0])
                cls_name = model.names[cls_id]
                conf_percent = float(box.conf[0]) * 100
                
                # 통계용 데이터 저장
                detections_log.append((cls_name, conf_percent))

    # 영상 1개 종료 시 통계 함수 호출
    print_video_stats(video_name, total_frames, detections_log)


# 5. 시간 측정 종료
end_total_time = time.time()
total_seconds = end_total_time - start_total_time

minutes = int(total_seconds // 60)
seconds = total_seconds % 60

print(f"\n⏱️ 전체 총 소요 시간: {minutes}분 {seconds:.2f}초 ({total_seconds:.2f}초)")