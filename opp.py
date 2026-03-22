import streamlit as st
import streamlit.components.v1 as components

# ページ全体を広く使う設定
st.set_page_config(layout="wide", page_title="思考マップ")

# Streamlitのヘッダーと被らないように、上部だけ少し余白（3rem）を持たせる
st.markdown("""
    <style>
        .block-container {
            padding-top: 3rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
    </style>
""", unsafe_allow_html=True)

# mindmap.html を読み込んで表示
try:
    with open("mindmap.html", "r", encoding="utf-8") as f:
        html_data = f.read()
        components.html(html_data, height=850, scrolling=False)
except FileNotFoundError:
    st.error("mindmap.html が見つかりません。同じディレクトリに配置されているか確認してください。")
