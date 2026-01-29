import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split


data = pd.read_csv("weight and height.csv")

X = data[["Height"]].values
Y = data[["Weight"]].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, shuffle=True, test_size = 0.2)

print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)

fig, (ax1, ax2) = plt.subplots(1, 2)

w = np.random.randn(1, 1)
b = np.random.randn(1, 1)
learning_rate_w = 0.000001
learning_rate_b = 0.01

losses = []
epochs = 80

for j in range(epochs):
    for i in range(X_train.shape[0]):
        x = X_train[i]
        y = Y_train[i]
        y_pred = x * w + b
        error = y - y_pred

        # SGD
        w = w + (error * x * learning_rate_w)
        b = b + (error * learning_rate_b)


        # mae
        loss = np.mean(np.abs(error))
        losses.append(loss)

        Y_pred = X_train * w + b


print(error)
print(loss)

ax1.scatter(X_train, Y_train, color="b")
ax1.plot(X_train, Y_pred, color="r")

# set limitation for better reviewing last losses
# ax2.set_xlim(315000, 325000)
# ax2.set_ylim(0, 15)

ax2.plot(losses)
plt.show()
