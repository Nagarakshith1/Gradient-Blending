'''
  File name: getCoefficientMatrix.py
  Author:
  Date created:
'''
import numpy as np
from scipy import sparse

def getCoefficientMatrix(indexes):
	N = np.sum(1*indexes>0)
	coeffA = np.zeros((N,N))
	list = np.argwhere(indexes>0)

	for i in list:
		y = i[0]
		x = i[1]
		coeffA_row = int (indexes[y][x] - 1)
		coeffA[coeffA_row,coeffA_row] = 4
		index_list = [indexes[y-1][x]-1, indexes[y+1][x]-1, indexes[y][x-1]-1 ,indexes[y][x+1]-1] #above,below,left,right
		for j in index_list:
			if j>0:
				coeffA[coeffA_row,int(j)] = -1

	coeffA = sparse.csr_matrix(coeffA)
	return coeffA
