import streamlit as st

with st.form(key="profile_form"):
    # テキストボックス
    name = st.text_input("名前を入力してください")
    address = st.text_input("住所を入力してください")
    print(name)

    # ラジオボックス
    age_category = st.radio("年齢を選択してください", ("子供", "大人"))

    # 複数選択
    hobby = st.multiselect("趣味を選択してください", ("野球", "サッカー", "テニス"))

    # ボタン
    submit_btn = st.form_submit_button("送信")
    cancel_btn = st.form_submit_button("キャンセル")
    print(f"submit_btn: {submit_btn}")
    print(f"cancel_btn: {cancel_btn}")

    if submit_btn:
        st.text(f"{name}さん、こんにちは！{address}にお住まいですね！")
        st.text(f"年齢層: {age_category}")
        st.text(f"趣味: {', '.join(hobby)}")
