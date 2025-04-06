# pmf_core/residuals.py
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def compute_residuals(X, G, F, U):
    X_hat = G @ F
    R = (X - X_hat) / U
    return R

def plot_residual_histogram(R):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(R.flatten(), bins=100, color="skyblue", edgecolor="black")
    ax.set_title("残差分布直方图")
    ax.set_xlabel("残差值")
    ax.set_ylabel("频数")
    return fig

def plot_q_trend(q_values):
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(range(1, len(q_values)+1), q_values, marker='o')
    ax.set_title("Q 值收敛趋势")
    ax.set_xlabel("迭代次数")
    ax.set_ylabel("Q 值")
    return fig