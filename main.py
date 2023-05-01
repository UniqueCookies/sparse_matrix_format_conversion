from scipy.io import mmread
import numpy as np
import random

mat = mmread('baseball.mtx')
with open('baseball_labels.txt') as file:
    labels = file.read().splitlines()

#convert to csr matrix
mat = mat.tocsr() #convert to csr matrix

def vertex_vertex(mat): #make it into a large big matrix..
    m,n = mat.shape #get shape
    length = len(mat.indptr)
    A = np.zeros((m,n))
    i = 0
    for z in range(length-1):
        start = mat.indptr[z]
        end = mat.indptr[z+1]
        for k in range(start,end):
            j = mat.indices[k] #get which column to add
            A[i,j]=1 #add the column
        i = i+1
    return A #make i
def vertex_vertex_sparse(mat):  ##make sure the matrix is in SCR format
    length = len(mat.data)
    mat.data = np.ones(length)
    return mat
