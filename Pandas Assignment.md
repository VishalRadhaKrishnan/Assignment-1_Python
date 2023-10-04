# PandasAssignment

Q1. How do you load a CSV file into a Pandas DataFrame?
    ou can load a CSV (Comma-Separated Values) file into a Pandas DataFrame using the read_csv() function provided by the Pandas library in Python. 
            *** import pandas as pd
            *** df = pd.read_csv('your_file.csv')
            *** df = pd.read_csv('your_file.csv', delimiter=';', header=None, usecols=[0, 1, 3], dtype={'Column3': float}, skiprows=2)


Q2. How do you check the data type of a column in a Pandas DataFrame?
To check the data type of a column in a Pandas DataFrame, you can use the dtype attribute or the dtypes attribute.
*** column_data_type = df['column_name'].dtype
    print(column_data_type)

*** column_data_types = df.dtypes
    print(column_data_types)

Q3. How do you select rows from a Pandas DataFrame based on a condition?

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45]}
df = pd.DataFrame(data)

condition = df['Age'] > 30
selected_rows = df[condition]
print(selected_rows)

Q4. How do you rename columns in a Pandas DataFrame?
You can rename columns in a Pandas DataFrame using the rename() method or by directly assigning new column names to the columns attribute.
Using the rename() method:

import pandas as pd
# Create a sample DataFrame
data = {'Old_Name1': [1, 2, 3],
        'Old_Name2': [4, 5, 6]}
df = pd.DataFrame(data)
# Rename columns using the rename() method
df.rename(columns={'Old_Name1': 'New_Name1', 'Old_Name2': 'New_Name2'}, inplace=True)
# The 'inplace=True' parameter modifies the DataFrame in place; you can omit it to create a new DataFrame with the updated column names

Q5. How do you drop columns in a Pandas DataFrame?
You can drop columns from a Pandas DataFrame using the drop() method or by selecting the columns you want to keep.

import pandas as pd
# Create a sample DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}
df = pd.DataFrame(data)
# Drop one or more columns using the drop() method
columns_to_drop = ['B', 'C']
df.dropped(columns=columns_to_drop, inplace=True)

Q6. How do you find the unique values in a column of a Pandas DataFrame?
To find the unique values in a column of a Pandas DataFrame, you can use the unique() method.
unique_values = df['Column_Name'].unique()

Q7. How do you find the number of missing values in each column of a Pandas DataFrame?
To find the number of missing (null or NaN) values in each column of a Pandas DataFrame, you can use the isna() or isnull() method in combination with the sum() method.

# Using the isna() method to identify missing values and sum() to count them
missing_values = df.isna().sum()
# Alternatively, you can use isnull() method, which is equivalent to isna()
# missing_values = df.isnull().sum()
# Print or access the count of missing values for each column
print(missing_values)

Q8. How do you fill missing values in a Pandas DataFrame with a specific value?
You can fill missing (NaN or null) values in a Pandas DataFrame with a specific value using the fillna() method.

**** df.fillna(value_to_fill, inplace=True)

Q9. How do you concatenate two Pandas DataFrames?
You can concatenate (combine) two Pandas DataFrames along rows or columns using the concat() function from the Pandas library. The concat() function allows you to stack DataFrames either vertically (along rows) or horizontally (along columns).

Concatenate along rows (vertically):
concatenated_df = pd.concat([df1, df2], axis=0, ignore_index=True)

Concatenate along columns (horizontally):
concatenated_df = pd.concat([df1, df2], axis=1)


Q10. How do you merge two Pandas DataFrames on a specific column?
You can merge two Pandas DataFrames on a specific column using the merge() function. The merge() function allows you to combine DataFrames by specifying one or more columns as the merging keys.
merged_df = pd.merge(df1, df2, on='key_column', how='inner')

Q11. How do you group data in a Pandas DataFrame by a specific column and apply an aggregation function?
You can group data in a Pandas DataFrame by a specific column and apply an aggregation function using the groupby() method in combination with various aggregation functions like sum(), mean(), max(), min(), and more.

