import numpy as np
import pandas as pd
from scipy import stats

df = pd.read_csv("student_scores.csv")
print(df)


scores = df[['math_score', 'english_score', 'science_score','history_score','art_score' ,'programming_score']]


x1 = np.mean(scores)
print("mean of scores is:", x1)

print('----------')


x2 = np.median(scores, axis=0)
print('median of scores is', x2)

print('----------')


x3 = stats.mode(scores, axis=0, keepdims=True)
print('mode of scores is:', x3.mode[0])
print(x3.count[0])

print('----------')

x4=np.var(scores, axis=0)
print(x4)
print('----------')

x5=np.std(scores, axis=0)
print(x5)