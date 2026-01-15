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
st.link_button("시작하기",GOOGLE_FORM_URL , type="primary", use_container_width=True)



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

# ---------------------------
# 탭 1: 버튼 + 카운트
# ---------------------------
with tab1:
    st.subheader("Google Form 시작하기")

    # 실제 이동용 링크 버튼
    st.link_button(
        "시작하기",
        GOOGLE_FORM_URL,
        type="primary",
        use_container_width=True
    )

    # 클릭 감지용 버튼 (카운트 증가)
    if st.button("시작하기 버튼 클릭 기록", use_container_width=True):
        st.session_state.click_count += 1
        log_click(st.session_state.click_count)
        st.success("클릭이 기록되었습니다!")

    st.metric(
        label="총 클릭 수",
        value=st.session_state.click_count
    )

# ---------------------------
# 탭 2: 로그 확인
# ---------------------------
with tab2:
    st.subheader("클릭 기록 로그")

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = f.read()
        st.text_area(
            "기록 내용",
            logs,
            height=400
        )
    except FileNotFoundError:
        st.info("아직 기록된 클릭이 없습니다.")
