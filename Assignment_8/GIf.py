import os
import imageio
import cv2

file_ls = sorted(os.listdir("Assignment_8\Pics"))

ims = []

for file_n in file_ls:
    path = "Assignment_8\Pics" + "\\" + file_n
    im = cv2.imread(path)
    im = cv2.resize(im, (1920, 1080))
    ims.append(im)

imageio.mimsave("Assignment_8\Gif_car.gif", ims)