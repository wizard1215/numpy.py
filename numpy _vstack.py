# The vstack is vertical stack which is add row at above to each other:if row and column same size otherwise errro occured: 
"""import numpy as np
a=np.array([10,20,30,40])
b=np.array([20,30,40,50])
new_array=a,b
print(np.vstack(new_array))"""

#if one array 2d 

"""import numpy as np
a=np.array([[10,20,30],
           [40,50,60]])
b=np.array([1,2,3])
c=np.array([23,24,25])
new_array=a,b,c
print(np.vstack(new_array))"""


#if both array 2d:
"""import numpy as np
arr1=np.array([[100,200,300],
               [400,500,600]])
arr2=np.array([[700,800,900],
               [1000,1100,1200]])
new_array=arr1,arr2
print(np.vstack(new_array))"""


#if you use a 1d array then vstack is automatically converted it into 2d array:
"""import numpy as np
arr=np.array([12,13,14,15,16])
print(arr.ndim)
new_aray=np.vstack(arr)
print(new_aray.ndim)
print(np.vstack(new_aray))"""

#find output of this code:
"""import numpy as np
a=np.array([10,20])
b=np.array([30,40])
c=a,b
print(np.vstack(c))"""



#now find the output of this code:
"""import numpy as np
a=np.array([[1,2,3]])
b=np.array([[4,5,6]])
c=np.array([[7,8,9]])
d=a,b,c
print(np.vstack(d))""" 

# based on axis: if axis is 0 then it is work same as vstack add row up to buttom side:

"""import numpy as np
a=np.array([[10,20,30]])
b=np.array([[30,40,50]])
c=np.array([[60,707,80]])
print(np.concatenate((a,b,c),1))"""


#if axis is 1 then it is add row in a left to right side :as
"""import numpy as np
a=np.array([[10,20,30]])
b=np.array([[30,40,50]])
c=np.array([[60,707,80]])
print(np.concatenate((a,b,c),1))"""

# 2nd example:
"""import numpy as np
a=np.array([[10,20,30]])
b=np.array([[40,50,60]])
print(np.vstack((a,b)))
print(np.concatenate((a,b),0))"""


"""import numpy as np
a=np.array([10,20,30,40])
b=np.array([50,60,70,80])
c=np.array([90,100,110,120])
new_array=np.vstack([a,b,c])
print(new_array)"""












