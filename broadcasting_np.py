"""import numpy as np
x=np.array([1,2,3,4])
print(np.shape(x))
y=np.array([[2],[3],[4]])
print(np.shape(y))
print(x+y)"""


"""import numpy as np
x=np.array([10,20,30,40])
y=5
add=x+y
print(x + y) """


# This is through error because elements shape are not good for bradcasting:
"""import numpy as np
a1=np.array([10,20,30])
a2=np.array([10,20,30,40])
print(a1+a2)"""

#create a two array x and y x is(1,4),and y is (4,1) shape then broadcast  them: 

"""import numpy as np
x=np.array([1,2,3,4])
print(x.shape)
y=np.array([[1],[2],[3],[4]])
print(y.shape)
print(x+y)"""


# if There are two array a and b a shape is (3,4) and b shape is (4)then what is the shape of a and b:

"""import numpy as np
a=np.array([[1,2,3,4],
            [4,5,6,7],
            [7,8,9,8]])

b=np.array([1,2,3,4])
new_array=a+b
print(new_array.shape)"""

# Array x shape is (5,3,2) and Array y shape is(3,1) then find the shape of X+y :
"""import numpy as np
x=np.arange(2,32)
new_array=x.reshape(5,3,2)
print(new_array)
y=np.array([[2],
            [3],
            [4]])
new_array1=new_array+y
print(new_array1)
print(new_array1.shape)"""


#Array z shape is(2,4) and find array Z=5 shape :

"""import numpy as np
z=np.array([[2,3,4,8],
            [4,5,6,7]])
add=z+5
new_array=add+z
print(new_array)
print(new_array.shape)"""

# if array A shape is (3,4) and array B shape is (4,) then find the shape of a*b

"""import numpy as np
a=np.array([[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]])
print(a.shape)
b=np.array([1,2,3,4])
print(b.shape)
new_array=a*b
print(new_array.shape)"""



#solve this:
# Identify the shape:and find the final output 
"""import numpy as np

a=np.array([1,2,3])
print(np.shape(a))
b=np.array([[10],
            [20]])
print(np.shape(b))
print(a+b)"""

# Broadcasting of these array:
"""import numpy as np
a=np.array([[1],
            [2],
            [3]])

b=np.array([10,20])
print(a+b)"""

# solve this:
"""import numpy as np
a=np.array([[1,2,3]])
b=np.array([[10],
            [20],
            [30]])

print(a+b)"""

#solve this :

"""import numpy as np
a=np.array([[1,2],
            [3,4]])
b=np.array([10,20])
print(a+b)
"""

# solve this:
"""import numpy as np
a=np.array([[1],
            [2]])
b=np.array([[10,20,30]])
print(a+b)"""


# solve this not adding multiplied broadcasting:
"""import numpy as np
a=np.array([[1,2,3]])
b=np.array([[10],
            [20]])
print(a*b)"""

# find its final output shape and show that there are broadcasting possible:
"""import numpy as np
a=np.array([[1],
            [2],
            [3]])
b=np.array([1,2,3,4,5])
print(np.shape(a))
print(np.shape(b))
print(a+b)"""


# Data annalyst broadcsting like:
"""import numpy as np
sales=np.array([100,200,300])
tax=10
print(sales+tax)"""





