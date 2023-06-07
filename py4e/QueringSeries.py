#a panda series can be queried by the index position or index label
#if you don't give an index to the series, the position and the label will be the same
#to query by numeric location, starting at 0 use the iloc attribute
#to query by index label you can use the loc attribute
import pandas as pd
student_classes={'Alice':'Physics',
                 'Jack':'Chemistry',
                 'Molly':'English',
                 'Sam':'History'}
s=pd.Series(student_classes)
print(s)
#we use iloc by position
print(s.iloc[3])
#we use loc by label
print(s.loc['Molly'])
#if you pass it via integer parameter, it will behave as query via iloc attribute
print(s[3])
#if you pass an object, it will query as label based loc attribute
print(s['Molly'])

grades=pd.Series([90,80,70,60])
total=0
for grade in grades:
    total+=grade
print(total/len(grades))

#we can write the same code using the numpy sum method
import numpy as np
total=np.sum(grades)
print(total/len(grades))
#the last one is faster and simplify, its called vectorization
#creating a series of random numbers
numbers=pd.Series(np.random.randint(0,1000,10000))
print(numbers.head())#it prints the first 5 values
#to prove and run many times a code we can use timeit
#%%timeit -n 100#it is 1000 for default
#total=np.sum(numbers)
#print(total/len(numbers))

#broadcasting, with it you can apply an operation to every value in the series
numbers+=2#this way is faster
print(numbers.head())
#it is the same as doing iterable
for label, value in numbers.items():
    numbers._set_value(label,value+2)
print(numbers.head())
#the .loc attribute also can add a new element in the series, if the value in the index doesnt exist
s=pd.Series([1,2,3])
s.loc['History']=120
print(s)

student_classes=pd.Series({'Alice':'Physics',
                 'Jack':'Chemistry',
                 'Molly':'English',
                 'Sam':'History'})
#we can add some repetitive indexes
kelly_classes=pd.Series(['Philosophy','Arts','Math'], index=['Kelly','Kelly','Kelly'])
print(kelly_classes)
#finally we can append all of the data to the series
#.append returns a new series and doesnt change the original series
all_students_classes=student_classes.append(kelly_classes)#we can use .concat instead
print(all_students_classes)

#if we use .loc('Kelly') we will have a list of the values