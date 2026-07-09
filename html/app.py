import streamlit as st
from pathlib import Path

# Streamlit 앱 페이지 레이아웃 설정
st.set_page_config(
    page_title="프루트 & 7 슬롯머신 배포 서버",
    page_icon="🎰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# [1] 다양한 경로 탐색 방식 시도 (상대 경로 문제 해결)
current_dir = Path(__file__).resolve().parent

# 후보 1: 일반적인 구조 (내-웹앱/htmls/index.html)
path_option1 = current_dir / "htmls" / "index.html"
# 후보 2: 현재 에러가 발생하는 환경을 고려한 상위 폴더 기준 구조
path_option2 = current_dir.parent / "htmls" / "index.html"
# 후보 3: 혹시 모를 동일 폴더 내 구조 (내-웹앱/index.html)
path_option3 = current_dir / "index.html"

# 최종 파일 경로 결정
final_html_path = None
if path_option1.exists():
    final_html_path = path_option1
elif path_option2.exists():
    final_html_path = path_option2
elif path_option3.exists():
    final_html_path = path_option3

# [2] HTML 파일 로드 및 렌더링
if final_html_path and final_html_path.exists():
    try:
        with open(final_html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # 상단 여백 제거용 CSS 주입
        st.markdown(
            """
            <style>
                .block-container {
                    padding-top: 1rem;
                    padding-bottom: 1rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
                iframe {
                    border-radius: 12px;
                    background-color: #0b0b0f;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        # 슬롯머신 웹앱 화면 표시
        st.components.v1.html(html_content, height=850, scrolling=True)

    except Exception as e:
        st.error("❌ HTML 파일을 읽는 과정에서 오류가 발생했습니다.")
        st.info(f"오류 메시지: {e}")
else:
    # [3] 파일이 여전히 없을 때 노출할 안내 메시지
    st.warning("⚠️ 슬롯머신 웹앱 구동에 필요한 HTML 파일을 찾을 수 없습니다.")
    st.markdown(
        f"""
        ### 📂 GitHub 저장소(Repository)의 폴더명을 다시 확인해 주세요!
        
        현재 Streamlit 서버가 파일 시스템을 탐색하고 있지만 `index.html`을 찾지 못했습니다. 
        **GitHub 레포지토리**에 접속하셔서 아래 규칙대로 파일이 들어가 있는지 눈으로 직접 확인해 보시는 것이 가장 빠릅니다.
        
        #### 💡 추천하는 가장 간단한 해결 방법
        깃허브 저장소 최상위 경로(app.py가 있는 곳)에 **`htmls`**라는 이름의 폴더를 만들고, 그 안에 **`index.html`**을 넣어주세요. 폴더 이름이 대소문자(`htmls` vs `HTMLS`)까지 정확한지 꼭 확인해야 합니다!
        
        * **서버가 시도해 본 경로들:**
          1. `{path_option1}`
          2. `{path_option2}`
          3. `{path_option3}`
        """
    )
