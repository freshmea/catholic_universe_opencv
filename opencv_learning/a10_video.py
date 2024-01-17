import cv2


def main():
    cap = cv2.VideoCapture(
        "/home/aa/catholic_universe_opencv/opencv_learning/data/vtest.avi"
    )
    con = True
    while con:
        ret, frame = cap.read()
        if ret:
            cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord("q"):
            con = False


if __name__ == "__main__":
    main()
