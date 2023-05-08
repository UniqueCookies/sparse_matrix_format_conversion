from scipy.io import mmread
import scipy.sparse as sp
import numpy as np
import random

baseball = mmread('baseball.mtx')
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
    n = 0 #count number of edges
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
    length = mat.shape[1]
    d = mat@np.ones(length)
    indices = [i for i in range(length)]
    D = sp.coo_matrix((d,(indices,indices)))
    laplacian = D - mat
    return laplacian
#edge_edge sparse matrix
def edge_edge_sparse(mat):
    ve = vertex_edge_sparse(mat)
    return ve@ve.T
#Modularity matrix
def modularity_matrix(mat):
    T = sum(mat.data)
    d = mat@np.ones((mat.shape[1],1))
    B = mat - (1/T)*d@d.T
    return B

B= modularity_matrix(baseball)
ve = edge_edge_sparse(baseball)
print(ve)