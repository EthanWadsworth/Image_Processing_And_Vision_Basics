import cv2
import matplotlib.pyplot as plt


def create_canvas(width, height):
    if (width < 1) or (height < 1):
        return None
    
    return [[[0 for k in range(3)] for j in range(width)] for i in range(height)]


def visualize_img(img):
    if img == None:
        return
    
    plt.imshow(img)


