from scipy.io import mmread
import numpy as np
import random

mat = mmread('baseball.mtx')
with open('baseball_labels.txt') as file:
    labels = file.read().splitlines()
def vertex_vertex(mat): #make it into a large big matrix..
    mat = mat.tocsr()
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
    mat = mat.tocsr()
    length = len(mat.data)
    mat.data = np.ones(length)
    return mat
def vertex_edge(mat):
    mat = mat.tocoo() #work with COO format
    m = mat.shape[0]
    n = len(mat.data)//2
    A = np.zeros((m,n))
    for i in range(n):
        a = mat.row[i]
        b = mat.col[i]
        if a>=b:
            A[a,i]=1
            A[b,i]=1
    return A  #upper Traingle matrix

#vertex_edge sparse format