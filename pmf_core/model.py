# pmf_core/model.py
import numpy as np

class PMF:
    def __init__(self, X, U, n_factors=4, max_iter=500, tol=1e-4, random_state=0):
        np.random.seed(random_state)
        self.X = X
        self.U = U
        self.k = n_factors
        self.max_iter = max_iter
        self.tol = tol
        self.n_samples, self.n_features = X.shape
        self.G = np.abs(np.random.rand(self.n_samples, self.k))
        self.F = np.abs(np.random.rand(self.k, self.n_features))
        self.q_values = []

    def fit(self):
        prev_q = np.inf
        for iteration in range(self.max_iter):
            # 更新 G
            for i in range(self.n_samples):
                A = self.F @ self.F.T
                B = self.F @ self.X[i, :].T
                self.G[i, :] = np.linalg.lstsq(A + 1e-8 * np.eye(self.k), B, rcond=None)[0]
                self.G[i, :] = np.clip(self.G[i, :], 0, None)

            # 更新 F
            for j in range(self.n_features):
                A = self.G.T @ self.G
                B = self.G.T @ self.X[:, j]
                self.F[:, j] = np.linalg.lstsq(A + 1e-8 * np.eye(self.k), B, rcond=None)[0]
                self.F[:, j] = np.clip(self.F[:, j], 0, None)

            # 计算 Q 值
            X_hat = self.G @ self.F
            Q = np.sum(((self.X - X_hat) / self.U) ** 2)
            self.q_values.append(Q)

            if np.abs(prev_q - Q) < self.tol:
                break
            prev_q = Q

        return self.G, self.F, self.q_values[-1]

    def get_q_trend(self):
        return self.q_values