#indexing for 1D array
"""import numpy as np
array1=np.array([10,20,30,40])
ind=array1[3]
print(ind)

import numpy as np
array1=np.array([10,-2,-5,10,20,30,40,77,100])
ind=array1[3]
print(ind)"""


#indexing for 2d array
"""import numpy as np
arr1=np.array([[10,20,30,40,100],[20,30,40,50,60]])
indexing=arr1[0:]
print(indexing)"""

# or
"""import numpy as np
arr1=np.array([[10,20,30,40,100],[20,30,40,50,60]])
indexing=arr1[:3]
print(indexing)"""  #output is same of both expression:


#if we want to acess only 1 row 3 index value 
"""import numpy as np
arr1=np.array([[10,20,30,40,100],[20,30,40,50,60]])
indexing=arr1[0,1]
print(indexing)"""

#if we want to acess only 1 row 3 index value 

"""import numpy as np
arr1=np.array([[10,20,30,40,100],[20,30,40,50,60]])
indexing=arr1[1,3]
print(indexing)"""

# for 3d array indexing..
"""import numpy as np
array1=np.array([[[10,20,30,40],[50,60,70,80],[90,100,110,120]]])
print(array1[1:])
"""

#print only 0 and 3 row
"""import numpy as np
a=np.array([[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]])
print(a[:,(0,3)])"""

# slice 1st two row and last two column print karo:
"""import numpy as np
a=np.array([[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]])
print(a[0:2,[2,3]])"""


#print every column of the given matrix
"""import numpy as np
a=np.array([[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]])

print(a[:,(0,1,2,3)])"""


#print only greater then 5
"""import numpy as np
x=np.array([3,10,6,1,15,8,2])
print(x[x>5])"""


#print only even number:

"""import numpy as np
x=np.array([3,10,6,1,15,8,2])
print(x[x%2==0])"""

#print only diognal elements of b array
"""import numpy as np
b=np.arange(1,26)
new_array=b.reshape(1,5,5)
diognal_new_array=new_array[0].diagonal()
print(diognal_new_array)"""


#print only last 3 row and 2 column slices:
"""import numpy as np
b=np.arange(1,26)
new_array=b.reshape(1,5,5)
print(new_array)
print()
print(new_array[0:,2:5,:]) #now staring 2 column:
print()
print(new_array[0:,:,0:2])"""


# Take every row last elements form index: 

"""import numpy as np
b=np.arange(1,26)
new_array=b.reshape(1,5,5)
print(new_array)
print()
print(new_array[0,0,4])
print(new_array[0,1,4])
print(new_array[0,2,4])
print(new_array[0,3,4])
print(new_array[0,4,4])"""



#print first 3 elements using slicing:
"""import numpy as np
a=np.array([10,20,30,40,50,60]))
print(a[0:4])"""

#last two elements slice:

"""import numpy as np
a=np.array([10,20,30,40,50,60])
print(a[4:6])"""


# print or slice form 5 to 12 elements:
"""
import numpy as np
a=np.arange(1,21)
print(a)
print(a[5:12])"""


#Take every 2nd elements:
"""import numpy as np
a=np.arange(1,21)
print(a[::2])"""


#slice only middle three:elemts
"""import numpy as np
a=np.array([5,10,15,20,25,30])
print(a[1:4])"""




























