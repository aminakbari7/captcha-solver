import os
import pickle
import cv2
import numpy as np
from skimage.transform import resize
from Separator import PredictWord
from captchaDownloader import addres

Categories = os.listdir("./DataSet/")
filename = "model.sav"
loaded_model = pickle.load(open(filename, "rb"))

def getCaptchaText(Captcha):
    clusters = PredictWord(Captcha)
    text = ""
    for image in clusters:
        flat_data = []
        img_resized = resize(image, (40, 40, 3))
        flat_data.append(img_resized.flatten())
        flat_data = np.array(flat_data)
        y_output = loaded_model.predict(flat_data)
        text += Categories[y_output[0]].replace("upper", "").replace("lower", "")
    return text

def main():
    addres()
    text = getCaptchaText("image.gif")
    print("Predicted Text Is:", text)
    
if __name__=="__main__":
    main()




