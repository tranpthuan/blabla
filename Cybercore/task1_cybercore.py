import numpy as np
import matplotlib.pyplot as plt
import csv

read1 = []
read2 = []

with open('train.csv',"rb") as csvfile:
    read = csv.reader(csvfile)
    read.next()
    for row in read :
        if len(row) <= 1 :      #data preprocessing c
            continue
        read1.append(row[0])
        read2.append(row[1])

X = np.array([read1], dtype = float).T
Y = np.array([read2], dtype = float).T

#Xbar for the mean value
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)

#processing lines
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T,Y)
w = np.dot(np.linalg.pinv(A),b)
w0 = w[0][0]
w1 = w[1][0]

print(w0)
print(w1)

x0 = np.linspace(0, 110, 2)
y0 = w0 + w1*x0

plt.plot(X, Y, 'm.')     # data
plt.plot(x0, y0, 'c')               # the fitting line
plt.axis([0, 110, 0, 110])
plt.xlabel('X')
plt.ylabel('')
plt.show()

temp = []
data = []

with open('test.csv',"rb") as csvtest :
    test = csv.reader(csvtest)
    test.next()
    for i in test:
        if(len(i) < 1) :
            continue
        temp.append(i[0]);

data = np.array(temp, dtype = float)

with open('predict.csv',"wb") as output :
    writer = csv.writer(output)
    writer.writerow(['x','y'])
    for j in data :
        y1 = j*w1 + w0
        writer.writerow([j, y1])

csvtest.close()
csvfile.close()
output.close()