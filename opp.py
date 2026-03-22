import streamlit as st
import streamlit.components.v1 as components

# mindmap.html を読み込んで画面いっぱいに表示する
with open("mindmap.html", "r", encoding="utf-8") as f:
    components.html(f.read(), height=800, scrolling=True)
