import streamlit as st

GOOGLE_FORM_URL = "https://forms.gle/여기에_네_구글폼_링크"

st.set_page_config(
    page_title="PIKL",
    page_icon="🚀",
    layout="centered",
)

st.title("PIKL 🚀")
st.write("한 줄 소개: 이 서비스는 ~~를 ~~하게 해줍니다.")

st.subheader("기능 설명")
st.markdown(
    """
- ✅ 기능 1: 뭐가 좋은지
- ✅ 기능 2: 누구에게 좋은지
- ✅ 기능 3: 어떤 결과가 나오는지
"""
)

st.divider()

# 버튼을 누르면 새 탭으로 링크 열리는 '링크 버튼'
st.link_button("시작하기","https://forms.gle/tCjHKKRSAvNPXnJdA" , type="primary", use_container_width=True)
