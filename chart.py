import matplotlib.pyplot as plt

# Sample data for the charts
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [30, 50, 20, 60]

# Create a Bar Chart
plt.figure(figsize=(8, 6))
plt.bar(categories, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.show()

# Create a Line Chart
plt.figure(figsize=(8, 6))
plt.plot(categories, values, marker='o', linestyle='-', color='b')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Line Chart Example')
plt.show()

# Create a Pie Chart
plt.figure(figsize=(8, 6))
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart Example')
plt.show()
