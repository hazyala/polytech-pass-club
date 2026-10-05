# 터미널 학식 메뉴 조회

Selenium으로 정수캠퍼스 학식 페이지를 열고 BeautifulSoup으로 당일 메뉴를 읽어 출력한다. 날짜·식사 구간을 HTML에서 찾으므로 학교 페이지 구조가 바뀌면 조회가 실패할 수 있다.

## 실행

이 폴더에서 Conda 환경을 만든다. environment.yml은 Python 3.10, Selenium, webdriver-manager, BeautifulSoup, requests를 포함한다. Chrome과 driver 다운로드 네트워크가 필요하다.

```bash
conda env create -f environment.yml
conda activate menu
python menu_bot.py
```

Windows는 `menu.bat`가 환경 활성화와 스크립트 위치를 처리한다. PATH에 이 terminal 폴더를 등록하면 다른 위치에서도 `menu`를 실행할 수 있다. 일반 Python 명령과 Windows 바로가기를 구분한다.

## Windows PATH 등록

기존 안내의 사용 흐름을 유지한다. 시스템 환경변수 편집에서 사용자 Path에 이 폴더의 절대 경로를 추가하고 새 cmd 창에서 `menu`를 실행한다. 이미 열린 터미널에는 새 PATH가 반영되지 않을 수 있다.

카카오 전송 코드와 달리 이 스크립트는 터미널 출력용이다. 조회 성공은 Chrome·학교 페이지·네트워크에 의존하며 배포된 bot 서비스가 아니다.
