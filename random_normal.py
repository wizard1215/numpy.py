# This function gie the random numbers using three terms:
#(1)center: The numbers which around
#(2)spread: How much numbers is spread
#(3)size : How many nuumbers are need:

"""import numpy as np
array=np.random.normal(10,4,(2,2))
print(array)"""


# if you  Genreate 1000 sales record:with around 1000 spread 200:
"""import numpy as np
sales = np.random.normal(1000, 200, 1000)
print(sales)"""


# Employees salary : suppose
"""Average salary = ₹50,000
Std deviation = ₹8,000
salary = np.random.normal(50000, 8000, 500)
print(salary)"""



# np.random.uniform:This function is giving the random numbers:
# but all numbers have eqally chance to arriving:like Ludio dice:
"""import numpy as np
dice=np.random.uniform(1,7,7)
print(dice)""" # Each value blw 1 to 7 : with qually probablity:

# If we create 2d array then :like coin having only two probablity:
#suppose That

"""import numpy as np
coin=np.random.uniform(0,1)
if coin >0.5:
    print("Head")
else:
    print("Tail")"""



# np.random.seed: it use to fixed random numbers:
#so that output is not change running time:as

"""import numpy as np
rand_num=np.random.randint(2,50,10)
print(rand_num)""" # This code give the diffrent numbers at every running time:
 
# Now
"""import numpy as np
numbers=np.random.seed(50)
rand_num=np.random.randint(2,50,10)
print(rand_num)""" # now it code give genreate the same numbers at every running time:

# if Genreate array
"""import numpy as np
array1=np.random.seed(20)
array=np.random.randint(2,20,(3,4))
print(array)"""

# np.random.choice :
"""import numpy as np
numbers=np.random.choice([10,20,30,40,50],4)
print(numbers) """# any 4 elements are outcome:


"""import numpy as np
coin_Toss=np.random.choice(["Head","Tail"],1)
print(coin_Toss)"""

"""import numpy as np
Ludio_Dice=np.random.choice([1,2,3,4,5,6],1)
print(Ludio_Dice)"""

"""import numpy as np
numbers=np.random.choice([2,4,5,6,7,6],7)
print(numbers)""" # elements < given numbers then by default use replace=True:
# Then it use any elements two time:
# BUT IS WE use the replace =False hen occured error:

"""import numpy as np
numbers=np.random.choice([2,4,5,6,7,6],7,replace=False)
print(numbers)"""

# susppose we want to select randomley 2 customers:
"""import numpy as np
customers=np.random.choice(["Ritik","Ravi","Pari","Shiv","Jiya","Aashu"],2)
print(customers)"""

# Employee Audit

# suppose select randomley  10  employees for audit upon 100 employees then:
"""import numpy as np
employees = np.arange(1,101)
audit_sample = np.random.choice(employees, 10, replace=False) # so same employee not audicts:"""

"""import numpy as np
a1=np.array([1,2,3])
a2=np.array([4,5,6])
new_array=np.dot(a1,a2)
print(new_array)"""



