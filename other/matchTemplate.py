import cv2
import numpy as np

# 웹캠 열기
cap = cv2.VideoCapture(0)

# ==========================================
# [공란] 찾고자 하는 템플릿 이미지의 경로를 입력하세요.
# 예시: 'template.jpg' (그레이스케일로 불러옵니다)
# ==========================================
template_path = r'D:\opencv\x1.png' 
template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

# 템플릿 이미지가 정상적으로 로드되었는지 확인
if template is None:
    print("⚠️ 경고: 템플릿 이미지 경로가 비어있거나 파일을 찾을 수 없습니다.")
    print("-> 코드 상단의 'template_path'에 이미지 경로를 입력한 후 실행해주세요.")
    # 경로가 없을 경우를 대비한 가상의 빈 이미지 생성 (에러 방지용)
    template = np.zeros((50, 50), dtype=np.uint8) 

# 템플릿 이미지의 가로, 세로 크기 구해두기
th, tw = template.shape[:2]

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

while(True):
    ret, src = cap.read()

    if (ret):
        # 1. 템플릿 매칭을 위해 웹캠 프레임을 그레이스케일로 변환
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        
        # 2. cv2.matchTemplate 알고리즘 적용
        # method로는 cv2.TM_CCOEFF_NORMED(정규화된 상관계수)를 가장 흔히 사용합니다.
        # 결과물(res)은 일종의 맵(Map) 데이터이며, 매칭 점수가 높을수록 밝은 값을 가집니다.
        res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
        
        # 3. cv2.minMaxLoc를 통해 매칭 결과에서 최솟값, 최댓값 및 그 위치를 찾아냅니다.
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
        # 4. 매칭 신뢰도(Threshold) 설정 
        # TM_CCOEFF_NORMED 기준 1.0에 가까울수록 완벽히 일치함을 뜻합니다. 보통 0.7~0.8 이상을 기준으로 잡습니다.
        threshold = 0.7
        if max_val >= threshold:
            # 가장 매칭 확률이 높은 왼쪽 위 시작 좌표
            top_left = max_loc
            # 템플릿 크기를 더해 오른쪽 아래 끝 좌표 계산
            bottom_right = (top_left[0] + tw, top_left[1] + th)
            
            # 찾은 영역에 파란색(BGR: 255, 0, 0) 사각형 그리기
            cv2.rectangle(src, top_left, bottom_right, (255, 0, 0), 3)
            # 사각형 위에 매칭 점수 표기
            cv2.putText(src, f"Match: {max_val:.2f}", (top_left[0], top_left[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        else:
            # 매칭되는 물체가 없을 때 화면에 안내 문구 출력
            cv2.putText(src, "Searching template...", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # 5. 결과 영상 출력
        cv2.imshow('Template Matching', src)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()