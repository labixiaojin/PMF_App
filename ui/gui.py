# gui.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from utils.io import load_uploaded_data
from pmf_core.model import PMF
from bootstrap.bootstrap import run_bootstrap, generate_report

def launch_app():
    st.set_page_config(page_title="🧪 PMF 智能因子分析平台", layout="wide")
    st.markdown("<h1 style='text-align: center;'>🧪 欢迎使用 PMF 智能因子分析平台</h1>", unsafe_allow_html=True)
    
    # 导航栏
    tab = st.sidebar.radio("导航", ["首页", "数据上传与参数", "分析结果展示"])

    if tab == "首页":
        st.success("👋 欢迎！请通过侧边栏导航进入操作流程。")

    elif tab == "数据上传与参数":
        st.subheader("📁 数据上传")
        uploaded_conc = st.file_uploader("上传浓度数据", type=["csv", "txt"])
        uploaded_unc = st.file_uploader("上传不确定性数据", type=["csv", "txt"])

        st.subheader("🎛 参数设置")
        n_factors = st.number_input("因子数", min_value=2, max_value=10, value=4)
        n_bootstrap = st.number_input("Bootstrap 次数", min_value=0, max_value=100, value=10, step=5)

        run_button = st.button("🚀 开始分析")

        if run_button:
            st.info("这里将调用 PMF 模型进行分析。此处仅为框架，尚未接入具体分析逻辑。")

    elif tab == "分析结果展示":
        st.subheader("📊 分析结果展示")
        st.info("此处将展示分析结果图表与报告。")

if __name__ == "__main__":
    launch_app()