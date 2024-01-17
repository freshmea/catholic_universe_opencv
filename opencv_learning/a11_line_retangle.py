import cv2


def main():
    cap = cv2.VideoCapture(
        "/home/aa/catholic_universe_opencv/opencv_learning/data/vtest.avi"
    )
    con = True
    var = 1
    text = "My name is Catholic Universe"
    org = (50, 100)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while con:
        ret, frame = cap.read()
        # get width
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        pt1 = (int(width // var), int(height // var * 2))
        pt2 = (int(width // 2), int(height // 2))
        # pt1 = (100, 100)
        # pt2 = (200, 200)
        var += 0.1
        if var > 20:
            var = 1
        if ret:
            cv2.line(frame, pt1, pt2, (0, 0, 255), 3)
            cv2.rectangle(frame, pt1, pt2, (0, 255, 0), 3)
            cv2.rectangle(frame, (0, 0, 500, 500), (255, 0, 0), 5)
            cv2.circle(frame, pt2, 10, (255, 255, 0), 3)
            cv2.circle(frame, pt1, 10, (0, 0, 255), 3)
            cv2.putText(frame, text, pt1, font, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow("frame", frame)
        if cv2.waitKey(1) == ord("q"):
            con = False


if __name__ == "__main__":
    main()
