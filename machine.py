import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

data={ "X_hours_of_study":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "Y_the_score":[50, 55, 60, 65, 70, 75, 80, 85, 90, 95]}
md=pd.DataFrame(data)
print(md)

md.describe()

viz=md[["X_hours_of_study", "Y_the_score"]]
viz.hist()
plt.show

plt.scatter(md.X_hours_of_study, md.Y_the_score, color= 'orange')
plt.xlabel("hours of study")
plt.ylabel("the score")
plt.show

msk= np.random.rand(len(md))<0.4
train=md[msk]
test=md[~msk]
print(train)
print(test)

from sklearn import linear_model
regr= linear_model.LinearRegression()
train_x= np.asanyarray(train[['X_hours_of_study']])
train_y= np.asanyarray(train[['Y_the_score']])
regr.fit(train_x, train_y)
print(regr)
print('Cofficients:', regr.coef_) #تتا 0
print('Intercept:', regr.intercept_)#تتا 1

plt.scatter(train.X_hours_of_study, train.Y_the_score, color='blue')
plt.plot(train_x, regr.coef_[0][0]*train_x+regr.intercept_[0], '-r')
plt.xlabel('hours of study')
plt.ylabel('the score')

from sklearn.metrics import r2_score
test_x = np.asanyarray(test[['X_hours_of_study']])
test_y = np.asanyarray(test[['Y_the_score']])
test_y_ = regr.predict(test_x)
print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y)**2))
print("R2-score: %.2f" % r2_score(test_y, test_y_))
