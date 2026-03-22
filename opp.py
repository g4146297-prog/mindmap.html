import streamlit as st
import streamlit.components.v1 as components

# ページ全体を広く使う設定
st.set_page_config(layout="wide", page_title="思考マップ")

# Streamlitのデフォルトの余白を消すためのCSS
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }
    </style>
""", unsafe_allow_html=True)

# mindmap.html を読み込んで画面いっぱいに表示する
try:
    with open("mindmap.html", "r", encoding="utf-8") as f:
        html_data = f.read()
        # heightを指定してスクロールバーが出ないように調整
        components.html(html_data, height=900, scrolling=False)
except FileNotFoundError:
    st.error("mindmap.html が見つかりません。同じディレクトリに配置されているか確認してください。")
