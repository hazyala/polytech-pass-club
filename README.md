# P.A.S.S 프로젝트와 실습

[GPT 챗봇 웹 데모](https://chatbot-project-made-by-hazyala.onrender.com/)

동아리 활동에서 만든 챗봇, 학식 조회 자동화, C 실습을 모은 저장소.

## 프로젝트별 진입점

| 프로젝트 | 구현 | 문서 |
|---|---|---|
| GPT 웹 챗봇 | HTML/JS → Express → OpenAI API | [ChatBot_Project](ChatBot_Project/README.md) |
| 터미널 학식 조회 | Selenium·BeautifulSoup → 학교 메뉴 출력 | [terminal](Student_cafeteria_announcements/terminal/README.md) |
| 카카오 학식 실험 | 학식 scraping, token 갱신·카카오 메시지 요청 코드 | `Student_cafeteria_announcements/kakao/` |
| C 수업 | 별·구구단·게임·신호등 예제 | `C_study/` |

챗봇과 학식 프로그램은 실행 환경이 다르며 공통 backend가 없다. 챗봇은 요청에 받은 키로 모델 API를 호출하고, 학식은 학교 페이지의 HTML 구조를 읽는다. 카카오 스크립트는 외부 메시지 전송을 포함하므로 일반 실행 안내와 분리한다.

현재 챗봇의 서버 시작 코드에는 같은 포트의 listen이 두 번 있어 실행 장애가 있다. 자세한 코드 상태를 챗봇 README에 기록했다. 배포된 시작 화면과 입력 검증 API는 접근 가능하지만, 현재 코드를 그대로 재배포하는 조건은 별도로 확인해야 한다.
