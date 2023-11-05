import pandas as pd 
data = {"Roll-num": [10,20,30,40,50,60,70], "Age":[12,14,13,12,14,13,15], 
"NAME":['John','Camili','Rheana','Joseph','Amanti','Alexa','Siri']}
block = pd.DataFrame(data)
print("Original Data frame:\n",block)

#Create a subset of a Python dataframe using the loc() function
block.loc[[0,1,3]]
#Example 2: Create a subset of rows using slicing
block.loc[0:3]

#shape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
#creating subsets and concat
df2 = arr[:25]
df3 = arr[25:]
print(df2)
print(df3)
#merge
df2 = df.iloc[:,:3]
df3 = arr.iloc[:,2:]
df7 = df2.merge(df3, on=['Marketing Spend'],how='inner')
#sort
x = df.sort_values(by = ['Marketing Spend'],ascending=True) 
#transpose
x = df.T
