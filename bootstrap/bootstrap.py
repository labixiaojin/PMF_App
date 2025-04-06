import numpy as np
import pandas as pd

def run_bootstrap(X, U, n_factors, n_bootstrap):
    """
    执行 Bootstrap 分析，返回 F 因子组成的均值与标准差。
    """
    all_F = []

    for i in range(n_bootstrap):
        # 生成有放回的样本索引
        indices = np.random.choice(X.shape[0], size=X.shape[0], replace=True)
        X_sampled = X[indices]
        U_sampled = U[indices]

        # 模拟拟合过程（后续我们会调用 PMF）
        F_fake = np.abs(np.random.randn(n_factors, X.shape[1]))  # 生成随机正值数据
        all_F.append(F_fake)

    # 汇总统计
    all_F = np.array(all_F)  # 形状：(n_bootstrap, n_factors, n_species)
    F_mean = np.mean(all_F, axis=0)
    F_std = np.std(all_F, axis=0)

    # 返回 DataFrame 格式，便于前端展示
    df_summary = pd.DataFrame()
    for i in range(n_factors):
        for j in range(X.shape[1]):
            df_summary.loc[j, f'因子{i+1}_均值'] = F_mean[i, j]
            df_summary.loc[j, f'因子{i+1}_标准差'] = F_std[i, j]

    return df_summary

def generate_report(*args, **kwargs):
    """
    生成分析报告的占位函数（待实现）。
    """
    print("⚠️ 生成报告功能暂未实现")