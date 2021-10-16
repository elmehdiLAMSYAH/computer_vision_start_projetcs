import cv2


class Picrure:
    def __init__(self, name):
        self.name = name

    def takepic(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            cv2.imshow("rea ltime picture", frame)
            if cv2.waitKey(1) == 13:
                cv2.imwrite(self.name + ".jpg", frame)
                break
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    pic = Picrure("mep")
    pic.takepic()
    image = cv2.imread(pic.name + ".jpg")
    cv2.imshow("image ", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
