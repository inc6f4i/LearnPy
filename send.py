import os
import sys
from datetime import datetime
from urllib.parse import quote
import tkinter as tk
import webbrowser

if getattr(sys, 'frozen', False):
    exe_dir = os.path.dirname(sys.executable)
else:
    exe_dir = os.path.dirname(os.path.abspath(__file__))
counter_file = os.path.join(exe_dir, "pytechmr.txt")
today_str = datetime.now().strftime("%y%m%d")
current_count = 1

# 기본값
to_email = "techmr@daum.net"
cc_email = "sm4inc@gmail.com"
student_name = "김동진"

# txt 읽기
if os.path.exists(counter_file):
    with open(counter_file, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    if len(lines) >= 1:#첫 줄 교수님 이메일주소
        to_email = lines[0].strip()

    if len(lines) >= 2 and lines[1].strip():# 두번째 줄 보내는학생이름
        student_name = lines[1].strip()

    if len(lines) >= 3:#세번째 줄 CC 참조주소
        cc_email = lines[2].strip()

    if len(lines) >= 4 and "," in lines[3]: #네번째 줄 날짜기반 카운터, 자동갱신되나 오류시 이부분 텍스트파일수정
        saved_date, saved_count = lines[3].split(",", 1)
        if saved_date == today_str:
            current_count = int(saved_count) + 1
# txt 다시 저장
with open(counter_file, "w", encoding="utf-8") as f:
    f.write(f"{to_email}\n")    
    f.write(f"{student_name}\n")
    f.write(f"{cc_email}\n")
    f.write(f"{today_str},{current_count}\n")
# 제목
subject = f"{today_str}일차-실습-{current_count}-완료"

# 클립보드 내용
try:
    root = tk.Tk()
    root.withdraw()
    code_content = root.clipboard_get()
    root.destroy()
except Exception:
    code_content = "// 클립보드에 복사된 텍스트가 없거나 올바르지 않습니다."

body_template = (
    f"{code_content}\n\n\n\n\n"
    f"안녕하세요 교수님, 교육생 {student_name}입니다.\n"
    f"실습코드 송부드립니다.\n\n\n\n"
    f"감사합니다."
)

encoded_subject = quote(subject)
encoded_body = quote(body_template)

gmail_url = (
    f"https://mail.google.com/mail/?view=cm&fs=1"
    f"&to={quote(to_email)}"
)

if cc_email:
    gmail_url += f"&cc={quote(cc_email)}"

gmail_url += (
    f"&su={encoded_subject}"
    f"&body={encoded_body}"
)
webbrowser.open(gmail_url)
print(f"Gmail 작성창 열기 완료 -> {subject} / 이름: {student_name} / CC: {cc_email or '없음'}")