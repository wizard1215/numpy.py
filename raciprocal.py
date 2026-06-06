# np.raciprocal is return the reverse of the number: but it perform ,
# only the numerical data int and flot cannot work on the string or bolean type data:
# it is work only 1 array:

"""import numpy as np
a1=np.array([10,20,30])
new=np.reciprocal(a1,dtype=float)
print(new)"""

"""import numpy as np
a1=np.array([[1,2,3],
             [5,6,7]])
a2=np.array([[4,5,6],
            [7,8,9]])
new_array=np.rec iprocal(a1)
new_array1=np.reciprocal(a2) 
print(new_array)
"""

#Now it giving the result only integer number if we want,
#to perfect output then we use dtype =float as

"""import numpy as np
a1=np.array([[1,2,3],
             [5,6,7]])
a2=np.array([[4,5,6],
            [7,8,9]])
new_array=np.reciprocal(a1,dtyep=float)
new_array1=np.reciprocal(a2,dtype=float) 
print(new_array)"""


# It work only integer or numerical array not string or bollean data:
"""import numpy as np
a1=np.array(["Ritik","Ravi","Nikhile"])
new=np.reciprocal(a1)
print(new) """# now it through error :

# for solve the string data there are many function which can we use for our data:
"""import numpy as np
names=np.array(["tom","jerry","elon mask"])# if we want to captialize these name then use:
result=np.char.upper(names)
print(result)"""     

# if we want to small them  these name then use:
"""import numpy as np
names=np.array(["Tom","Jerry","Elon Mask"])
result=np.char.lower(names)
print(result)"""


"""import numpy as np
a1=np.array([[1,0],
             [0,1]]) 
new=np.linalg.det(a1)
print(new)"""


# Line linalg.eig
"""import numpy as np
a1=np.array([[10,20,30],
             [40,50,60],
             [40,50,90]])
eigen_value=np.linalg.eig(a1)
print(eigen_value)"""   

# np.shuffle: it change the array 's elemnts position but elements are same:
