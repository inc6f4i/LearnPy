#####################################################
###   기존 코드에서 GUI 수정, 색상변경 선분을 점선으로 등
#####################################################

import cv2
import numpy as np
TRACKER_NAMES = [
    "BOOSTING",
    "MIL",
    "KCF",
    "TLD",
    "MEDIANFLOW",
    "CSRT",
    "MOSSE"
]

#AI 함수#############################################점선그리기
def drawDot(img, pt1, pt2, color, thickness=1, dash_length=10):
    x1, y1 = pt1
    x2, y2 = pt2
    # 사각형의 네 변을 구성하는 직선의 시작점과 끝점 정의
    lines = [
        ((x1, y1), (x2, y1)), # 상단 변
        ((x2, y1), (x2, y2)), # 우측 변
        ((x2, y2), (x1, y2)), # 하단 변
        ((x1, y2), (x1, y1))  # 좌측 변
    ]
    
    for start, end in lines:
        # 각 변의 전체 길이 계산
        line_len = np.hypot(end[0] - start[0], end[1] - start[1])
        
        # 선을 몇 개의 조각(점선)으로 나눌지 계산
        chunks = int(line_len / dash_length)
        
        for i in range(chunks):
            # 시작점과 끝점 사이의 점선 구간 계산 (하나 건너 하나씩 그리기)
            if i % 2 == 0:
                p1_x = int(start[0] + (end[0] - start[0]) * (i / chunks))
                p1_y = int(start[1] + (end[1] - start[1]) * (i / chunks))
                p2_x = int(start[0] + (end[0] - start[0]) * ((i + 1) / chunks))
                p2_y = int(start[1] + (end[1] - start[1]) * ((i + 1) / chunks))
                
                cv2.line(img, (p1_x, p1_y), (p2_x, p2_y), color, thickness)


#TRACKER_NAMES = [
#    "KCF",
#    "CSRT"
#]
trackerIdx = 5
tracker = None
bbox = None
isFirst = True
#video_src = r'C:\Users\user\Desktop\objdecsrc\2026-07-07 highway.mp4'
video_src = 0
cap = cv2.VideoCapture(video_src)
if not cap.isOpened():
    print("Could not open video")
    exit()
fps = cap.get(cv2.CAP_PROP_FPS)
if fps is None or fps <= 0:
    delay = 33
else:
    delay = int(1000 / fps)
win_name = "Tracking APIs"
def create_tracker(tracker_name):
    name_map = {
        "BOOSTING": "Boosting",
        "MIL": "MIL",
        "KCF": "KCF",
        "TLD": "TLD",
        "MEDIANFLOW": "MedianFlow",
        "GOTURN": "GOTURN",
        "CSRT": "CSRT",
        "MOSSE": "MOSSE"       
    }
    class_name = name_map[tracker_name]
    create_func_name = f"Tracker{class_name}_create"
    create_func = getattr(cv2, create_func_name, None)
    if create_func is not None:
        return create_func()
    tracker_class_name = f"Tracker{class_name}"
    tracker_class = getattr(cv2, tracker_class_name, None)
    if tracker_class is not None and hasattr(tracker_class, "create"):
        return tracker_class.create()
    if hasattr(cv2, "legacy"):
        legacy_create_func = getattr(cv2.legacy, create_func_name, None)
        if legacy_create_func is not None:
            return legacy_create_func()
        legacy_tracker_class = getattr(cv2.legacy, tracker_class_name, None)
        if legacy_tracker_class is not None and hasattr(legacy_tracker_class, "create"):
            return legacy_tracker_class.create()
    raise AttributeError(
        f"{tracker_name} 트래커를 현재 OpenCV에서 찾을 수 없습니다. "
        f"opencv-contrib-python 설치 여부와 cv2.legacy 지원 여부를 확인하세요."
    )
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Cannot read video file")
        break
    img_draw = frame.copy()
    if tracker is None:
        cv2.putText(
            img_draw,
            "Press the Space to set ROI!!",
            (100, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (10, 10, 10),
            2,
            cv2.LINE_AA
        )
    else:
        ok, bbox = tracker.update(frame)
        x, y, w, h = map(int, bbox)
#260708################################################# 요구사항 1
        if ok:
            drawDot(img_draw, (int(x), int(y)),  (int(x + w), int(y + h)), (0, 255, 255), thickness=1, dash_length=10)
  
            cv2.putText(
                img_draw,
                "Tracking Success!!!!!",
                (int(x), int(y)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.75,
#260708################################################# 요구사항 2. 성공실패 시각화     
                (0, 255, 0),                     
                2,
                cv2.LINE_AA
            )            
        else:
            cv2.putText(
                img_draw,
                "Tracking fail!!!!!",
                (100, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.75,
#260708################################################# 요구사항 2. 성공실패 시각화     
                (0, 0, 255),                     
                2,
                cv2.LINE_AA
            )
    trackerName = TRACKER_NAMES[trackerIdx]
    cv2.putText(
        img_draw,
        f"{trackerIdx}:{trackerName}",
        (100, 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.75,
        (0, 255, 0),
        2,
        cv2.LINE_AA
    )
    cv2.imshow(win_name, img_draw)
    key = cv2.waitKey(delay) & 0xff
    if key == ord(" ") or (video_src != 0 and isFirst):
        isFirst = False
        roi = cv2.selectROI(win_name, frame, False)
        if roi[2] and roi[3]:
            tracker = create_tracker(TRACKER_NAMES[trackerIdx])
            bbox = roi
            isInit = tracker.init(frame, roi)
            if not isInit: 
                print("Tracker initialization failed")
    elif 48 <= key < 48 + len(TRACKER_NAMES):  
        trackerIdx = key - 48
        if bbox is not None:
#260708################################################# 요구사항 외 init오류가 있어서 추가한코드입니다
            x, y , w, h = map(int, bbox)
            int_bbox = (x, y, w, h)
            tracker = create_tracker(TRACKER_NAMES[trackerIdx])
            isInit = tracker.init(frame, int_bbox)
            if not isInit:
                print("Tracker re-initialization failed")
    elif key == 27:
        break
cap.release()
cv2.destroyAllWindows()