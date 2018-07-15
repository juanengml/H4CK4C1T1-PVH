import zbar

from PIL import Image
import cv2
import urllib
import numpy as np 



url = "http://10.0.90.51:8080/shot.jpg"



while True:
    imgResp=urllib.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    ibagem=cv2.imdecode(imgNp,-1)
    cv2.imshow('test',ibagem)
    gray = cv2.cvtColor(ibagem, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    image = Image.fromarray(gray)
    width, height = image.size
    zbar_image = zbar.Image(width, height, 'Y800', image.tostring())
    scanner = zbar.ImageScanner()
    for decoded in zbar_image:
        text = decoded.data
        print text
    if ord('q')==cv2.waitKey(10):
        exit(0)

    """#capture = cv2.VideoCapture(0)
                #ret, ibagem = capture.read()
                gray = cv2.cvtColor(ibagem, cv2.COLOR_BGR2GRAY)
                image = Image.fromarray(gray)
                width, height = image.size
                zbar_image = zbar.Image(width, height, 'Y800', image.tostring())
                scanner = zbar.ImageScanner()
                scanner.scan(zbar_image)
                cv2.imshow('Detect QRCODE', ibagem) #DESCOMENTE SE QUISER MODAFOKA
                cv2.imshow('gray', gray)
                for decoded in zbar_image:
                        text = decoded.data
            """
