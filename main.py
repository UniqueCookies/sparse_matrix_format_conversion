from scipy.io import mmread
import scipy.sparse as sp
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
def vertex_vertex_sparse(mat):
    mat = mat.tocsr()
    length = len(mat.data)
    mat.data = np.ones(length)
    return mat #return SCR format
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


#vertex_edge sparse format ---- NOT DONE
def vertex_edge_sparse(mat):
    mat = mat.tocoo()
    length = len(mat.data)
    data = np.ones(length)
    vertex = np.ones(length)
    edge = np.ones(length)
    n = 0
    for i in range (length):
        if mat.row[i]>mat.col[i]:
            vertex[i]=mat.row[i]
            vertex[-(i+1)]=mat.col[i]
            edge[i]=n
            edge[-(i+1)]=n
            n=n+1
    ve = sp.coo_matrix((data, (vertex, edge)),shape=(int(np.max(vertex))+1, int(np.max(edge))+1))
    return ve

#Laplacian matrix
def laplacian_matrix_sparse(mat):
    mat = mat.tocsr()
    length = len(mat.indptr)-1
    diagonal = np.zeros(length)
    for i in range (length):
        start = mat.indptr[i]
        end = mat.indptr[i+1]
        d = sum(mat.data[start:end])
        diagonal[i]=d
    indices = [i for i in range(length)]
    D = sp.coo_matrix((diagonal,(indices,indices)))
    D = D.tocsr()
    laplacian = D - mat
    return laplacian,D

#Modularity matrix
def modularity_matrix_sparse(mat):
    mat = mat.tocsr()
    T = sum(mat.data)
    laplacian, d = laplacian_matrix_sparse(mat)
    m = d.T @d
    B = mat - (1/T)*m
    return B

data = np.ones(6)
row =[0,1,1,2,2,3]
col = [1,0,2,1,3,2]
mat = sp.coo_matrix((data,(row,col)))
mat = mat.tocsr()

print(vertex_edge_sparse(mat).col)
#print(vertex_edge_sparse(mat))
#print(b)
