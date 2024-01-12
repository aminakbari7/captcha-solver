import cv2
import requests
def addres():
   url = "https://golestan.jsu.ac.ir/Forms/AuthenticateUser/captcha.aspx"
   r = requests.get(url)
   with open("image.gif", "wb") as f:
    f.write(r.content)
   
 