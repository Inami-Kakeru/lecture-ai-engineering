import streamlit as st
import pandas as pd
import numpy as np
import time

# ページ設定
st.set_page_config(
    page_title="Streamlit 機能体験デモ",
    layout="wide",
    initial_sidebar_state="expanded"
)

# タイトル
st.title("🚀 Streamlit 入門ガイド")
st.markdown("このアプリは、Streamlitの基本的な機能を体験しながら学べるインタラクティブなデモです。")

# サイドバー
with st.sidebar:
    st.header("💡 ガイド")
    st.markdown("各タブでは、Streamlitでよく使われるUIを確認できます。")
    st.markdown("必要に応じてコードの一部を有効化しながら、動作を確認してください。")

# 解説表示切り替え
if st.checkbox("各機能の解説を表示する"):
    show_guide = True
else:
    show_guide = False

# タブで整理
tab1, tab2, tab3 = st.tabs(["🎮 入力・操作", "📊 データ表示", "📈 グラフ・応答"])

with tab1:
    st.header("🎮 入力操作")

    name = st.text_input("あなたの名前を入力してください", "")
    if name:
        st.success(f"こんにちは、{name}さん！")

    if show_guide:
        st.info("`st.text_input()`は、ユーザーから文字列入力を受け取るUI要素です。")

    if st.button("ボタンをクリック！"):
        st.balloons()
        st.success("クリックされました！")

    if st.checkbox("追加の情報を表示"):
        st.info("これはチェックボックスで表示される追加情報です。")

    age = st.slider("あなたの年齢は？", 0, 100, 20)
    st.write(f"選択された年齢: {age}")

    lang = st.selectbox("好きな言語は？", ["Python", "JavaScript", "C++", "Go", "Rust"])
    st.write(f"選んだ言語: {lang}")

with tab2:
    st.header("📊 データ表示")
    
  df = pd.DataFrame({
       '名前': ['田中', '鈴木', '佐藤', '高橋', '伊藤'],
       '年齢': [25, 30, 22, 28, 33],
       '都市': ['東京', '大阪', '福岡', '札幌', '名古屋']})
    st.dataframe(df)

    st.subheader("テーブル表示（静的）")
    st.table(df)

with tab3:
    st.header("📈 グラフと応答機能")

    st.subheader("ランダムなラインチャート")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
    st.line_chart(chart_data)

    st.subheader("ファイルアップロード")
    uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("ファイルを読み込みました！")
        st.dataframe(df)

    st.subheader("進捗バー")
    if st.button("進捗バーを表示"):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

# 最後の案内
st.divider()
st.markdown("このアプリは `Streamlit` の機能を試すために作られています。コードを少しずつ理解してきています。")
