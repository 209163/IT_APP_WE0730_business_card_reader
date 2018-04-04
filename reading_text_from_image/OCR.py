from PIL import Image
import pytesseract
import cv2
import os
from os import listdir
from os.path import isfile, join


class OCR:

    # there are two preprocess methods default is tresholing and blur
    def __init__(self, path, preprocess="tresholding"):
        self.preprocess = preprocess
        self.path = path

    # preprocessing methods resizing, converting to grayscale, tresholing or blur
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

    def textformating(self, text):
        text = text.splitlines()
        for word in text:
            if word == "":
                text.remove(word)
        return text

    # returns read text from image
    def textReading(self):
        filename = self.preprocessing()
        text = self.textformating(pytesseract.image_to_string(Image.open(filename)))
        os.remove(filename)
        imageData = self.addLabels(text)
        return imageData

    def addLabels(self, text):
        imageData = []
        for element in text:
            imageData.append({"text": element, "length": len(element), "index": text.index(element)})
        return imageData

    def saveToFile(self, imageData):
        file = open("trainingSet.txt", 'a')
        file.write("business card:" + "\n")
        for element in imageData:
            file.write(element["text"] + "," + str(element["length"]) + "," + str(element["index"]) + "\n")
        file.close()


# takes directory and creates file with text from images
def saveImagesFromDirectory(directory):
    for path in listdir(directory):
        if isfile(join(directory, path)):
            path = join(directory, path)
            ocr = OCR(path)
            imageData = ocr.textReading()
            ocr.saveToFile(imageData)
            print("image: " + path + " saved")


if __name__ == "__main__":
    directory = "img"
    saveImagesFromDirectory(directory)

    # #reads a single image
    #path = "img/55-page-001.jpg"
    #ocr=OCR(path)
    #imageData = ocr.textReading()
    #print(imageData)


