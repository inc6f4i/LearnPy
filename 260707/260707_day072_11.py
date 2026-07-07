# Tracker APIs 수정판
# track_trackingAPI_fixed.py

import cv2

# 사용할 트래커 이름 목록
# GOTURN은 별도 모델 파일(goturn.prototxt, goturn.caffemodel)이 필요한 경우가 많으므로 기본 목록에서 제외함
TRACKER_NAMES = [
    "BOOSTING",
    "MIL",
    "KCF",
    "TLD",
    "MEDIANFLOW",
    "CSRT",
    "MOSSE"
]
#TRACKER_NAMES = [
#    "KCF",
#    "CSRT"
#]


trackerIdx = 5
tracker = None
bbox = None
isFirst = True

video_src = r'C:\Users\user\Desktop\imaging\260707\highway.mp4'

cap = cv2.VideoCapture(video_src)

if not cap.isOpened():
    print("Could not open video")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)

# FPS를 읽지 못하는 경우를 대비한 안전 처리
if fps is None or fps <= 0:
    delay = 33       # 약 30fps 기준
else:
    delay = int(1000 / fps)

win_name = "Tracking APIs"


def create_tracker(tracker_name):
    """
    OpenCV 버전에 따라 트래커 생성 위치가 다르므로
    cv2 최상위와 cv2.legacy를 모두 확인해서 생성함.
    """

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

    # 1순위: cv2.TrackerKCF_create 같은 함수형 생성자
    create_func_name = f"Tracker{class_name}_create"
    create_func = getattr(cv2, create_func_name, None)

    if create_func is not None:
        return create_func()

    # 2순위: cv2.TrackerKCF.create() 같은 클래스형 생성자
    tracker_class_name = f"Tracker{class_name}"
    tracker_class = getattr(cv2, tracker_class_name, None)

    if tracker_class is not None and hasattr(tracker_class, "create"):
        return tracker_class.create()

    # 3순위: cv2.legacy.TrackerKCF_create 같은 legacy 함수형 생성자
    if hasattr(cv2, "legacy"):
        legacy_create_func = getattr(cv2.legacy, create_func_name, None)

        if legacy_create_func is not None:
            return legacy_create_func()

        # 4순위: cv2.legacy.TrackerKCF.create() 같은 legacy 클래스형 생성자
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
            (0, 0, 255),
            2,
            cv2.LINE_AA
        )
    else:
        ok, bbox = tracker.update(frame)

        x, y, w, h = bbox

        if ok:
            cv2.rectangle(
                img_draw,
                (int(x), int(y)),
                (int(x + w), int(y + h)),
                (0, 255, 0),
                2,
                1
            )
        else:
            cv2.putText(
                img_draw,
                "Tracking fail.",
                (100, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.75,
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

    # 스페이스바 또는 비디오 파일 최초 실행 시 ROI 선택
    if key == ord(" ") or (video_src != 0 and isFirst):
        isFirst = False

        roi = cv2.selectROI(win_name, frame, False)

        if roi[2] and roi[3]:
            tracker = create_tracker(TRACKER_NAMES[trackerIdx])
            bbox = roi
            isInit = tracker.init(frame, roi)

            if not isInit:
                print("Tracker initialization failed")

    # 숫자키 0 ~ 트래커 개수-1
    elif 48 <= key < 48 + len(TRACKER_NAMES):
        trackerIdx = key - 48

        if bbox is not None:
            tracker = create_tracker(TRACKER_NAMES[trackerIdx])
            isInit = tracker.init(frame, bbox)

            if not isInit:
                print("Tracker re-initialization failed")

    elif key == 27:
        break

cap.release()
cv2.destroyAllWindows()