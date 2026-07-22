################################################################################
###         onnx 모델적용해보기
################################################################################
import cv2
model_path = r'C:\Users\user\Desktop\face_detection_yunet_2026may.onnx'

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
if not ret:
    print("카메라 읽기 실패")
    exit()

h, w = frame.shape[:2]

detector = cv2.FaceDetectorYN.create(
    model=model_path,
    config="",
    input_size=(w, h),
    score_threshold=0.9,
    nms_threshold=0.3,
    top_k=5000
)

while True:
    ret, src = cap.read()
    if not ret:
        break

    h, w = src.shape[:2]
    detector.setInputSize((w, h))

    result = detector.detect(src)
    faces = result[1]

    if faces is not None:
        for face in faces:
            x, y, w, h = face[:4].astype(int)

            cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(src, "Face", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("YuNet Face Detection", src)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()