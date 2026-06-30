@echo off
chcp 65001 >nul
:: 1. 탐색기 특정 폴더 열기
start "" "E:\code"

:: 1. 탐색기 특정 폴더 열기
start "" "E:\code dokim"

:: 2. 크롬 시크릿 모드로 열기
start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --incognito "https://gemini.google.com/app"

:: 3. 옵시디언 열기
start "" "C:\Users\user\AppData\Local\Programs\Obsidian\Obsidian.exe"

:: 4. 카카오톡열기
start "" "C:\Program Files\Kakao\KakaoTalk\KakaoTalk.exe"

:: 5. 폴더만들기
start "" "E:\makeDailyPy.exe"

exit