from PIL import Image
import pytesseract
import cv2
import os


class OCR:

    #there are two preprocess methods default is tresholing and blur
    def __init__(self, path, preprocess="tresholding"):
        self.preprocess = preprocess
        self.path = path

    #preprocessing methods resizing, converting to grayscale, tresholing or blur
    def preprocessing(self):
        img = cv2.imread(self.path)
        img = cv2.resize(img, (0, 0), fx=4, fy=4)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if self.preprocess == "thresholding":
            img = cv2.threshold(img, 0, 255,
                                 cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        elif self.preprocess == "blur":
            img = cv2.medianBlur(img, 3)
        filename = "img/temporary.png"
        cv2.imwrite(filename, img)
        return filename

    #returns read text from image
    def textReading(self):
        filename = self.preprocessing()
        text = pytesseract.image_to_string(Image.open(filename))
        os.remove(filename)
        return text




if __name__ == "__main__":
    ocr=OCR('img/card12.png')
    text = ocr.textReading()
    print(text)

