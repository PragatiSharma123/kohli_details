'''from array import *
vals = array ('i', [5, 9, -8, 4, 2])
for e in vals:
    print(e)'''


'''from array import *
vals = array('i', [5, 9, -8, 4, 2])
print(vals.buffer_info())'''

'''from array import *
vals = array('i',[5, 9, -8, 4, 2])
newArr = array (vals.typecode,(a for a in vals ))

for e in newArr:
    print(e)'''

8
'''from array import *
vals = array('u',['a','e','i'])

for e in vals:
    print(e)'''

'''from array import *
arr = array('i',[])
n = int(input("Enter the length of the array"))
for i in range(n):
    x= int(input("Enter the next value"))
    arr.append(x)
    print(arr)

    val = int(input("enter the value for search"))
    k=0
    for e in arr:
        if e==val:
            print(k)
            break
        k+=1
        print(arr.index(val))'''


from numpy import *
arr1 = array([2, 6, 8, 1, 3])
arr2 = arr1.copy()
arr1[1] = 7
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

