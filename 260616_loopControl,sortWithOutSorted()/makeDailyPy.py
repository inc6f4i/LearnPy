import os
from datetime import datetime
import numpy as np

def create_daily_workspace():
    # 1. ⚠️ numpy 날짜 형식반드시 "YYYY-MM-DD"
    START_DATE = "2026-03-19" 
    
    # 2. 오늘 날짜 정보 가져오기
    today = datetime.now()
    sttDate = datetime.strptime("260319","%y%m%d")
    endDate = datetime.strptime("261005","%y%m%d")
    if  endDate >= today >= sttDate: #추가한사항 시작~끝날 사이에만 작동
        folder_name = today.strftime("%y%m%d")  # 폴더명: "260616" << 여기 datetime.str방식설정가능 
        today_str = today.strftime("%Y-%m-%d") # 평일 계산용: "2026-06-16"
        
        # 주말제외 공휴일 리스트 (형식 일치 필수) class numpy .array에
        holidays_list = np.array([
            '2026-04-23', # 체육대회
            '2026-04-24', # 체육대회
            '2026-05-01', # 근로자의날
            '2026-05-04', # 자율학습 
            '2026-05-25',  # 석가탄신일 대체휴일
            '2026-06-03', # 선거
            '2026-07-17',  # 제헌절
            '2026-08-17',  # 대체공휴일
            '2026-09-24',  # 추석연휴
            '2026-09-25',  # 추석
            '2026-10-06'  # 대체휴일
        ], dtype='datetime64[D]')
        print(holidays_list)
        # 3. 평일(수업일) 계산 진행
        try:
            # 주말과 공휴일을 제외한 실제 수업 일수 계산
            class_days = np.busday_count(START_DATE, today_str, holidays=holidays_list)
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
            file_name = f"{folder_name}_{day_prefix}_{i:02d}.py"
            file_path = os.path.join(folder_name, file_name)
    
            if not os.path.exists(file_path):
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(f"#{folder_name}_{day_prefix}_{i:02d}_.py\n")
                created_count += 1
                
        if created_count > 0:
            print(f"{created_count} .py file created!")
        else:
            print("all file already exist.")
    else :
        exit(0)
if __name__ == "__main__":
    create_daily_workspace()