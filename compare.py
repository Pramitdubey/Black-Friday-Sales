import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('BlackFriday.csv')

# Basic data exploration
print(data.info())
print(data.describe())

# Age distribution
plt.figure(figsize=(10, 6))
data['Age'].value_counts().sort_index().plot(kind='bar')
plt.title('Age Distribution')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.show()

# Gender distribution
plt.figure(figsize=(8, 6))
data['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Gender Distribution')
plt.show()

# Occupation distribution (top 10)
plt.figure(figsize=(12, 6))
data['Occupation'].value_counts().nlargest(10).plot(kind='bar')
plt.title('Top 10 Occupations')
plt.xlabel('Occupation')
plt.ylabel('Count')
plt.show()

# Average purchase amount by age group
plt.figure(figsize=(10, 6))
data.groupby('Age')['Purchase'].mean().plot(kind='bar')
plt.title('Average Purchase Amount by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Purchase Amount')
plt.show()

# Average purchase amount by gender
plt.figure(figsize=(8, 6))
data.groupby('Gender')['Purchase'].mean().plot(kind='bar')
plt.title('Average Purchase Amount by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Purchase Amount')
plt.show()

# Correlation between numerical variables
correlation_matrix = data[['Purchase', 'Product_Category_1', 'Product_Category_2', 'Product_Category_3']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Purchase amount distribution by city category
plt.figure(figsize=(10, 6))
sns.boxplot(x='City_Category', y='Purchase', data=data)
plt.title('Purchase Amount Distribution by City Category')
plt.show()

# Average purchase amount by marital status
plt.figure(figsize=(8, 6))
data.groupby('Marital_Status')['Purchase'].mean().plot(kind='bar')
plt.title('Average Purchase Amount by Marital Status')
plt.xlabel('Marital Status (0: Unmarried, 1: Married)')
plt.ylabel('Average Purchase Amount')
plt.show()

# Product category 1 distribution
plt.figure(figsize=(10, 6))
data['Product_Category_1'].value_counts().sort_index().plot(kind='bar')
plt.title('Product Category 1 Distribution')
plt.xlabel('Product Category 1')
plt.ylabel('Count')
plt.show()

# Average purchase amount by years in current city
plt.figure(figsize=(10, 6))
data.groupby('Stay_In_Current_City_Years')['Purchase'].mean().plot(kind='bar')
plt.title('Average Purchase Amount by Years in Current City')
plt.xlabel('Years in Current City')
plt.ylabel('Average Purchase Amount')
plt.show()

# 1. Product Category 1 distribution (Pie Chart)
plt.figure(figsize=(10, 8))
data['Product_Category_1'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Product Category 1 Distribution')
plt.ylabel('')
plt.show()

# 2. City Category distribution (Bar Chart)
plt.figure(figsize=(8, 6))
data['City_Category'].value_counts().plot(kind='bar')
plt.title('City Category Distribution')
plt.xlabel('City Category')
plt.ylabel('Count')
plt.show()

# 3. Stay In Current City Years distribution (Pie Chart)
plt.figure(figsize=(10, 8))
data['Stay_In_Current_City_Years'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Stay In Current City Years Distribution')
plt.ylabel('')
plt.show()

# 4. Marital Status distribution (Bar Chart)
plt.figure(figsize=(8, 6))
data['Marital_Status'].value_counts().plot(kind='bar')
plt.title('Marital Status Distribution')
plt.xlabel('Marital Status (0: Unmarried, 1: Married)')
plt.ylabel('Count')
plt.show()

# 5. Average Purchase Amount by Product Category 1 (Bar Chart)
plt.figure(figsize=(12, 6))
data.groupby('Product_Category_1')['Purchase'].mean().sort_values(ascending=False).plot(kind='bar')
plt.title('Average Purchase Amount by Product Category 1')
plt.xlabel('Product Category 1')
plt.ylabel('Average Purchase Amount')
plt.show()

# 6. Gender distribution by Age Group (Stacked Bar Chart)
gender_age = pd.crosstab(data['Age'], data['Gender'], normalize='index')
gender_age.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Gender Distribution by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Proportion')
plt.legend(title='Gender')
plt.show()

# 7. Occupation distribution by Gender (Stacked Bar Chart)
occupation_gender = pd.crosstab(data['Occupation'], data['Gender'], normalize='index')
occupation_gender.plot(kind='bar', stacked=True, figsize=(14, 8))
plt.title('Gender Distribution by Occupation')
plt.xlabel('Occupation')
plt.ylabel('Proportion')
plt.legend(title='Gender')
plt.xticks(rotation=90)
plt.show()

# 8. Average Purchase Amount by City Category and Gender (Grouped Bar Chart)
city_gender_purchase = data.groupby(['City_Category', 'Gender'])['Purchase'].mean().unstack()
city_gender_purchase.plot(kind='bar', figsize=(10, 6))
plt.title('Average Purchase Amount by City Category and Gender')
plt.xlabel('City Category')
plt.ylabel('Average Purchase Amount')
plt.legend(title='Gender')
plt.show()

# 9. Product Category 1 distribution by Age Group (Stacked Bar Chart)
product_age = pd.crosstab(data['Age'], data['Product_Category_1'], normalize='index')
product_age.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.title('Product Category 1 Distribution by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Proportion')
plt.legend(title='Product Category 1', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# 10. Average Purchase Amount by Marital Status and Gender (Grouped Bar Chart)
marital_gender_purchase = data.groupby(['Marital_Status', 'Gender'])['Purchase'].mean().unstack()
marital_gender_purchase.plot(kind='bar', figsize=(10, 6))
plt.title('Average Purchase Amount by Marital Status and Gender')
plt.xlabel('Marital Status (0: Unmarried, 1: Married)')
plt.ylabel('Average Purchase Amount')
plt.legend(title='Gender')
plt.show()
