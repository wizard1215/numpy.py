# stacking 
# 1) np.vstack() for 2d array:

"""import numpy as np
array=np.array([1,2,3,4])
array1=np.array([[5,6,7,8],[10,11,13,14]])
array3=np.array([[9,10,11,12]])
new_array=array,array1,array3
print(np.vstack(new_array)) """


# add new students :
"""import numpy as np
data=np.array([[80,90,85],[70,75,88]])
data1=np.array([33,50,60])
data3=np.array([100,200,300])
data4=np.array([12,19,20])
new_data=data,data1,data3,data4
print(np.vstack(new_data))"""

# np.hstack the hstack is join the horizontlly arrays:it produe error when the row number are not same in array:
"""import numpy as np
arr=np.array([1,2,3,4,5])
arr1=np.array([6,7,8,9,10])
new_array=np.array(arr,arr1) 
print(np.hstack(new_array))"""


"""import numpy as np 
arr1=np.array([[1,2,3,4],[5,6,7,8]]) 
arr2=np.array([[9,10,11,12],[13,14,15,16]]) 
arr3=np.array([[17,18,19,20],[21,22,23,24]])
new_array=np.array([arr1,arr2,arr3])
print(np.hstack(new_array))
print(new_array.ndim)"""


#3 np.dstack() depth stack: for 1d array:
"""import numpy as np
a=np.array([10,20,30])
b=np.array([40,50,60])
new_array=a,b
print(np.dstack(new_array))
print(a.ndim)
print(b.ndim)"""

# for 2d array
"""import numpy as np
a=np.array([[10,20,30],[40,50,60]])
b=np.array([[70,80,90],[100,110,120]])
new_array=np.array([a,b])
print(np.dstack(new_array))
print(new_array.ndim)
print(np.shape(new_array))  """  



# np.random.seed its give the fix starting point number so that we find the same random number :
"""import numpy as np
array=np.random.seed(9)
arr2=(np.random.randint(2,100,9))
print(arr2.reshape(3,3))"""




# np.random.normal:  its give the random number with centre,spread and size:
#give me 5 random number which is arround 50 with some distance
"""import numpy as np
array=np.random.normal(50,1,5)
print(array)"""

#give me 5 random number which is having some distance with 50 :
"""import numpy as np
array=np.random.normal(1,10,5)
print(array)"""


#np.random.uniform: it is give the too the random number but around its are upeer lower :
"""import numpy as np
array=np.random.uniform(1,10,5)
print(array) """



# np.dot() it is work two type 1)vector dot product and matrix multiplication:
#1)vector dot product 1d array single number input:
"""import numpy as np
arr=np.array([1,2,3,4])
arr1=np.array([5,6,7,8])
print(np.dot(arr,arr1))"""

"""import numpy as np
arr=np.array([1,2])
arr1=np.array([5,6])
print(np.dot(arr,arr1)) """


#2)matrix multiplication:2d array matrix output:
"""import numpy as np
a=np.array([[1,2],
            [3,4]])
b=np.array([[5,6],
            [7,8]])
print(np.dot(a,b))"""

#for 3d array

"""import numpy as np
a=np.array([[[1,2],
            [3,4]]])
b=np.array([[[5,6],
            [7,8]]] )
print(np.dot(a,b))"""


#if multiply matrix * vector:
"""import numpy as np
a=np.array([[1,2,3],
            [4,5,6]])
b=np.array([1,1,1])
print(np.dot(a,b))"""

#dot product question:
"""import numpy as np
a=np.array([[1,2,3],
           [0,1,4],
           [5,6,0]])     
b=np.array([1,0,1])
print(np.dot(a,b))"""

#dot product question:
"""import numpy as np
a=np.array([[1,2],
            [3,4]])
b=np.array([[5,6],
            [7,8]])
print(np.dot(a,b))"""

# np.matmul() it is work same as np.dot() but some basic diffrenece:
"""import numpy as np
a=np.array([[[1,2],
            [3,4]],
            
           [[5,6],
            [7,8]],
            
            [[1,1],
            [1,1]]])

b=np.array([[1,0],
            [0,1]])
print(np.matmul(a,b))"""

#2nd matmul qustions:
"""import numpy as np
a=np.array([[1,2,3],
   [4,5,6]])

b=np.array([[1],
           [1],
           [1]])
print(np.matmul(a,b))"""

#np.linalg.inv() its return inverse of the matrices:

"""import numpy as np
a=np.array([[[1,1,2],
             [2,3,4],
             [4,5,6]]])          
print(np.linalg.inv(a))
print(np.linalg.det(a))  
print(a.ndim)
print(np.shape(a))"""


#np.linalg.inv questions:
"""import numpy as np
a=np.array([[4,7],[2,6]])
print(np.linalg.det(a))
print(np.linalg.inv(a))"""

#np.linalg.inv questions:
"""import numpy as np
b=np.array([[1,2,3],
   [1,4,3],
   [1,3,4]])
print(np.linalg.det(b))
print(np.linalg.inv(b))"""


# if matrix detrminate 0 then inverse not exist then error occured:  
"""import numpy as np
a=np.array([[1,2],
            [2,4]]) 
print(np.linalg.det(a))
print(np.linalg.inv(a))"""



#print only columns using indexing and slicing..  
"""import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[:,0])"""


#print only greater than 15
"""import numpy as np
a=np.array([12,7,19,5,16,30])
print(a[a>15])"""

#print only even number
"""import numpy as np
a=np.array([12,7,19,5,16,30])
print(a[a%2==0])"""

# print value greater thena 10 and less than 25:
"""import numpy as np
a=np.array([12,7,19,5,16,30])
print("greater than 10=",a[a>10])
print("less than 25=",a[a<25])"""




"""import numpy as np
a=np.array([10,20,30,40])
b=np.array([50,60,70,80])
c=np.array([90,100,110,120])
new_array=np.vstack([a,b,c])
print(new_array)"""


   







