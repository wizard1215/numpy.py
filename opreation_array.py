#1) for adding
"""import numpy as np
array1=np.array([10,20,30,40,50 ])
array2=np.array([20,30,40,60,70])
print(array1+array2)"""


#2) for subtract
"""import numpy as np
array1=np.array([10,20,30,40,50 ])
array2=np.array([20,30,40,60,70])
print(array2-array1)
print(np.subtract(array2,array1))"""

#3) for multiply:

"""import numpy as np
array1=np.array([10,20,30,40,50 ])
array2=np.array([20,30,40,60,70])
print(array1*array2)
print(np.multiply(array1,array2))"""

#4) for dividing...
"""import numpy as np
array1=np.array([[10,20],[40,50] ])
array2=np.array([[20,30],[60,70]])
print(array2/array1)
print(np.divide(array2,array1))"""

#5) for power
"""array1=np.array([2,3,4,5 ])
array2=np.array([3])
print(np.pow(array1,array2))"""


#6) for finding square root:
"""import numpy as np
array1=np.array([8,27,16,125 ])
#array2=np.array([3])
print(np.sqrt(array1))
print(array1.astype(int))"""

#7) There are various method of array in numpy..
#1 concatination:
"""import numpy as np
a1=np.array([[10,20],[30,15]])
a2=np.array([[5,6],[7,12]])
print(np.concatenate([a1,a2],axis=1))"""


#8) np.sum()
"""import numpy as np
a1=np.array([10,20,30,15])
sum=np.sum(a1)
print(sum)"""

# for 2d

"""import numpy as np
a1=np.array([[10,20,30,15],[25,30,30,20]])
sum=np.sum(a1)
print(sum)"""

#based on axis if axis is 0 then wrok sum is row finish column -wise,if axix is 1 then sum work is column finish sum row wise :
"""import numpy as np
b=np.array([[10,20],
            [30,40]])
sum=np.sum(b,0)
print(sum)"""
  

"""import numpy as np
b=np.array([[10,20],
            [30,40]])
sum=np.sum(b,1)
print(sum)"""

#9) np.mean( )the mean  is return the average of numbers in numpy:
"""import numpy as np
array=np.array([2,3,4,1])
average=np.mean(array)
print(average)"""

#for 2d array
"""import numpy as np
array=np.array([[2,3,4,1],[50,60,70,80]])
average=np.mean(array)
print(array.ndim)
print(average)"""


# for 3d array
"""import numpy as np
array=np.array([[[2,3,4,1],[50,60,70,80]]])
average=np.mean(array)
print(average)
print(array.ndim)"""

#np.mean with axis if axis 0 then average computation based upon column row finish:
"""import numpy as np
a=np.array([[3,4,5],
            [6,7,8]])
axis=np.mean(a,0)
print(axis)"""


#np.mean with axis if axis 1 then average computation based upon Row , column finish

"""import numpy as np
a=np.array([[3,4,5],
            [6,7,8]])
axis=np.mean(a,1)
print(axis)"""
 
# second example #np.mean with axis if axis 0 then average computation based upon column row finish:

"""import numpy as np
array=([[2,4,4],[4,4,4]])
avrage=np.mean(array,0)
print(avrage)"""

#np.mean with axis if axis 1 then average computation based upon Row , column finish
"""import numpy as np
array=([[2,4,4],[4,4,4]])
avrage=np.mean(array,1)
print(avrage)"""

#10) np.std the if std colsely  
"""import numpy as np
array=np.array([10,20,30])
print(np.std(array))"""

# np.std if std spread
"""import numpy as np
array=np.array([10,50,100,150])
print(np.std(array))"""

# if the axis as 0 then

"""import numpy as np
array=np.array([[10,50],[100,150]])
print(np.std(array,0 ))"""

#if the axis as  then

"""import numpy as np
array=np.array([[10,50],[100,150]])
print(np.std(array,0 ))"""


#11) np min find for the minimum value from the array: 1d  array

"""import numpy as np
array=np.array([10,20,3,40,5,1,67])
find=np.min(array)
print(find)"""

#for 2d array
"""import numpy as np
array=np.array([[10,20,3,40,5,1,67],[12,10,3,4,0,7,9]])
find=np.min(array)
print(find)"""

#if axis is 0 then it finish row find only from the column:
"""import numpy as np
array=np.array([[10,20,3,40,5,1,67],[12,10,3,4,0,7,9]])
find=np.min(array,0)
print(find)"""

#if axis is 1 then it finish column find only from the Row:
"""import numpy as np
array=np.array([[10,20,3,40,5,1,67],[12,10,3,4,0,7,9]])
find=np.min(array,1)
print(find)"""
 


#12)np.max() it find for maximum value from the array:
"""import numpy as np
array=np.array([10,20,3,40,5,1,67])
find=np.max(array)
print(find)"""

#for 2d array:
"""import numpy as np
array=np.array([[10,20,3,40,5,1,67],[2,3,10,11,200,350,3000]])
find=np.max(array)
print(find)"""

# if axis 0 then: it finish row ,find only from the column:

"""import numpy as np
array=np.array([[10,20,3,40,5,1,67],[2,3,10,11,200,350,3000]])
find=np.max(array,0)
print(find)"""

#if axis 1 then: it finish column ,find only from the Row:
"""import numpy as np
array=np.array([[10,20,3,40,5,1,67],[2,3,10,11,200,350,3000]])
find=np.max(array,1)
print(find)"""

#create two array 3*3 and perform opreation elements wise:
"""import numpy as np
array1=np.arange(1,10)
arr1=array1.reshape(3,3)
print(arr1)
print()
array2=np.arange(10,19)
arr2=array2.reshape(3,3)
print(arr2)"""


#13) np.nan()
"""import numpy as np
x=np.nan
print(type(x))"""


"""import numpy as np
a=np.array([10,20,30,np.nan,90])
print(a)"""

# np.nan not is equally to any value or self value:
"""import numpy as np
x=np.nan==np.nan
print(x)"""

# the np nan is corrupted to any calculation:
"""import numpy as np
x=np.array([10,20,30,40,np.nan,50,60])
x1=np.sum(x)
print(x1)"""


# for handled this exception we use nansum:
"""import numpy as np
x=np.array([10,20,30,40,np.nan,50,60])
x1=np.nansum(x) 
print(x1)"""


#14) is nan()
"""import numpy as np
x=np.isnan(np.nan)
print(x)"""


#check that np.isnan occured or not
"""import numpy as np
array=np.array([10,20,30,40,np.nan,100,130])
check=np.isnan(array)
print(check)"""


# count the nan value from any array:
"""import numpy as np
a=np.array([10,20,30,np.nan,1000,200,np.nan,89,102,np.nan])
count=np.isnan(a)
print(count)
print(count.sum())"""


# 16) np.nanmean its return the avrage of the values to ignore nan value:
"""import numpy as np
arr=np.array([10,10,10,10,np.nan,np.nan,10,10])
find_avg=np.nanmean(arr)
print(find_avg)"""

#17) np.nanstd its return the standrd deviative value : to ignoring the nan value:
"""import numpy as np
arr=np.array([10,20,np.nan,40])
find=np.nanstd(arr)
print(find)"""


# Replacing opreation to any num or value as:
import numpy as np
students_marks=np.array([40,55,75,80,np.nan,90,33,np.nan])# Replace the np.nan values to 0 then:
replaced=np.nan_to_num(students_marks ,nan="Invalid")
print(replaced)


