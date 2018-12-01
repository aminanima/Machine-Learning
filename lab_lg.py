import numpy as np

#если аппроксимация соответствует ожидаемому результату
def test(x, test, response):
    sum = 0
    for i in range (0, len(test)):
        sum = sum + x[i]*test[i]
    aux = approx(sum)
    if(aux == response): return True
    else:
        print 'approximation: \"', sum, '\" -> \"', aux, '\" expected: \"', response, '\"'
        return False

def Dataset(arq, matriz, vetor, col):
    i = 0;
    f = open(arq, 'r')
    for line in f:
        y = line.split(',')
        vetor.append(convertIris(y[col]))
        for j in range (0, col):
            matriz[i][j] = y[j]
        i = i+1

#converts flowers name to number
def convertIris(name):
    if(name == "Iris-setosa\r\n"):
        return 1
    if(name == "Iris-versicolor\r\n"):
        return 2
    if(name == "Iris-virginica\r\n"):
        return 3

#Converts number of flowers to name
def convertIrisBack(number):
    if(number == 1):
        return "Iris-setosa"
    if(number == 2):
        return "Iris-versicolor"
    if(number == 3):
        return "Iris-virginica"

def approx(n):
    v = []
    v.append(abs(1-n))
    v.append(abs(2-n))
    v.append(abs(3-n))
    if(min(v) == v[0]):
        return 1;
    if(min(v) == v[1]):
        return 2;
    if(min(v) == v[2]):
        return 3;

#definition of the data matrix A on the flower and definition vector b
LIN, COL = 120, 4
A = np.zeros([LIN, COL])
b = []
Dataset('Iris80p.txt', A, b, COL)

#test data
TAM1, TAM2 = 150, 4
T = np.zeros([TAM1, TAM2])
r = []
Dataset('IrisDataset.txt', T, r, TAM2)

#do some math
At = A.transpose()
AtA = np.dot(At, A)
Atb = np.dot(At, b)

#coefficients of linear approximation with the least squared error possible
x = np.linalg.solve(AtA, Atb)
print(x)

for i in range(0, TAM1):
    if(test(x, T[i], r[i])): print 'passed on'
    else: print 'did not pass', convertIrisBack(r[i]), 'case ', i