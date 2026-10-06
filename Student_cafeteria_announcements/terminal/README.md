# 터미널 학식 메뉴 조회

Selenium으로 정수캠퍼스 학식 페이지를 열고 BeautifulSoup으로 당일 메뉴를 읽어 출력한다. 날짜·식사 구간을 HTML에서 찾으므로 학교 페이지 구조가 바뀌면 조회가 실패할 수 있다.

## 실행

**권장: Python 가상환경으로 실행**

Python 3.10 이상과 Chrome이 설치된 Windows에서 이 폴더의 `setup.bat`을 실행합니다. 필요한 패키지는 폴더 내 `.venv`에 설치됩니다. 이후 `menu.bat`은 해당 Python으로 원본 조회 프로그램을 실행합니다. 개인 PC의 절대경로를 사용하지 않습니다.

```cmd
setup.bat
menu
```

EXE 실행이 Device Guard 정책으로 차단되는 PC에서도, 조직에서 허용한 Python 실행 환경을 사용할 수 있습니다. Python 실행도 차단되는 경우 관리자에게 문의하세요.

**기존 conda 환경 사용**
터미널(Anaconda Prompt 또는 cmd)을 열고 현재 폴더(`terminal`)로 이동한 뒤, 아래 명령어를 실행하여 필요한 패키지가 포함된 가상환경을 생성합니다.

```bash
conda env create -f environment.yml
conda activate menu
python menu_bot.py
```

Windows는 `menu.bat`가 로컬 `.venv`를 우선 사용하고, 없으면 Conda `menu` 환경을 사용한다. PATH에 이 terminal 폴더를 등록하면 다른 위치에서도 `menu`를 실행할 수 있다. 일반 Python 명령과 Windows 바로가기를 구분한다.

## Windows PATH 등록

시스템 환경변수 편집에서 사용자 Path에 이 폴더의 절대 경로를 추가하고 새 cmd 창에서 `menu`를 실행한다. 이미 열린 터미널에는 새 PATH가 반영되지 않을 수 있다.

## 🚀 실행 방법

### 방법 1 (해당 폴더에서 실행)
터미널을 열고 본 스크립트가 있는 `terminal` 폴더로 이동한 뒤, 아래 명령어를 입력합니다.

```cmd
menu
```
폴더 내 `.venv`를 우선 사용하고, 없으면 기존 conda `menu` 환경으로 조회합니다.

### 방법 2 (환경변수 PATH 등록 후 실행)
PATH에 이 폴더가 등록되었다면 윈도우의 어느 폴더에서나 단순히 아래와 같이 입력하면 됩니다.

```cmd
menu
```

## EXE 빌드와 장애 확인

```cmd
.venv\Scripts\python.exe -m pip install pyinstaller
.venv\Scripts\python.exe -m PyInstaller --noconfirm menu_bot.spec
```

빌드 설정에서 Selenium과 webdriver-manager의 하위 모듈 및 데이터를 수집합니다. `No module named 'selenium.webdriver.chrome.options'`가 발생하면 이 설정으로 재빌드하세요. 기존 `install.bat`은 EXE 배포용이며 Python 설치에는 `setup.bat`을 사용합니다.

PATH에 이 폴더를 등록한 다음 새 CMD에서 `where menu`로 등록 경로를 확인하고, 다른 폴더에서 `menu`를 실행하세요. 주말 안내만 확인하면 브라우저 의존성을 검증하지 못하므로 실제 평일 식단 조회까지 확인해야 합니다.

2026-10-06 검증: 원본 Python 조회 로직으로 중식·석식 조회 성공. 같은 의존성으로 새 EXE를 빌드했으나 해당 PC의 Device Guard 정책이 실행을 차단하여 EXE의 조회 성공은 확인하지 못했습니다.

카카오 전송 코드와 달리 이 스크립트는 터미널 출력용이다. 조회 성공은 Chrome·학교 페이지·네트워크에 의존하며 배포된 bot 서비스가 아니다.
