import cv2

def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)

    while True:
        ret_val, img = cam.read()
        if mirror:
            img = cv2.flip(img, 1)
        #cv2.imshow('my webcam', img)

        cv2.imwrite("elma.png",img)
        break  # esc to quit
    cv2.destroyAllWindows()

def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()