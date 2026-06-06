#array method:
"""import numpy as np
array1=np.array([[[[10,20,30,40],[50,60,70,80]]]])
print(np.shape(array1))
print(array1.ndim)
print(np.size(array1))
print(array1.dtype)
print(type(array1))
print(array1.astype(str))
print(len(array1))"""

"""import numpy as np
arr=np.array([10,20,30,40])
arr1=np.array([50,60,70,80])
new_arr=(arr,arr1)
print(np.concatenate_arr)"""

# importing function
"""import numpy as np
arr1=np.zeros([ 5,2])
new_array=arr1.reshape(1,1,5,2)
print(new_array)
print(new_array.ndim)"""

"""import numpy as np 
arr1=np.ones([3,4])
new_array=arr1.reshape(1,1,1,3,4)
print(new_array)
print(new_array.ndim)"""


"""import numpy as np
arr1=np.arange(1,10)
new_array1=arr1.reshape(1,1,1,1,3,3)
print(new_array1,new_array1.ndim)
"""
"""import numpy as np
arr=np.linspace(1,20,3)
arr2=arr.reshape(1,1,3)
print(arr2)
print(arr2.ndim)"""



# create an array which is having number blw 1 to 20 and having 4 row ,5 column and 4 dimension:
"""import numpy as np
array1=np.random.randint(1,20,(1,1,4,5))
print(array1.ndim)
print(array1)"""


"""import numpy as np
arra1=np.random.rand(1,1,5,2)
print(arra1)
print(arra1.ndim)"""

# 
"""import numpy as np
array1=np.full((1,1,2,3,7),8)
print(array1)
print(array1.ndim)"""

"""import numpy as np
array1=np.eye(3,2)
print(array1)
print(array1.ndim)"""


# How to genreate random number using numpy :
""""import numpy as np
x=np.arange(2,18) 
new_array=x.reshape(4,4)
print(new_array)"""


#Genreate an array of 5 random number blw 10 to 50 using numpy :
"""import numpy as np
array=np.random.randint(10,50,5)
print(array)"""


# Find its output:
"""import numpy as np

a=[[[1,2,3],
    [4,5,6]]]


print(a[0])
print(len(a))
print(np.shape(a))"""



""" find the predictions for this array:like
# Shape
# len
# dtype
# ndim
# size
#type:
import numpy as np
a=np.array([[[10]],
            [[20]],
            [[30]]])
print(np.shape(a))
print(len(a))
print(a.dtype)
print(np.ndim(a))
print(type(a))
print(np.size(a))"""


"""import numpy as np
a=np.array(["Ravi","Aman","Ritik"])
print(np.shape(a))
print(len(a))
print(a.dtype)
print(np.ndim(a))
print(type(a))
print(np.size(a))"""

"""import numpy as np
a=np.array([[10,"20"],
            [30,"40"]])
print(type(a))
print(np.shape(a))
print(len(a))
print(a.dtype)
print(np.ndim(a))
print(np.size(a))"""

# Reshape the given array into 3*4 :

"""import numpy as np
a=np.arange(1,13)
new_array=a.reshape(3,4)
print(new_array)"""


# first convert it into 3d array and its reshape should be (2,2,2)
"""import numpy as np
a=np.arange(1,9)
new=a.reshape(2,2,2)
print(new)
print(np.shape(new))"""


# solve this problem using reshape and (3,) column calcluate numpy yourself:
"""import numpy as np
a=np.arange(1,13)
new=a.reshape(3,-1)
print(new)"""

"""# Reshape it as:
# 2 blocks
# every block  having 3 rows
# and  every  row having  8 columns

import numpy as np
a=np.arange(1,49)
new=a.reshape(2,3,8)
print(new)"""
 
"""import numpy as np
a1=np.random.randint(2,20,(2,2,3))
print(a1)
print(a1.ndim)
new=a1.flatten()
print(new)
print(new.ndim)"""

"""solve this questions clarify that here are possible dot product:if shape of two array:
a=(2,3)
b=(3,4)
#let us create two array according to given shape()

import numpy as np
a=np.array([[3,4,5],
            [6,7,8]])
b=np.array([[3,4,6,8],
            [5,6,7,9],
            [9,6,7,4]])
find_dot_product=np.dot(a,b)
print(find_dot_product)"""

""" if  dot product is  possible then show the result shape:
A=A.shape = (2,3)
B.shape = (3,5)"""

"""import numpy as np
a=np.array([[5,6,6],
            [9,5,6]])
b=np.array([[6,7,8,9,3],
            [9,5,6,8,6],
            [3,4,5,2,1]])
Result=np.dot(a,b)
print(Result)
print(np.shape(Result))"""

# calculate its output:
"""import numpy as np

A = np.array([[1,2]])
B = np.array([[3],
              [4]])

print(np.dot(A,B))  # 11  there are 1 row and 1 column are multplied to each other:"""


# Complete this rule for np.product

# (m,n) × (?,?)
# Dot product is possible if (m.n)=(n.p)


# How to check that a matrix is square matrix or not in numpy:
# if output is =True then  matrix are square matrix :
# if output is =False then matrix are not a square matrix:  

"""import numpy as np
a=np.array([[10,20,30],
            [40,50,60],
            [60,70,80]])
print(a.shape[0]==a.shape[1])"""


# create a matrix with using random no.which is not a square matrix:
"""import numpy as np
a1=np.random.randint(2,10,(2,3))
print(a1)
result=a1.shape[0]==a1.shape[1]
print(result)"""

import numpy as np
a=np.array([[10,20,30],
            [40,50,60],
            [60,70,80]])
eigen_value=np.linalg.eig(a)

print(eigen_value)





