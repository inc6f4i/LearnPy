import os
import subprocess 
from datetime import datetime 
from urllib.parse import quote
import tkinter as tk

if getattr(sys, 'frozen', False):
    exe_dir = os.path.dirname(sys.executable)
else:
    exe_dir = os.path.dirname(os.path.abspath(__file__))

counter_file = os.path.join(exe_dir, "pytechmr.txt")

today_str = datetime.now().strftime("%y%m%d")
current_count = 1

# 파일이 존재하면 읽어서 날짜 확인 후 카운트 계산
if os.path.exists(counter_file):
    with open(counter_file, "r", encoding="utf-8") as f:
        line = f.read().strip()
        if line and "," in line:
            saved_date, saved_count = line.split(",")
            # 저장된 날짜가 오늘과 같다면 카운트를 1 증가
            if saved_date == today_str:
                current_count = int(saved_count) + 1
            # 날짜가 바뀌었다면 자동으로 1부터 다시 시작 (current_count = 1 유지)
# 변경된(또는 유지된) 날짜와 카운트를 파일에 다시 기록
with open(counter_file, "w", encoding="utf-8") as f:
    f.write(f"{today_str},{current_count}")
#제목
subject = f"{today_str}일차-실습-{current_count}-완료"

#내용
try:
    root = tk.Tk()
    root.withdraw()  # 빈 GUI 창이 뜨지 않도록 숨김
    code_content = root.clipboard_get()  # 클립보드 텍스트 추출
except Exception:
    code_content = "// 클립보드에 복사된 텍스트가 없거나 올바르지 않습니다."


to_email = "techmr@daum.net"
cc_email = ""

body_template = (
    f"{code_content}\n\n\n\n"
    f"안녕하세요 교수님, 교육생 홍길동입니다.\n"
    f"실습코드 송부드립니다.\n\n\n\n"
    f"감사합니다."
)
encoded_subject = quote(subject)
encoded_body = quote(body_template)

gmail_url = f"https://mail.google.com/mail/?view=cm&fs=1&to={to_email}&cc={cc_email}&su={encoded_subject}&body={encoded_body}"

# [중요] 윈도우 cmd에서 & 기호가 명령어로 쪼개져 발생하는 오류를 완벽 차단하기 위해
# 주소 전체를 하나의 독립된 인자로 묶어 쉘(shell=False)을 거치지 않고 크롬에 다이렉트로 던집니다.
chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" 
#subprocess.Popen(["cmd", "/c", "start", "chrome", "--incognito", f"{gmail_url}"])
subprocess.Popen([chrome_path, "--incognito", gmail_url])

print(f"workSpaceOnWithChromeIncognito -> {subject} (클립보드 내용 반영 완료)")