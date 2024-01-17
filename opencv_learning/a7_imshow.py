import cv2


def main():
    img = cv2.imread(
        "/home/aa/catholic_universe_opencv/opencv_learning/data/lena.jpg", 1
    )
    # img = cv2.imread("opencv_learning/a7_imshow.py", 1)
    cv2.imshow("lena", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
