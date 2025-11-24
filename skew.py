import pandas as pd
from scipy.stats import skew
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("student_scores.csv")
print(df)

score_columns = df.columns[1:]


for col in score_columns:
    skew_value = skew(df[col], bias=False)
    print(f"Skewness of {col}: {skew_value:.4f}")


plt.figure(figsize=(18, 10))
for i, col in enumerate(score_columns):
    plt.subplot(3, 3, i + 1)
    sns.histplot(df[col], kde=True, bins=10, color="#B5618E")
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
