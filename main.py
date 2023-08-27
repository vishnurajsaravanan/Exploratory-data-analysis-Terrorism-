import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('globalterrorismdb_0718dist.csv', encoding='ISO-8859-1')

print(data.info())
print(data.head())
print(data.describe())

plt.figure(figsize=(10, 6))
sns.countplot(x='attacktype1_txt', data=data, order=data['attacktype1_txt'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Distribution of Attack Types')
plt.show()

# Number of attacks over the years
plt.figure(figsize=(12, 6))
sns.countplot(x='iyear', data=data, palette='viridis')
plt.xticks(rotation=90)
plt.title('Number of Attacks Over the Years')
plt.show()

# Distribution of terrorist groups
plt.figure(figsize=(12, 6))
sns.barplot(y=data['gname'].value_counts()[:10].index, x=data['gname'].value_counts()[:10].values, orient='h', palette='viridis')
plt.title('Top 10 Terrorist Groups')
plt.show()

# Heatmap of correlations
corr_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()