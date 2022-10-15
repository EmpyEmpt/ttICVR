import os
import sys
import cv2
import matplotlib.pyplot as plt


def imShow(path):

    image = cv2.imread(path)

    height, width = image.shape[:2]
    resized_image = cv2.resize(
        image, (3*width, 3*height), interpolation=cv2.INTER_CUBIC)

    fig = plt.gcf()
    fig.set_size_inches(18, 10)

    plt.axis("off")
    plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
    plt.show()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('You have to provide a path to the image as an argument')
        exit()
    im_path = sys.argv[0]
    os.system('cd ..')
    os.system('cd darknet')
    os.system(
        f'./darknet detector test data/obj.data cfg/yolov4-custom.cfg yolov4-custom_best.weights {im_path} -thresh 0.6')
    imShow('predictions.jpg')
