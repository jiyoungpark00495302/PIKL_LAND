######-------------페이지 구현---------############

import streamlit as st

GOOGLE_FORM_URL = "https://forms.gle/43bhQMmmKLGZjswH9"

st.set_page_config(
    page_title="PIKL",
    page_icon="",
    layout="centered",
)

st.title("PIKL")
st.write("""
        건강한 토론장이 되는 사회 공유 서비스
        """)


st.markdown(
    """
- ✅ 우리학교, 우리 학과에서 가장 뜨거운 이슈를 확인해요!
- ✅ 민감한 주제에 대해서도 건강하게 의견을 나눠요!
- ✅ 의견을 공유할 때마다 무럭무럭 자라나는 피클!
"""
)

st.divider()

# 버튼을 누르면 새 탭으로 링크 열리는 '링크 버튼'
#st.link_button("시작하기",GOOGLE_FORM_URL , type="primary", use_container_width=True)



####---------------카운트-------------##############
import streamlit as st
import os, json
from datetime import datetime, timezone, timedelta
from pathlib import Path


st.set_page_config(page_title="버튼 클릭 카운터", layout="wide")

# ---------------------------
# session_state 초기화
# ---------------------------
if "click_count" not in st.session_state:
    st.session_state.click_count = 0

# ---------------------------
# 기록 함수
# ---------------------------

LOG_FILE = "click_log.txt"
def log_click(count):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | click_count={count}\n")

# ---------------------------
# 탭 구성
# ---------------------------
tab1, tab2 = st.tabs(["📌 시작하기", "📊 클릭 기록"])

KST = timezone(timedelta(hours=9))


if st.button("🚀 시작하기", use_container_width=True):
    # 1. 클릭 로그 기록
    append_log({
        "ts": datetime.now(KST).isoformat(),
        "type": "click",
        "page": "home",
        "target": "google_form_start"
    })

    # 2. 링크 열기
    st.success("구글 폼을 여는 중입니다 👇")
    st.markdown(f"""
    <meta http-equiv="refresh" content="0; url={FORM_URL}">
    """, unsafe_allow_html=True)
