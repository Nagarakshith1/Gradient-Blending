'''
  File name: seamlessCloningPoisson.py
  Author:
  Date created:
'''
import numpy as np
import getIndexes
import getCoefficientMatrix
import getSolutionVect
import reconstructImg
from scipy import sparse

def seamlessCloningPoisson(sourceImg, targetImg, mask, offsetX, offsetY):
    targetH, targetW, k = targetImg.shape
    indexes = getIndexes.getIndexes(mask, targetH, targetW, offsetX, offsetY)
    coeffA = getCoefficientMatrix.getCoefficientMatrix(indexes)

    for i in range(3):
        target = targetImg[:, :, i]
        source = sourceImg[:, :, i]
        b = getSolutionVect.getSolutionVect(indexes, source, target, offsetX, offsetY)
        if i == 0:
            red = sparse.linalg.spsolve(coeffA, b)
            red = np.clip(red, 0, 255)

        elif i == 1:
            green = sparse.linalg.spsolve(coeffA, b)
            green = np.clip(green, 0, 255)
        else:
            blue = sparse.linalg.spsolve(coeffA, b)
            blue = np.clip(blue, 0, 255)
    resultImg = reconstructImg.reconstructImg(indexes, red, green, blue, targetImg)

    return resultImg
