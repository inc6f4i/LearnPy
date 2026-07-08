#####################################################
###         트래커알고리즘별 차이점 체험해보기
#####################################################



# 073일차-실습-3-해답 
# Tracker APIs 수정판
# track_trackingAPI_green_dotted_status_text_260708_01.py

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


trackerIdx = 0
tracker = None
bbox = None
isFirst = True

video_src = 0  # 기본 카메라 사용
#video_src = "D:/GoogleDrv/99_LectureData/00_incheon/code/day260707/images/highway.mp4"

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


#260708주석 : 이것은 초록색 점선을 구현하는 함수입니다
def draw_green_dotted_rectangle(img, x, y, w, h, dot_length=8, gap=6, thickness=2):
    """
    초록색 점선 사각형을 그리는 함수임.
    OpenCV의 cv2.rectangle()은 점선을 직접 지원하지 않으므로
    짧은 선분을 반복해서 점선처럼 보이도록 구현함.
    """

    green = (0, 255, 0)  # OpenCV는 BGR 순서이므로 초록색은 (0, 255, 0)임

    x1 = int(x)
    y1 = int(y)
    x2 = int(x + w)
    y2 = int(y + h)

    # 위쪽 가로선
    for i in range(x1, x2, dot_length + gap):
        cv2.line(
            img,
            (i, y1),
            (min(i + dot_length, x2), y1),
            green,
            thickness
        )

    # 아래쪽 가로선
    for i in range(x1, x2, dot_length + gap):
        cv2.line(
            img,
            (i, y2),
            (min(i + dot_length, x2), y2),
            green,
            thickness
        )

    # 왼쪽 세로선
    for i in range(y1, y2, dot_length + gap):
        cv2.line(
            img,
            (x1, i),
            (x1, min(i + dot_length, y2)),
            green,
            thickness
        )

    # 오른쪽 세로선
    for i in range(y1, y2, dot_length + gap):
        cv2.line(
            img,
            (x2, i),
            (x2, min(i + dot_length, y2)),
            green,
            thickness
        )


#260708주석 : 이것은 초록색 점선으로 ROI 선택 상자를 구현하는 함수입니다
def select_roi_green_dotted(window_name, frame):
    """
    cv2.selectROI() 대신 사용하는 사용자 정의 ROI 선택 함수임.
    ROI 선택 중에도 초록색 점선 상자가 표시되도록 구현함.

    사용법:
    1. 마우스 왼쪽 버튼을 누른 상태로 드래그함
    2. 마우스 버튼을 놓으면 ROI 영역이 선택됨
    3. Enter 또는 Space 키를 누르면 ROI가 확정됨
    4. ESC 키를 누르면 ROI 선택이 취소됨
    """

    clone = frame.copy()
    roi = [0, 0, 0, 0]

    drawing = False
    selected = False

    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0

    def mouse_callback(event, x, y, flags, param):
        nonlocal drawing, selected
        nonlocal start_x, start_y, end_x, end_y
        nonlocal roi

        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            selected = False

            start_x = x
            start_y = y
            end_x = x
            end_y = y

        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing:
                end_x = x
                end_y = y

                temp = clone.copy()

                rect_x = min(start_x, end_x)
                rect_y = min(start_y, end_y)
                rect_w = abs(end_x - start_x)
                rect_h = abs(end_y - start_y)

                #260708주석 : ROI 선택 중 표시되는 상자를 초록색 점선으로 표시함
                draw_green_dotted_rectangle(
                    temp,
                    rect_x,
                    rect_y,
                    rect_w,
                    rect_h
                )

                cv2.imshow(window_name, temp)

        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            selected = True

            end_x = x
            end_y = y

            rect_x = min(start_x, end_x)
            rect_y = min(start_y, end_y)
            rect_w = abs(end_x - start_x)
            rect_h = abs(end_y - start_y)

            roi = [rect_x, rect_y, rect_w, rect_h]

            temp = clone.copy()

            #260708주석 : ROI 선택 완료 후에도 초록색 점선 상자를 표시함
            draw_green_dotted_rectangle(
                temp,
                rect_x,
                rect_y,
                rect_w,
                rect_h
            )

            cv2.imshow(window_name, temp)

    cv2.imshow(window_name, clone)
    cv2.setMouseCallback(window_name, mouse_callback)

    while True:
        key = cv2.waitKey(1) & 0xff

        # Enter 키 또는 Space 키로 ROI 확정
        if selected and (key == 13 or key == ord(" ")):
            break

        # ESC 키로 ROI 선택 취소
        if key == 27:
            roi = [0, 0, 0, 0]
            break

    #260708주석 : ROI 선택 후 마우스 콜백을 비활성화함
    cv2.setMouseCallback(window_name, lambda *args: None)

    return tuple(roi)


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
            #260708주석 : 기존 cv2.rectangle() 대신 초록색 점선 바운딩 박스 함수를 호출함
            draw_green_dotted_rectangle(
                img_draw,
                x,
                y,
                w,
                h
            )

            #260708주석 : 추적 성공 시 초록색 성공 메시지를 화면에 추가 표시함
            cv2.putText(
                img_draw,
                "Tracking Success!!!!!",
                (100, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.75,
                (0, 255, 0),
                2,
                cv2.LINE_AA
            )
        else:
            #260708주석 : 추적 실패 시 빨간색 실패 메시지를 화면에 추가 표시함
            cv2.putText(
                img_draw,
                "Tracking Fai1ed!!!!!",
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

        #260708주석 : cv2.selectROI() 대신 초록색 점선 ROI 선택 함수를 호출함
        roi = select_roi_green_dotted(win_name, frame)

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
