import numpy as np

# class LLS:
#     def __init__(self, x_train, y_train):
#         self.x = np.array(x_train).reshape(-1, 1)
#         self.y = np.array(y_train).reshape(-1, 1)
#         self.w = None
#
#     def fit(self):
#         self.w = np.linalg.inv(self.x.T @ self.x) @ self.x.T @ self.y
#         return self.w
#
#     def predict(self, new_data):
#         y_pred = new_data * self.w
#         return y_pred


class LLS:
    def __init__(self):
        self.w = None

    def fit(self, x, y):
        self.w = np.linalg.inv(x.T @ x) @ x.T @ y
        return self.w

    def predict(self, new_data):
        y_pred = new_data * self.w
        return y_pred

    def evaluate(self, x_test, y_test, metric):
        y_pred = self.predict(x_test)

        if metric == 'mse':
            loss = np.sum((y_pred - y_test)**2) / len(y_test)
        elif metric == 'mae':
            loss = np.sum(np.abs(y_pred - y_test)) / len(y_test)
        else:
            raise "Please enter metric correctly"

        return loss