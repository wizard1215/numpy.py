# Logical function are return the result in the True False form:
# (1) np.logical_and : Two condition are true together ata a time:
"""import numpy as np
a1=np.array([10,67,90,20,30,60,70,65])
result=np.logical_and(a1>20,a1<60)
print(result)"""

"""import numpy as np
a1=np.array([[10,67,90],
             [40,70,65]])
result=np.logical_and(a1>20,a1<60)
print(result)"""


# np.logical_or:if anyone conditions are True then return True:otherwise return false:
"""import numpy as np
a1=np.array([10,67,90,20,30,60,70,65])
result=np.logical_or(a1>20,a1<60)
print(result)"""

"""import numpy as np
a1=np.array([[10,67,90],
             [40,70,65]])
result=np.logical_and(a1>20,a1<60)
print(result)"""

# np.logical_not: It reverse the conditon If( True)then False: ,if (False) then True:
"""import numpy as np
a1=np.array([10,67,90,20,30,60,70,65])
result=np.logical_not(a1>=30)
print(result)"""

"""import numpy as np
a1=np.array([[10,67,90],
             [40,70,65]])
result=np.logical_not(a1>20)
print(result)"""


# np.xor--if a condition are true and another conditon is false Then it return True:

"""import numpy as np
a1=np.array([10,67,90,20,30,60,70,65])
result=np.logical_and(a1>20,a1<60)
print(result)"""

"""import numpy as np
a1=np.array([[10,67,90],
             [40,70,65]])
result=np.logical_and(a1>20,a1<60)
print(result)"""

# np.all--it check that in array all conditons are same:
"""import numpy as np
a1=np.array([45,44,46,22,30,59,34,56])
result=np.all((a1>20) & (a1<60))
print(result)"""

# with or
"""import numpy as np
a1=np.array([[45,44,46,22]
            [30,59,34,56]])
result=np.all((a1>20) | (a1<60))
print(result)"""

# np.any-- IT check that in a array there are any condtions are true or not:
# suppose we check that any  students is fail:
"""import numpy as np
students=np.array(["pass","pass","fail","pass","pass","pass"])
result=np.any(students=="fail")
print(result) """


# we check that here the tempreature are greater then 40"c anyday:
"""import numpy as np
tempreature=np.array([30,26,40,23,27,28,32])
result=np.any(tempreature>40)
print(result)"""

# if we check that anyday product sales are 0:
"""import numpy as np
product_sales=np.any([10,20,100,0,3000,400,90,500])
result=np.any(product_sales>=0)
print(result)"""


# np.where --it is return the result bases on the conditions and return the indices of the result:
"""import numpy as np
a = np.array([10, 20, 30, 40, 50])
result = np.where(a > 25)
print(result)"""

#It is follow to Replacing conditons:
"""import numpy as np
Tempreature=np.array([30,26,42,23,27,28,32])
check=np.where(Tempreature>40,"HOt",'Cold')
print(check)"""

"""import numpy as np
numbers=np.array([10,20,30,3,19,35,14,18,19,90])
check=np.where(numbers>20,"Big","small")
print(check)"""

# students result check:
"""import numpy as np
students_marks=np.array([10,40,37,90,67,56,45,28,53])
result_check=np.where(students_marks>33,"Pass","Fail")
print(result_check)"""
