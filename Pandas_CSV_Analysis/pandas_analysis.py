import pandas as pd

# Read CSV file
df = pd.read_csv("data/students.csv")

print("Data loaded successfully")

# Inspect Data
print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataset Info:")
df.info()

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

print("\nMean Marks:", df['Marks'].mean())
print("Median Marks:", df['Marks'].median())
print("Minimum Marks:", df['Marks'].min())
print("Maximum Marks:", df['Marks'].max())
print("Total Students:", df['Marks'].count())

# Filter Students with Marks > 80
high_scorers = df[df['Marks'] > 80]
print("\nStudents with Marks > 80:")
print(high_scorers)

# CS Department Students
cs_students = df[df['Department'] == 'CS']
print("\nCS Department Students:")
print(cs_students)

# Select specific columns
selected_columns = df[['Name', 'Department', 'Marks']]
print("\nSelected Columns:")
print(selected_columns)

# First 3 students
print("\nFirst 3 Students:")
print(df.iloc[:3])

# Save output to CSV
high_scorers.to_csv("output/high_scorers.csv", index=False)
cs_students.to_csv("output/cs_students.csv", index=False)

print("\nFiltered files saved successfully!")
