import pandas as pd

# Load your dataset from the specified path
df = pd.read_csv(r'C:\Users\admin\Desktop\DSBDA\Dataset.csv')

df = df.drop_duplicates()


print(df)

#data integration
df1=df.head(2)
print(df1)

df2=df.tail(2)
print(df2)

df.isnull()
df.isna().any()
df.isna().sum()
#integrating data by applying union and intersection
union_df = pd.concat([df1, df2], ignore_index=True)
intersection_df = pd.merge(df1, df2, how='inner')
print("Union:")
print(union_df)

print("Intersection:")
print(intersection_df)


#data transformation
import pandas as pd

# Create a sample DataFrame
data = {'product': ['Product A', 'Product B', 'Product C'],
        'price_inr': [100, 150, 200]}

df = pd.DataFrame(data)

# Define the exchange rate (1 INR to USD)
exchange_rate = 0.014  # 1 INR = 0.014 USD

# Perform the data transformation
df['price_usd'] = df['price_inr'] * exchange_rate

# Print the transformed DataFrame
print(df)

#error correcting

# Create a sample DataFrame
data = {'product': ['Product A', 'Product B', 'Product C', 'Product D'],
        'price_inr': [100, 150, 200, 10000]}

df = pd.DataFrame(data)

# Define a valid price range in INR
min_valid_price_inr = 50
max_valid_price_inr = 1000

# Filter out rows with prices outside the valid range
filtered_df = df[(df['price_inr'] >= min_valid_price_inr) & (df['price_inr'] <= max_valid_price_inr)]

# Print the filtered DataFrame
print(filtered_df)

# model building
