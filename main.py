from scipy.io import mmread
import numpy as np
import random

mat = mmread('baseball.mtx')
with open('baseball_labels.txt') as file:
    labels = file.read().splitlines()

'''''
random_team = random.choice(labels)
i = labels.index(random_team)
print(f'In 2022, the {random_team} played:')
row = mat.getrow(i)
for (j, num_games) in zip(row.indices, row.data):
    print(f'{num_games} games against {labels[j]}')
'''''
#convert to csr matrix
mat = mat.tocsr() #convert to csr matrix

def vertex_vertex(mat):
    m,n = mat.shape #get shape
    length = len(mat.indptr)
    A = np.zeros((m,n))
    i = 0
    for z in range(length-1):
        start = mat.indptr[z]
        end = mat.indptr[z+1]
        for k in range(start,end):
            j = mat.indices[k] #get which column to add
            A[i,j]=mat.data[k] #add the column
        i = i+1
    return A


