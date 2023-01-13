import numpy as np

arr = np.array([1, 4, 5])

#print(arr)
#print("type of array :", type(arr))
#print("shape of array:", arr.shape)


#print(arr[0], arr[1], arr[2])
arr[1] = 10
#print(arr)

arr2D = np.array([
    [2, 5, 6],
    [1, 5, 3]
])
#print(arr2D)
#print(arr2D.shape)

#print(arr2D[0], type(arr2D[0]))
#print(arr2D[1], type(arr2D[1]))

print(
    arr2D[0, 0], arr2D[0, 1], arr2D[0,2]
)
print(
    arr2D[1, 0], arr2D[1,1],  arr2D[1,2]
)

zeros = np.zeros((3, 4))

#print(zeros, zeros.shape)

ones = np.ones((4, 5))
#print(ones, ones.shape)

consts = np.full((3, 7), 5)
print(consts, consts.shape)

random = np.random.random((4, 5))
print(random, random.shape)

consts = np.full((5, 5),5)
print(consts, consts.shape)

for i in range(5):
    for j in range(5):
        if i==j:
            consts[i,j]=0

            #print(consts)
temp = np.array([
    [5, 4,  3, 1],
    [7, 3, 9, 3 ],
    [6, 4, 2, 4 ]
])

print(temp)

s_arr = temp[:2, 1:3]
S_arr = temp[1:, 2:]
print(s_arr)

#print(temp[2, :])
#print(temp[0:2, :])

#print(temp)
#print([temp>2])
#print(temp[temp>2])

x = np.array([3, 4])
print(x)
print(x.dtype)
y = np.array([5, 4, 6], dtype=np.float64)
print(y, y.dtype)

print(x)
print(y)
#elementwise sum
print("Normal sum: \n", x+y)
print("Numpy sum: \n", np.add(x,y))

print(np.substract(x,y))
print(np.multiply(x,y))
print(np.divide(x,y))

x = np.array([[3, 4], [7, 6]], dtype=np.float64)
x = np.array([[1, 2], [3, 2]], dtype=np.float64)

v = np.array([9, 10])
w= np.array([5, 6])

#inner product
print(v.dot(w))
print(np.dot(v,w))

print(x.dot(y))

x=np.array([
      [1, 2, 3]
      [4, 3, 1]
      [5, 8, 3]
])

print(x)
print(x.T)

print(np.sum(x))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))
