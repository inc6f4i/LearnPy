import os
from datetime import datetime

def create_daily_folder():
    # 1. 오늘 날짜를 YYMMDD 형식의 문자열로 변환 (예: 2026년 6월 16일 -> "260616")
    folder_name = datetime.now().strftime("%y%m%d")
    
    # 2. 폴더 생성 (이미 존재하면 생성하지 않고 넘어감)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"🎉 폴더가 성공적으로 생성되었습니다: {folder_name}")
    else:
        print(f"ℹ️ 이미 동일한 이름의 폴더가 존재합니다: {folder_name}")

if __name__ == "__main__":
    create_daily_folder()