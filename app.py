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


####---------------카운트-------------##############
import streamlit as st
import os, json
from datetime import datetime, timezone, timedelta
from pathlib import Path

COUNT_FILE = Path("visit_count.txt")
LOG_FILE = Path("visit_log.jsonl")
KST = timezone(timedelta(hours=9))

def load_count():
    if not COUNT_FILE.exists():
        COUNT_FILE.write_text("0", encoding="utf-8")
        return 0
    txt = COUNT_FILE.read_text(encoding="utf-8").strip()
    return int(txt) if txt else 0

def save_count(n: int):
    COUNT_FILE.write_text(str(n), encoding="utf-8")

def append_log(event: dict):
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")

# ✅ 세션(탭) 최초 1회만 증가
if "counted" not in st.session_state:
    st.session_state["counted"] = True

    count = load_count() + 1
    save_count(count)
    append_log({
        "ts": datetime.now(KST).isoformat(),
        "type": "page_view",
        "page": "home"
    })
else:
    count = load_count()

st.write(f"📌 방문 수(세션당 1회): {count}")



import streamlit as st
import os, json
from datetime import datetime, timezone, timedelta

COUNT_FILE = "visit_count.txt"
LOG_FILE = "visit_log.jsonl"
KST = timezone(timedelta(hours=9))

def load_count():
    if not os.path.exists(COUNT_FILE):
        with open(COUNT_FILE, "w") as f:
            f.write("0")
        return 0
    with open(COUNT_FILE, "r") as f:
        return int(f.read().strip() or 0)

def save_count(n: int):
    with open(COUNT_FILE, "w") as f:
        f.write(str(n))

def append_log(event: dict):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")

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

st.info(f"📌 방문 수(세션당 1회): {count}")
st.write(open("visit_log.jsonl").read())
