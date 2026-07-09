import streamlit as st
from pathlib import Path

# Streamlit 앱 페이지 레이아웃 설정 (최대한 전체 화면을 활용하기 위해 wide 설정)
st.set_page_config(
    page_title="프루트 & 7 슬롯머신 배포 서버",
    page_icon="🎰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# [1] HTML 파일의 절대 경로 설정 (프로젝트 폴더 구조 전제)
current_dir = Path(__file__).resolve().parent
html_file_path = current_dir / "htmls" / "index.html"

# [2] HTML 파일 로드 및 렌더링 검증
if html_file_path.exists():
    try:
        # 인코딩 에러 방지를 위해 utf-8로 파일 읽기
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Streamlit 화면 상단 여백 제거용 CSS 주입
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

        # HTML 컴포넌트를 이용해 index.html 전체 화면 렌더링
        # 모바일 및 데스크톱 환경에서 스크롤 없이 잘 보이도록 충분한 높이(height) 지정
        st.components.v1.html(html_content, height=850, scrolling=True)

    except Exception as e:
        st.error("❌ HTML 파일을 읽는 과정에서 오류가 발생했습니다.")
        st.info(f"오류 메시지: {e}")
else:
    # [3] 파일이 없을 때 노출할 친절한 한국어 안내 메시지 (중괄호 오류 수정 완료)
    st.warning("⚠️ 슬롯머신 웹앱 구동에 필요한 HTML 파일을 찾을 수 없습니다.")
    st.markdown(
        f"""
        ### 📂 현재 확인된 저장소 구조를 체크해 주세요
        정상적인 실행을 위해 아래와 같은 폴더 구조로 파일이 배치되어 있는지 확인이 필요합니다.
        
        ```text
        내-웹앱/
        ├── app.py
        ├── requirements.txt
        └── htmls/
            └── index.html 👈 이 위치에 슬롯머신 파일이 있어야 합니다.
        ```
        
        * **현재 탐색한 경로:** `{html_file_path}`
        * **해결 방법:** `htmls` 폴더를 생성하고 그 안에 생성된 `index.html` 소스코드를 저장해 주세요.
        """
    )
    
