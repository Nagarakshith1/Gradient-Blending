'''
  File name: getIndexes.py
  Author:
  Date created:
'''

import numpy as np

def getIndexes(mask, targetH, targetW, offsetX, offsetY):
	maskH,maskW = mask.shape
	indexes = np.zeros((targetH,targetW))
	i = 1
	for y in np.arange(maskH):
		for x in np.arange(maskW):
			if (mask[y,x]>0):
				indexes[y+offsetY][x+offsetX] = i
				i = i+1
	return indexes