# controllers/facial_recognition_controller.pyAdd commentMore actions
from flask import Blueprint, jsonify
from app.utils.emotion_recognition import EmotionRecognition
import cv2
from fer import FER

def start_real_time_emotion_detection():
    detector = FER(mtcnn=True)
    cap = cv2.VideoCapture(0)
facial_recognition_bp = Blueprint('facial_recognition', __name__)
emotion_recognition = EmotionRecognition()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
@facial_recognition_bp.route('/facial_recognition/stream', methods=['GET'])
def stream():
    # Abrir cámara
    cap = cv2.VideoCapture(0)  # Cámara integrada
    if not cap.isOpened():
        return jsonify({"error": "No se pudo acceder a la cámara"}), 500

        # Detecta emociones en el fotograma actual
        emotion, score = detector.top_emotion(frame)
        label = f"{emotion}: {score * 100:.2f}%" if emotion else "No face detected"
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

        # Muestra el resultado en el fotograma
        cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Real-Time Emotion Detection", frame)
            # Procesar cada fotograma
            response = emotion_recognition.detect_emotion(frame)
            print(response)  # Mostrar emoción detectada en consola (temporal)

        # Presiona 'q' para salir
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
Add commentMore actions
if __name__ == "__main__":
    start_real_time_emotion_detection()
        return jsonify({"message": "Streaming finalizado"})
    finally:
        cap.release()
