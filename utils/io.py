# utils/io.py
import pandas as pd

def load_uploaded_data(uploaded_file):
    if uploaded_file is not None:
        try:
            return pd.read_csv(uploaded_file, sep=None, engine="python")
        except Exception as e:
            raise ValueError(f"读取文件失败: {e}")
    return None