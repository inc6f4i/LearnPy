#####################################################
###         onnx 모델적용해보기
#####################################################


import cv2
import numpy as np

# ########## AI 모델 로드 및 트래커 초기화 ##########
# TrackerVit을 사용하려면 ONNX 모델 파일 경로가 필요합니다.
# 파일명이 다르다면 해당 파일 이름으로 수정해주세요.
model_path = r'C:\Users\user\Desktop\vitTracker.onnx' 

params = cv2.TrackerVit_Params()
params.net = model_path
# 필요에 따라 backend 및 target 설정 가능 (예: GPU 가속 시 cv2.dnn.DNN_BACKEND_CUDA)
params.backend = cv2.dnn.DNN_BACKEND_DEFAULT
params.target = cv2.dnn.DNN_TARGET_CPU

try:
    tracker = cv2.TrackerVit_create(params)
except Exception as e:
    print(f"트래커 생성 실패: {e}")
    print("모델 파일(.onnx)이 정확한 경로에 있는지 확인해주세요.")
    exit()
# ##################################################

# 카메라 열기 (cv2.IMREAD_GRAYSCALE은 VideoCapture의 옵션이 아닙니다. 기본으로 엽니다)
cap = cv2.VideoCapture(0)

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

is_first_frame = True
bbox = None

while(True):
    ret, src = cap.read() 

    if (ret):
        # TrackerVit은 기본적으로 컬러(BGR) 이미지를 입력으로 받습니다.
        dst = src.copy()

        # 첫 번째 프레임에서 사용자가 추적할 영역(ROI)을 선택합니다.
        if is_first_frame:
            print("추적할 영역을 마우스로 드래그한 후 'Enter' 또는 'Space'를 누르세요.")
            # selectROI는 창이 뜨면 마우스로 네모를 그리고 엔터를 치면 됩니다.
            bbox = cv2.selectROI('Tracking Window', dst, fromCenter=False, showCrosshair=True)
            
            # ########## AI 트래커 초기화 ##########
            # 선택한 bbox 영역을 기반으로 AI 모델이 추적을 시작합니다.
            tracker.init(dst, bbox)
            # ######################################
            
            cv2.destroyWindow('Tracking Window')
            is_first_frame = False

        else:
            # ########## AI 객체 추적 수행 ##########
            # 매 프레임마다 AI 모델이 이전 객체의 위치를 기반으로 새 위치를 추정합니다.
            success, bbox = tracker.update(dst)
            # ######################################

            # 추적에 성공했다면 사각형을 그려줍니다.
            if success:
                x, y, w, h = [int(v) for v in bbox]
                cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(dst, "Tracking", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            else:
                cv2.putText(dst, "Lost", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        # 결과 화면 표시
        cv2.imshow('TrackerVIT', dst)

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release() 
cv2.destroyAllWindows()