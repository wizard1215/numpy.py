#The hstack is add row from right to left side :as
"""import numpy as np
a=np.array([10,20,30])
b=np.array([20,30,40])
print(np.hstack((a,b)))"""


"""import numpy as np
a=np.array([[12,13,14]])
b=np.array([[15,16,17]])
print(np.hstack((a,b)))"""


# if 2d array with multiple row:if row are not matched then occured error:
"""import numpy as np
a1=np.array([[1,2],
             [3,4]])
a2=np.array([[5,6],
             [7,8]])
print(np.hstack((a1,a2)))"""



# Based on axis:if axis is 1 then is work same as for normally as np.horizontally: import numpy as np
"""import numpy as np
a1=np.array([[1,2],
             [3,4]])
a2=np.array([[5,6],
             [7,8]])
new_array=a1,a2
print(np.concatenate (new_array,1))"""

#if axis is 0 then is work as it is convert row from array column as:
"""import numpy as np
a1=np.array([[1,2]])
a2=np.array([[5,6]])
             
new_array=a1,a2
print(np.concatenate (new_array , 0))"""


