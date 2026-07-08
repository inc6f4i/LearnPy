#260630_day067_09_.py
import sys
import cv2
import numpy as np
import pytesseract
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, 
                             QLabel, QVBoxLayout, QHBoxLayout, QFileDialog, QTextEdit)
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt

# Tesseract 경로 설정
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class OcrApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.raw_img = None  # 불러온 원본 이미지를 저장할 변수

    def initUI(self):
        self.setWindowTitle('OpenCV + Tesseract OCR 프로그램')
        self.setGeometry(100, 100, 900, 600)

        # 메인 위젯 및 레이아웃
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # --- 왼쪽 레이아웃: 버튼 및 이미지 표시 ---
        left_layout = QVBoxLayout()
        
        self.btn_load = QPushButton('이미지 불러오기', self)
        self.btn_load.clicked.connect(self.load_image)
        left_layout.addWidget(self.btn_load)

        self.btn_ocr = QPushButton('OCR 실행 (PSM 6)', self)
        self.btn_ocr.clicked.connect(self.run_ocr)
        self.btn_ocr.setEnabled(False) # 이미지가 없을 땐 비활성화
        left_layout.addWidget(self.btn_ocr)

        # 이미지가 표시될 라벨
        self.lbl_image = QLabel('이미지를 불러와 주세요.', self)
        self.lbl_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_image.setStyleSheet("border: 1px solid gray; background-color: #f0f0f0;")
        left_layout.addWidget(self.lbl_image)

        # --- 오른쪽 레이아웃: 결과 텍스트창 ---
        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel('정제된 OCR 결과 텍스트:'))
        
        self.txt_result = QTextEdit(self)
        self.txt_result.setFontPointSize(12)
        right_layout.addWidget(self.txt_result)

        # 메인 레이아웃에 좌우 합치기
        main_layout.addLayout(left_layout, stretch=1)
        main_layout.addLayout(right_layout, stretch=1)

    def load_image(self):
        # 파일 탐색기 열기
        file_path, _ = QFileDialog.getOpenFileName(self, '이미지 선택', '', 'Images (*.png *.jpg *.jpeg *.bmp)')
        
        if file_path:
            # OpenCV로 이미지 읽기
            self.raw_img = cv2.imread(file_path)
            
            # UI용 화면 표시 변환 (BGR -> RGB)
            rgb_img = cv2.cvtColor(self.raw_img, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_img.shape
            bytes_per_line = ch * w
            
            # QImage 변환 후 라벨에 띄우기
            q_img = QImage(rgb_img.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(q_img)
            
            # 크기 조절하여 표시
            self.lbl_image.setPixmap(pixmap.scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio))
            self.btn_ocr.setEnabled(True)
            self.txt_result.clear()

    def run_ocr(self):
        if self.raw_img is None:
            return

        try:
            # 1. 사용자가 짠 OpenCV 전처리 로직 그대로 적용
            cropImg = self.raw_img[347:, 5:]
            sizeup = cv2.resize(cropImg, None, fx=2.5, fy=2.5, interpolation=cv2.INTER_CUBIC)
            hsv = cv2.cvtColor(sizeup, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, (0, 0, 175), (179, 80, 255))

            num, labels, stats, _ = cv2.connectedComponentsWithStats(mask, 8)
            clean = np.zeros_like(mask)
            h, w = mask.shape

            for i in range(1, num):
                x, y, bw, bh, area = stats[i]
                if area > w * h * 0.015: continue
                if area < 20: continue
                clean[labels == i] = 255

            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
            clean = cv2.morphologyEx(clean, cv2.MORPH_CLOSE, kernel, iterations=1)
            
            ocr_img = cv2.bitwise_not(clean)

            # 테두리 여백 추가 (인식률 보정용)
            ocr_img = cv2.copyMakeBorder(ocr_img, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=[255, 255, 255])

            # 2. Tesseract 실행
            custom_config = r'--psm 6'
            text = pytesseract.image_to_string(ocr_img, lang='kor+eng', config=custom_config)

            # 3. UI 우측 텍스트 창에 결과 출력
            self.txt_result.setText(text)
            
            # (선택사항) 전처리된 이진화 이미지를 왼쪽 창에 대신 보여주어 모니터링 가능하게 변경
            h, w = ocr_img.shape
            q_img = QImage(ocr_img.data, w, h, w, QImage.Format.Format_Grayscale8)
            pixmap = QPixmap.fromImage(q_img)
            self.lbl_image.setPixmap(pixmap.scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio))

        except Exception as e:
            self.txt_result.setText(f"에러가 발생했습니다:\n{str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OcrApp()
    ex.show()
    sys.exit(app.exec())