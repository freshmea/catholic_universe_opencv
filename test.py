#!/usr/bin/python3
import cv2
import cv2.aruco as aruco

# Video
Video_filename = "video/aruco_test_mp4_1920x1080.avi"
cap = cv2.VideoCapture(Video_filename)
VideoCap = True


def find_aruco_id(img, marker_size=4, total_markers=50, draw=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f"DICT_{marker_size}X{marker_size}_{total_markers}")
    arucoDict = aruco.getPredefinedDictionary(key)
    arucoParam = aruco.DetectorParameters()
    bbox, ids, _ = aruco.detectMarkers(gray, arucoDict, parameters=arucoParam)
    if draw:
        aruco.drawDetectedMarkers(img, bbox)
    return ids


while True:
    if VideoCap:
        VideoCap, frame = cap.read()
    else:
        frame = cv2.imread("sample.png")

    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = round(100 / fps)
    # print("FRAME FPS ; ", int(cap.get(cv2.CAP_PROP_FPS)))

    id = find_aruco_id(frame)
    print(id)

    if cv2.waitKey(delay) == 27:
        break
    cv2.imshow("WINDOW", frame)

cap.release()
cv2.destroyAllWindows()
