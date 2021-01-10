import random
import random
def M():
    M = []
    for j in range(4):
        M.append([])
        for i in range(5):
            M[j].append.int(random.randint(-10,10))
            return M()



def printMatrix (M):
    for i in range(0, 5):
        row = ''
        for j in range(0, 4):
            cell = M[i][j]
            cell_formated = f'{cell: >3},'

        printMatrix(M)



L=[]

for j in range(0, 4):
    for i in range(0, 5):
        cell=M
        if cell == 0:
            L[i:]= 0
            L[:j]=0
        else:
            L = cell


def printMatrix (L):
 for i in range(0, 5):
        row = ''
        for j in range(0, 4):
            cell = L[i][j]
            cell_formated = f'{cell: >3},'

            row = row + cell_formated
            printMatrix(row)

