import matplotlib.pyplot as plt
import seamlessCloningPoisson
import createMask

targetImg = plt.imread('Images/1_background.jpg')
sourceImg = plt.imread('Images/1_source.jpg')
#mask = createMask.main('1_source.jpg') #uncomment this if you want to create a new mask and comment the line below
mask = plt.imread('Images/1_mask.png')

offsetX = 300
offsetY = 240

resultImg = seamlessCloningPoisson.seamlessCloningPoisson(sourceImg,targetImg,mask,offsetX,offsetY)

plt.imshow(resultImg)
plt.xticks([]), plt.yticks([])
plt.show()