grouped = df.groupby('group_column')
result = grouped['value_column'].sum()

Q12. How do you pivot a Pandas DataFrame?
ou can pivot a Pandas DataFrame using the pivot() method or the pivot_table() method. Pivoting is a way to reshape your DataFrame by changing the structure of the data, typically by transforming columns into rows or vice versa.

data = {'Date': ['2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
        'Metric': ['A', 'B', 'A', 'B'],
        'Value': [10, 20, 15, 25]}
df = pd.DataFrame(data)
# Pivot the DataFrame
pivot_df = df.pivot(index='Date', columns='Metric', values='Value')
print(pivot_df)

Q13. How do you change the data type of a column in a Pandas DataFrame?
You can change the data type of a column in a Pandas DataFrame using the astype() method or by directly assigning new values with the desired data type to the column. 
df['column_name'] = df['column_name'].astype(int)

Q14. How do you sort a Pandas DataFrame by a specific column?
You can sort a Pandas DataFrame by a specific column using the sort_values() method. 
sorted_df = df.sort_values(by='column_name', ascending=True)
by: The name of the column by which you want to sort the DataFrame.
ascending: Set it to True for ascending order or False for descending order.

Q15. How do you create a copy of a Pandas DataFrame?
To create a copy of a Pandas DataFrame, you can use the copy() method or directly assign the DataFrame to a new variable.
df_copy = df.copy()

Q16. How do you filter rows of a Pandas DataFrame by multiple conditions?
You can filter rows of a Pandas DataFrame by multiple conditions using logical operators such as & (for "and") and | (for "or") to combine conditions.
import pandas as pd
# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45],
        'Score': [85, 92, 78, 88, 95]}
df = pd.DataFrame(data)
# Define the conditions
condition = (df['Age'] > 30) & (df['Score'] >= 90)
# Filter rows based on the conditions
filtered_df = df[condition]
print(filtered_df)

Q17. How do you calculate the mean of a column in a Pandas DataFrame?
To calculate the mean (average) of a column in a Pandas DataFrame, you can use the mean() method on the specific column.
column_mean = df['column_name'].mean()

Q18. How do you calculate the standard deviation of a column in a Pandas DataFrame?
To calculate the standard deviation of a column in a Pandas DataFrame, you can use the std() method on the specific column.
column_std = df['column_name'].std()

Q19. How do you calculate the correlation between two columns in a Pandas DataFrame?
You can calculate the correlation between two columns in a Pandas DataFrame using the corr() method.
correlation = df['column_A'].corr(df['column_B'])

Q20. How do you select specific columns in a DataFrame using their labels?
You can select specific columns in a Pandas DataFrame using their labels by indexing the DataFrame with a list of column labels.
selected_columns = df[['column_label_1', 'column_label_2', ...]]

Q21. How do you select specific rows in a DataFrame using their indexes?
You can select specific rows in a Pandas DataFrame using their indexes by using the .loc[] indexer.
selected_rows = df.loc[[1, 3, 4]]

Q22. How do you sort a DataFrame by a specific column?
You can sort a Pandas DataFrame by a specific column using the sort_values() method. This method allows you to specify the column by which you want to sort the DataFrame. 
sorted_df = df.sort_values(by='column_name', ascending=True)

Q23. How do you create a new column in a DataFrame based on the values of another column?
You can create a new column in a Pandas DataFrame based on the values of another column by simply assigning values or applying a function to the new column.
df['new_column'] = df['existing_column'] * 2

Q24. How do you remove duplicates from a DataFrame?
You can remove duplicates from a Pandas DataFrame using the drop_duplicates() method or by using the duplicated() method to identify duplicate rows and then filtering them out. 
df = df.drop_duplicates(keep='last')
df = df.drop_duplicates()

Q25. What is the difference between .loc and .iloc in Pandas?
.loc - customized index that we are providing.
.iloc - default system providing index number.