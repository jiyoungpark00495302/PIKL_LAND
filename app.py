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

import os, json
from datetime import datetime, timezone, timedelta
import streamlit as st

COUNT_FILE = "visit_count.txt"
LOG_FILE = "visit_log.jsonl"
KST = timezone(timedelta(hours=9))

def load_count():
    if not os.path.exists(COUNT_FILE):
        with open(COUNT_FILE, "w", encoding="utf-8") as f:
            f.write("0")
        return 0
    with open(COUNT_FILE, "r", encoding="utf-8") as f:
        return int(f.read().strip() or 0)

def save_count(n: int):
    with open(COUNT_FILE, "w", encoding="utf-8") as f:
        f.write(str(n))

def append_log(event: dict):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


# ✅ 아래부터는 "사용" 구간 (함수 정의 이후)
count = load_count()

if "counted_visit" not in st.session_state:
    st.session_state.counted_visit = True
    count += 1
    save_count(count)
    append_log({
        "ts": datetime.now(KST).isoformat(),
        "type": "page_view",
        "page": "home"
    })


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

# ✅ 버튼 하나로 합치기
if st.button("시작하기", use_container_width=True):
    # 1) 클릭 로그 기록
    append_log({
        "ts": datetime.now(KST).isoformat(),
        "type": "click",
        "page": "home",
        "target": "google_form_start"
    })

    # 2) 구글 폼 새 탭 열기
    st.components.v1.html(f"""
        <script>
            window.open("{FORM_URL}", "_blank");
        </script>
    """, height=0)

    st.success("구글 폼을 새 탭에서 열었어요!")
