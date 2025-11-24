import pandas as pd
from scipy.stats import kurtosis
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("student_scores.csv")
score_columns = df.columns[1:]


kurt_values = [kurtosis(df[col], bias=False) for col in score_columns]


for col, val in zip(score_columns, kurt_values):
    print(f"Kurtosis of {col}: {val:.4f}")


plt.figure(figsize=(8, 5))
sns.barplot(x=score_columns, y=kurt_values, palette="crest")
plt.xticks(rotation=45)
plt.title("Kurtosis of Each Subject")
plt.ylabel("Kurtosis Value")
plt.axhline(0, color="#A93386", linestyle='--')
plt.show()

