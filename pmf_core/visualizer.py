# pmf_core/visualizer.py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_g_matrix(G, factor_names=None):
    fig, ax = plt.subplots(figsize=(10, 4))
    for i in range(G.shape[1]):
        ax.plot(G[:, i], label=factor_names[i] if factor_names else f"因子 {i+1}")
    ax.set_title("G 矩阵（源贡献）")
    ax.set_xlabel("样本序号")
    ax.set_ylabel("贡献值")
    ax.legend()
    return fig

def plot_f_matrix(F, species_names=None, factor_names=None):
    fig, axs = plt.subplots(F.shape[0], 1, figsize=(10, 3 * F.shape[0]))
    for i, row in enumerate(F):
        ax = axs[i] if F.shape[0] > 1 else axs
        ax.bar(species_names if species_names else np.arange(len(row)), row, color='skyblue')
        ax.set_title(factor_names[i] if factor_names else f"因子 {i+1}")
        ax.set_ylabel("成分比例")
        ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    return fig