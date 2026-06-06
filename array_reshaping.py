# reshape: it is change the array structure ...
"""import numpy as np
array=np.arange(2,20)
print(array.reshape(2,9))"""


# create  a array which is contain 20 to 40 digit in one 1d and then convert it:
# 5*4array so we change the shape this array and this dimension:
"""import numpy as np
array2=np.arange(0,20)
print(array2) 
print(array2.reshape(4,5))"""

# if we want to change dimesion of array from 2d to  3d:

"""import numpy as np
array2=np.arange(1,17)
resape=array2.reshape(2,4,2)
print(resape)
print(resape.ndim)"""

#if we want to change dimesion of array from 3d to 4d:
"""import numpy as np
array3=np.arange(1,21)
shap=array3.reshape(2,2,5)
print(shap)
print(shap.ndim)"""

#if we want to change dimesion of array from 4d to 5d:
"""import numpy as np
array3=np.arange(1,41)
print(np.shape(array3))
shap=array3.res hape(1,1,2,5,4)
print(shap)
print(shap.ndim)"""


#flatten as we 2d array convert it into the 1d array use flatten
"""import numpy as np
array4=np.array([[1,2,3],[4,5,6]])
flat=array4.flatten()
print(flat)"""

"""import numpy as np
array4=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
flat=array4.flatten()
print(flat)
print(array4.ndim)
print(flat.ndim)"""

#if convert 4d in 1d

"""import numpy as np
array4=np.array([[[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]]])
flat=array4.flatten()
print(flat)
print(array4.ndim)
print(flat.ndim)"""

#if convert 5d in 1d:

"""import numpy as np
array4=np.array([[[[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]]]])
flat=array4.flatten()
print(flat)
print(array4.ndim)
print(flat.ndim)"""

# ravel  it is ame as flatten but is it give change in reval if chnage reveal:
#then orignal data is automatically change
"""import numpy as np
array5=np.array([[1,2,4],[5,6,7]])
print(array5.ravel())"""

# resize()
"""import numpy as np
array5=np.array([1,2,3,4,5,6])
array5.resize(3,2)
print(array5)"""

#for 2d 

"""import numpy as np
array5=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
array5.resize(3,5)
print(array5)"""


# here are two resize 
#1) which is used with as np.resize(arr,new_size) fill repeted vale
#2)which is used another type np.(arr) fill zero

#1"""import numpy as np
"""a=np.resize((2,3,4,5),6)
print(a)"""

2# 
"""import numpy as np
array=np.array([1,2,3,4,5,6])
array.resize(2,4)
print(array)"""










