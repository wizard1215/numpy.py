# The Array is diifrence from a list as:  
"""import numpy as np
a=np.array([12,13,40,10])
b=np.array([10,20,30,10])
print(a+b)"""

# 2 if...
"""a=np.array([10,20,30,100])
b=np.array([10])
print(a+b)"""

# 3.if 
"""a=np.array([10,20,40])
b=np.array([10])
print(a*b)"""

# you can store only one data type value in array :
"""l1=np.array([10,"20",30.1,"True"])
print(l1)"""

# if 
"""l2=np.array([12,30,40.4])
print(l2)
"""

# if we are not use the same data size in array as:
"""array1=np.array([[12,34,45,67],[10,23,45,40]])
print((type(array1)))"""
# but it is possible in list:

"""array1=[[12,34,45,67],[10,23,45]]
print(array1)"""



# create a matrix with using numpy which is containing the 4 row and 5 column:   

"""arr=np.array([[12,34,56,60,20],[10,20,30,40,30],[37,38,49,50,50],[10,20,0,80,90]])
print(arr)"""


#create a matrix with using numpy which is containing the the 3 row and 4 column:
"""matrix=np.array([[12,20,14,15],[10,20,30,40],[17,18,19,20]])
print((matrix))"""

#The slicing is working in numpy array as well as the list:
"""matrix=np.array([[12,20,14,15],[10,20,30,40],[17,18,19,20]])
print(matrix[0:2,2:3])"""

# find the above cerated array its using all  attribute of array:like 
#number of elments in arrary:
#shape of array:
#type of array :
#size of array:
#diemensional of array:
# len (array)
#array.astype(int)convert array to diffrent type...

"""import numpy as np
matrix=np.array([[12,20,14,15],[10,20,30,40],[17,18,20,10]])
shap=np.shape(matrix)
print("The shape of matrix as row and column",shap)
print("The size pr elements in matrix is as  ",np.size(matrix))
print("The dimesnional of matrix is",np.ndim(matrix))
print("The type of array is" ,matrix.dtype)
print(type(matrix))
print(matrix.astype(bool))
print(len(matrix))"""


"""import numpy as np
a=np.random.randint((1,20, 4,5))
print(a)"""

