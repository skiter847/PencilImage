from PencilImage.celery import app
import cv2
import os


@app.task
def convert_to_pencil(filename):
    path = os.getcwd() + filename
    img = cv2.imread(path, 1)
    cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(img_gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
    final_img = cv2.divide(img_gray, 255 - img_smoothing, scale=256)

    final_img_name = 'convert_' + path.split('media/')[1]

    path_to_final_img = os.getcwd() + '/media/' + final_img_name
    cv2.imwrite(path_to_final_img, final_img)

    return final_img_name
