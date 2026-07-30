import cv2
import asl_alphabet.app as asl

rec = asl.Recognizer()

# Single image
image = cv2.imread("img.jpg")
letter, confidence, _ = rec.predict(image)
print(f"Letter: {letter}, Confidence: {confidence:.2%}")
