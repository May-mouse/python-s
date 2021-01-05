
import random
def M(): return [[random.randint(-10, 10) for i in range(5)] for j in range(5)]

for row in M():
    print(row)

for i in  range (0,4):
    for j in  range (0,4):
        if M == 0:
            M[i:].append(0)
            M[:j].append(0)
        else:
            M= M

for row in M():
    print(row)








