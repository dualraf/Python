#the DataFrame is conceptually a two-dimensional series object
#there is an index and multiple columns of content, each column has a label
#two-axes labeled array
import pandas as pd
record1=pd.Series({'Name':'Alice',
                   'Class':'Physics',
                   'Score': 85})
record2=pd.Series({'Name':'Jack',
                   'Class':'Chemistry',
                   'Score': 82})
record3=pd.Series({'Name':'Helen',
                   'Class':'Biology',
                   'Score': 90})
#the DataFrame object is index, we can pass in our individual items in an array
#and we can pass in our index values as a second arguments
df=pd.DataFrame([record1,record2,record3], index=['school1','school2','school3'])
print(df.head())#we can use .head() like in the Series
#we will se the index as the leftmost column and the header of the rows of data
#an alternative method is using a list of dictionaries, where each dictionary represents a row of data
students=[{'Name':'Alice',
           'Class':'Physics',
           'Score': 85},
          {'Name': 'Jack',
           'Class': 'Chemistry',
           'Score': 82},
          {'Name': 'Helen',
           'Class': 'Biology',
           'Score': 90}]
#and pass the list of dictionaries to the DataFrame
df=pd.DataFrame(students, index=['school1','school2','school1'])
print(df.head())
#similar to the series we can extract data using .loc and .iloc
print(df.loc['school2'])#the index is unique, it will return a Series
#if we use a single value with DataFrame lock, where is non-unique, multiple rows will be returned as a new DataFrame
print(df.loc['school1'])
#we can add multiple axes
print(df.loc['school1','Name'])
#if we want to select a single column
#we could transpose the matrix and change the rows into columns and columns into rows
#it is done with the .T attribute
print(df.T)
print(df.T.loc['Name'])
#in panda's DataFrame columns always have a name, so you can select it simplier
print(df['Name'])#it returns a Series object
#we can use also many labels in chain
print(df.loc['school1']['Name'])
#a different method
print(df.loc[:,['Name','Score']])
#: means that we want all the rows, and the list is the columns we want back
#we can drop a row of the DataFrame
print(df.drop('school1'))
#it made a copy of the DataFrame and dropped the rows, but the original didn't change
#Drop has 2 parameters, the 1st is called inplace, if its true it'll update the DataFrame, otherwise it'll make a copy
#the 2nd parameter is the axes, by default is 0 that means you would drop a row, if it's 1 you want to drop a column
copy_df=df.copy()
#lets drop the name column
copy_df.drop("Name",inplace=True, axis=1)
print(copy_df)
#there is a second way to drop a column
del copy_df['Class']
print(copy_df)
#adding a new column of data
df['ClassRanking']=None
print(df)
#############################################################
df = pd.read_csv('Admission_Predict.csv')
print(df.head())#pandas create a new index by default
#we can set a column as the index
df = pd.read_csv('Admission_Predict.csv', index_col=0)
print(df.head())
#we can change the name of the columns by rename
new_df=df.rename(columns={'GRE Score':'GRE Score', 'TOEFL Score':'TOEFL Score',
                   'University Rating':'University Rating',
                   'SOP': 'Statement of Purpose','LOR': 'Letter of Recommendation',
                   'CGPA':'CGPA', 'Research':'Research',
                   'Chance of Admit':'Chance of Admit'})
print(new_df.head())
#we notice that LOR didn't change
print(new_df.columns)
#that's because LOR has an empty space after
new_df=new_df.rename(columns={'LOR ': 'Letter of Recommendation'})
print(new_df.head())
# So that works well, but it's a bit fragile. What if that was a tab instead of a space? Or two spaces?
# Another way is to create some function that does the cleaning and then tell renamed to apply that function
# across all of the data. Python comes with a handy string function to strip white space called "strip()".
# When we pass this in to rename we pass the function as the mapper parameter, and then indicate whether the
# axis should be columns or index (row labels)
new_df=new_df.rename(mapper=str.strip, axis='columns')
# Let's take a look at results
print(new_df.head())
#we can change the columns in other way
cols = list(df.columns)
cols = [x.lower().strip() for x in cols]
df.columns=cols
print(df.head())#we see that the columns are in lower now
#############################################################################################################
# Boolean masks are created by applying operators directly to the pandas Series or DataFrame objects.
# For instance, in our graduate admission dataset, we might be interested in seeing only those students
# that have a chance higher than 0.7
admit_mask=df['chance of admit'] > 0.7
print(admit_mask)
# the .where() function on the original DataFrame.
print(df.where(admit_mask).head())
# The next step is, if we don't want the NaN data, we use the dropna() function
print(df.where(admit_mask).dropna().head())
# Despite being really handy, where() isn't actually used that often. Instead, the pandas devs
# created a shorthand syntax which combines where() and dropna(), doing both at once. And, in
# typical fashion, the just overloaded the indexing operator to do this!
print(df[df['chance of admit'] > 0.7].head())
print(df[df["gre score"]>320].head())
#to add more comparisons we can use "and" u "or", "&" u "|"
print((df['chance of admit'] > 0.7) & (df['chance of admit'] < 0.9))
# Another way to do this is to just get rid of the comparison operator completely, and instead
# use the built in functions which mimic this approach
print(df['chance of admit'].gt(0.7) & df['chance of admit'].lt(0.9))
#you can chain it too
print(df['chance of admit'].gt(0.7).lt(0.9))
#######################################
df = pd.read_csv("Admission_Predict.csv", index_col=0)
print(df.head())
#it we want to change the index
df['Serial Number'] = df.index
# Then we set the index to another column
df = df.set_index('Chance of Admit ')
print(df.head())
# We can get rid of the index completely by calling the function reset_index(). This promotes the
# index into a column and creates a default numbered index.
df = df.reset_index()
print(df.head())
# Let's import and see what the data looks like
df = pd.read_csv('census.csv')
print(df.head())
# Here we can run unique on the sum level of our current DataFrame
print(df['SUMLEV'].unique())
# We see that there are only two different values, 40 and 50
#let's get only 50
df=df[df['SUMLEV'] == 50]
print(df.head())
#we can recude the count of column that we want to see
columns_to_keep = ['STNAME','CTYNAME','BIRTHS2010','BIRTHS2011','BIRTHS2012','BIRTHS2013',
                   'BIRTHS2014','BIRTHS2015','POPESTIMATE2010','POPESTIMATE2011',
                   'POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']
