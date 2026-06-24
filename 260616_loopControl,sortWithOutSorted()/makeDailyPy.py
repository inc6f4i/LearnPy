import os
from datetime import datetime
import numpy as np

def create_daily_workspace():
    # 1. ⚠️ 날짜 형식을 반드시 "YYYY-MM-DD" 형태로 적어주어야 에러가 나지 않습니다.
    START_DATE = "2026-03-27" 
    
    # 2. 오늘 날짜 정보 가져오기
    today = datetime.now()
    folder_name = today.strftime("%y%m%d")  # 폴더명: "260616"
    today_str = today.strftime("%Y-%m-%d") # 평일 계산용: "2026-06-16"
    
    # 공휴일 리스트 (형식 일치 필수)
    holidays_list = np.array([
        '2026-05-05', # 어린이날
        '2026-05-25'  # 석가탄신일
    ], dtype='datetime64[D]')
    # 3. 평일(수업일) 계산 진행
    try:
        # 주말과 공휴일을 제외한 실제 수업 일수 계산 (+1은 오늘 포함용)
        class_days = np.busday_count(START_DATE, today_str, holidays=holidays_list) +2
        day_prefix = f"day{class_days:03d}"  # 예: "day057"
    except Exception as e:
        print(f"error during calculate day: {e}")
        return

    # 4. 폴더 생성
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"folder created: {folder_name} ({day_prefix})")
    else:
        print(f"folder already exist: {folder_name} ({day_prefix})")
        
    # 5. 파일 생성 (1부터 20까지)
    created_count = 0
    for i in range(1, 21):
        file_name = f"{day_prefix}_{i:02d}.py"
        file_path = os.path.join(folder_name, file_name)

        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"# {day_prefix}_{i:02d}.py\n")
            created_count += 1
            
    if created_count > 0:
        print(f"{created_count} .py file created!")
    else:
        print("all file already exist.")

if __name__ == "__main__":
    create_daily_workspace()