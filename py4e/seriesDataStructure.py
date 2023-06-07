import pandas as pd
import numpy as np
#you can create a series by passing in a list of values
#Pandas adds automatically an index starting with zero
students=['Alice','Jack','Molly']
#now we call the series function in pandas and pass the students
print(pd.Series(students))
#pandas identified automatically the type of data as "objects"
numbers=[1,2,3]
print(pd.Series(numbers))
#if we have a None type, pandas inserts it as a None and uses the type object for the array
students=['Alice','Jack',None]
print(pd.Series(students))
#if we use None in a list of numbers integers or float,
#it uses the value NaN that means "Not a Number"
numbers=[1,2,None]
print(pd.Series(numbers))
#NaN is not equivalent a None
#instead of using an equality, you need to use a function of numpy library isnan()
print(np.isnan(pd.Series(numbers)))
#a series can be created directly from a dictionary and the index will automatic assigned to the keys
students_score={'Alice':'Physics',
                'Jack':'Chemistry',
                'Molly':'English'}
s=pd.Series(students_score)
print(s)
#once the series has been created, we can get the index object using the index attribute
print(s.index)
#the dtype of object is for arbitrary objects
students=[("Alice","Brown"),("Jack","White"),("Molly","Green")]
print(pd.Series(students))
#you can also separate your index creation by passing the index as a list explicity
s = pd.Series(['Physics','Chemistry','English'], index=['Alice','Jack','Molly'])
print(s)
#if the index is not found in the keys of your dictionary, pandas will add it with None or Nan
s=pd.Series(students_score,index=['Alice','Molly','Sam'])
print(s)