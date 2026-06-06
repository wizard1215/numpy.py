#np.array
"""import numpy as np
array1=np.array([10,20,30])
print(array1)"""

# np.array can convert the tuple into array as:
""""import numpy as np
a1=np.array([[(10,20,40),
            (50,60,70)]])
print(np.array(a1))
print(np.shape(a1))
print(a1.ndim)"""


# 2) np.zeros
"""import numpy as np
array1=np.zeros((3,2))
print(array1)"""

#3) np.ones
"""import numpy as np
array1=np.ones((2,3))
print(array1)"""

#4) np.arrange it is work same as range in pytho:range(start,stop,step):
"""import numpy as np
array1=np.arange(1,20,2)
array2=np.arange(1,20,3)
print(array1)
print(array2)"""

#5) np.linespace it give the gap number blw start and end equally:
"""import numpy as np
array1=np.linspace(1,20,30)
print(array1)"""

# 6) np.random.rand it is given the float number blw zero to one:
# for only row and column
"""import numpy as np
a=np.random.rand(2,5)
print(a)
print(a.ndim)"""

# for with block row and column in 3d as block,row,column
"""import numpy as np
a=np.random.rand(2,2,5,4)  
print(a)
print(a.ndim)"""

#7) np.random.randint it is given the all integer number or complete numbre
# for only single number or 1D
"""import numpy as np
array1=np.random.randint(1,10)
print(array1)"""

# for 2d array or row ,column 
"""import numpy as np
array1=np.random.randint(1,10,(1,2))
print(array1)"""

# for 3d array:  number blw  : row,column:
"""import numpy as np
array1=np.random.randint(1,10,(2,5))
print(array1)
print(array1.ndim)"""

# import numpy as np

"""a1=np.random.randint(1,20,(2,3))

print(a1)
print(a1.ndim)"""


#9) np.full()  filled for same value according to us desired:
"""import numpy as np
a=np.full((2,3),6)
print(a)"""

#10) np.eye()
"""import numpy as np
a=np.eye(4)
print(a)"""