df = df[columns_to_keep]
print(df.head())
#then we set the index by 2 columns
df = df.set_index(['STNAME', 'CTYNAME'])
print(df.head())
#if we want to use .loc, we must use 2 parameters because the index is complex
print(df.loc['Michigan', 'Washtenaw County'])
#we can compare many elements by adding tuples to the .loc attribute
# Therefore, in this case, we will have a list of two tuples, in each tuple, the first element is
# Michigan, and the second element is either Washtenaw County or Wayne County

print(df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ])

######################################################
df = pd.read_csv('class_grades.csv')
print(df.head(10))
# We can actually use the function .isnull() to create a boolean mask of the whole dataframe. This effectively
# broadcasts the isnull() function to every cell of data.
mask=df.isnull()
print(mask.head(10))
#we can drop a row where there is a missing data
print(df.dropna().head(10))
# So, if we wanted to fill all missing values with 0, we would use fillna
df.fillna(0, inplace=True)
print(df.head(10))#it modifies tha DataFrame

df = pd.read_csv("log.csv")
print(df.head(20))
# In Pandas we can sort either by index or by values. Here we'll just promote the time stamp to an index then
# sort on the index.
df = df.set_index('time')
df = df.sort_index()
print(df.head(20))
df = df.reset_index()
df = df.set_index(['time', 'user'])
print(df)
#Next up is the method parameter(). The two common fill values are ffill and bfill. ffill is for forward
#filling and it updates an na value for a particular cell with the value from the previous row. bfill is
#backward filling, which is the opposite of ffill. It fills the missing values with the next valid value.
#it must be sorted
df = df.fillna(method='ffill')
print(df.head())
#we can replace element of the DataFrame
df = pd.DataFrame({'A': [1, 1, 2, 3, 4],
                   'B': [3, 6, 3, 8, 9],
                   'C': ['a', 'b', 'c', 'd', 'e']})
print(df.replace(1, 100))
print(df.replace([1, 3], [100, 300]))

df = pd.read_csv("log.csv")
print(df.head(20))
# Here's my solution, first matching any number of characters then ending in .html
print(df.replace(to_replace=".*.html$", value="webpage", regex=True))
################
df=pd.read_csv("presidents.csv")
# And lets just take a look at some of the data
print(df.head())
# Here's one solution, we could make a copy of the President column
df["First"]=df['President']
# Then we can call replace() and just have a pattern that matches the last name and set it to an empty string
df["First"]=df["First"].replace("[ ].*", "", regex=True)
# Now let's take a look
print(df.head())
del(df["First"])
#we can change it in another way
def splitname(row):
    # The row is a single Series object which is a single row indexed by column values
    # Let's extract the firstname and create a new entry in the series
    row['First']=row['President'].split(" ")[0]
    # Let's do the same with the last word in the string
    row['Last']=row['President'].split(" ")[-1]
    # Now we just return the row and the pandas .apply() will take of merging them back into a DataFrame
    return row

# Now if we apply this to the dataframe indicating we want to apply it across columns
df=df.apply(splitname, axis='columns')
print(df.head())
del(df['First'])
del(df['Last'])

# Here's my solution, where we match three groups but only return two, the first and the last name
pattern="(^[\w]*)(?:.* )([\w]*$)"

# Now the extract function is built into the str attribute of the Series object, so we can call it
# using Series.str.extract(pattern)
print(df["President"].str.extract(pattern).head())
# So that looks pretty nice, other than the column names. But if we name the groups we get named columns out
pattern="(?P<First>^[\w]*)(?:.* )(?P<Last>[\w]*$)"

# Now call extract
names=df["President"].str.extract(pattern)
print(names)
# And we can just copy these into our main dataframe if we want to
df["First"]=names["First"]
df["Last"]=names["Last"]
print(df.head())
# Now lets move on to clean up that Born column. First, let's get rid of anything that isn't in the
# pattern of Month Day and Year.
df["Born"]=df["Born"].str.extract("([\w]{3} [\w]{1,2}, [\w]{4})")
print(df["Born"].head())
#So if I were building this out, I would actually
# update this column to the write data type as well
df["Born"]=pd.to_datetime(df["Born"])
print(df["Born"].head())

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj1 = pd.Series(sdata)
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj2 = pd.Series(sdata, index=states)
obj3 = pd.isnull(obj2)

print(obj2.iloc[0:3])

s1 = pd.Series({1: 'Alice', 2: 'Jack', 3: 'Molly'})
s2 = pd.Series({'Alice': 1, 'Jack': 2, 'Molly': 3})