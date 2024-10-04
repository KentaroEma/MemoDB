import streamlit as st
import requests
import json

page = st.sidebar.selectbox('Choose your page', ['registration', 'list'])

if page == 'registration':
    st.title('メモ登録画面')
    with st.form(key='registration'):
        content: str = st.text_input('メモ内容', max_chars=100)
        data = {
                'content': content
        }
        submit_button = st.form_submit_button(label='メモ登録')

        if submit_button:
            url = 'http://10.58.191.253:8501/memos'
            res = requests.post(
                url,
                data=json.dumps(data)
            )
            if res.status_code == 200:
                st.success('メモ登録完了')
            st.json(res.text)

elif page == 'list':
    st.title('メモ一覧画面')
    res = requests.get('http://10.58.191.253:8501/memos')
    records = res.json()
    for record in records:
        st.subheader('・' + record.get('content'))
