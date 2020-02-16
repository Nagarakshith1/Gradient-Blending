'''
  File name: getSolutionVect.py
  Author:
  Date created:
'''
import numpy as np
from scipy import signal

def getSolutionVect(indexes, source, target, offsetX, offsetY):

	laplace = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
	source_laplace = signal.convolve(source, laplace, mode='same', method='direct')
	list_indexes = np.argwhere(indexes > 0)
	list_b = list_indexes - np.array([offsetY,offsetX])
	N,a = list_b.shape
	SolVectorb = np.zeros((N,1))

	for i,j in zip(list_indexes,list_b):
		y = i[0]
		x = i[1]
		buffer = 0
		index_list = [indexes[y - 1][x] - 1, indexes[y + 1][x] - 1, indexes[y][x - 1] - 1, indexes[y][x + 1] - 1]  # above,below,left,right
		for l,k in enumerate(index_list):
			if k == -1:
				target_val = [target[y - 1][x], target[y + 1][x], target[y][x - 1], target[y][x + 1]]  # above,below,left,right
				buffer = buffer + target_val[l]
		SolVectorb[int((indexes[i[0]][i[1]])-1)] = source_laplace[j[0]][j[1]] + buffer

	return SolVectorb
