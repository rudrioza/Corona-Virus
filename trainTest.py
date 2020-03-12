import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


x = []
y = []

count = 0
newDeathPercentage = 0


with open('deathData.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if(count != 0 and row != []):
            x.append(count)
            newDeathPercentage = (int(row[1]))
            y.append(newDeathPercentage)
        count = count + 1

#reversing the features because latest data should appear last

y.reverse()




regression_model = LinearRegression()

trainingSetX = []
trainingSetY = []
testSetX = []

trainingLength = int(len(x))



for i in range(trainingLength):
    trainingSetX.append([x[i]])
trainingSetX = np.asarray(trainingSetX)


for i in range(trainingLength):
    trainingSetY.append([y[i]])
trainingSetY = np.asarray(trainingSetY)

for i in range(len(x) - trainingLength):
    testSetX.append([x[trainingLength + i]])
testSetX = np.asarray(testSetX)

regression_model.fit(trainingSetX, trainingSetY)

y_predicted = regression_model.predict(trainingSetX)



# model evaluation
rmse = mean_squared_error(trainingSetY, y_predicted)
r2 = r2_score(trainingSetY, y_predicted)
print("rmse",rmse)
print("r2", r2)

# data points
plt.scatter(trainingSetX, trainingSetY, s=10)
plt.xlabel('Time')
plt.ylabel('Total Deaths')


# predicted values
plt.title('Predicting Deaths')
plt.plot(trainingSetX, y_predicted, color='r')
plt.show()




