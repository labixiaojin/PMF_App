### 📌 PMF 智能因子分析平台开发进度记录

#### ✅ 项目初始化

- 创建项目结构：
  ```
  PMF_App/
    ├── ui/                # Streamlit 前端界面
    ├── pmf_core/          # PMF 模型核心功能
    ├── bootstrap/         # Bootstrap 分析相关模块
    ├── utils/             # 工具函数模块
    ├── output/            # 输出结果文件夹
    ├── main.py            # 启动入口
    ├── requirements.txt   # 依赖项
    └── .gitignore         # Git 忽略配置
  ```

- 配置 GitHub 仓库 `PMF_APP/PMF_App` 并完成初始推送

#### ✅ GUI 功能模块开发

- ✅ `ui/gui.py` 页面搭建完成，具有导航栏、上传数据、参数设置、分析运行、结果展示等功能分区
- ✅ 支持分析运行状态卡片实时显示
- ✅ 支持上传数据后进行格式校验（空值、负值、零等异常）
- ✅ 开始分析按钮与数据校验联动控制，数据异常时按钮置灰
- ✅ 支持残差分析图（热力图、残差分布、Q值趋势）
- ✅ Bootstrap 分析结果可视化与 Markdown 报告导出
- ✅ 页面布局支持固定顶部与响应式横向导航

#### ✅ 底层功能开发

- ✅ PMF 模型类：核心分解算法 `PMF.fit()`
- ✅ 残差分析模块：`compute_residuals`, `plot_residual_histogram`, `plot_q_trend`, `plot_residual_heatmap`
- ✅ Bootstrap 分析：支持多次拟合并统计均值与标准差
- ✅ 工具函数：上传数据读取、异常检查、报告生成等

---

**⏳ 未完成但已规划的内容：**

- [ ] 用户可自定义因子命名
- [ ] 数据预处理支持更多格式（如 Excel）
- [ ] 分析结果支持导出为 PDF 报告
- [ ] 更详细的交互式残差分析页面
- [ ] 云端部署及多用户支持
- [ ] 代码进一步模块解耦、测试覆盖
