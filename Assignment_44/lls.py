import numpy as np

class LLS:
    def __init__(self, x_train, y_train):
        self.x = np.array(x_train).reshape(-1, 1)
        self.y = np.array(y_train).reshape(-1, 1)
        self.w = None

    def fit(self):
        self.w = np.matmul(np.matmul(np.linalg.inv(np.matmul(self.x.T, self.x)), self.x.T), self.y)
        return self.w

    def predict(self, new_data):
        y_pred = new_data * self.w
        return y_pred