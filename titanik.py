import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')
print(df.head()) # Посмотри на первые 5 строк
df = df.drop(columns=['deck'])
df['age'] = df['age'].fillna(df['age'].median())
df.groupby('sex')['survived'].mean()
df.groupby('class')['survived'].mean()
# Если сумма родственников > 0, значит не один
df['is_alone'] = (df['sibsp'] + df['parch'] == 0).astype(int)
print(df.groupby('sex')['survived'].mean())
print(df.groupby('class')['survived'].mean())