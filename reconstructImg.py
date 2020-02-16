'''
  File name: reconstructImg.py
  Author:
  Date created:
'''
import numpy as np

def reconstructImg(indexes, red, green, blue, targetImg):

    resultImg = np.copy(targetImg)
    resultImg_red = np.copy(targetImg[:,:,0])
    resultImg_green = np.copy(targetImg[:, :, 1])
    resultImg_blue = np.copy(targetImg[:, :, 2])
    list = np.argwhere(indexes > 0)

    for i in list:
        x_index = int(indexes[i[0]][i[1]])-1
        resultImg_red[i[0]][i[1]] = red[x_index]

    for i in list:
        x_index = int(indexes[i[0]][i[1]])-1
        resultImg_green[i[0]][i[1]] = green[x_index]

    for i in list:
        x_index = int(indexes[i[0]][i[1]])-1
        resultImg_blue[i[0]][i[1]] = blue[x_index]

    resultImg[:,:,0] = resultImg_red
    resultImg[:,:,1] = resultImg_green
    resultImg[:,:,2] = resultImg_blue

    return resultImg