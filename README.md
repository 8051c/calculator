# 🧮 Calculator

> Python + Tkinter로 만든 독립형 계산기 애플리케이션
> 
> Claude 없이 어디서나 실행 가능한 .exe 파일

---

## 📌 개요

**Calculator**는 Python으로 만든 간단하면서도 실용적인 계산기입니다.

- ✅ **독립 실행 가능**: Python 설치 불필요, .exe만 있으면 실행
- ✅ **사용하기 쉬움**: 직관적인 버튼 인터페이스
- ✅ **키보드 지원**: 마우스 클릭 또는 키보드 입력 모두 가능
- ✅ **에러 처리**: 0으로 나누기 등의 오류 방지

---

## 🎯 기능

### 버튼 기능
- **AC**: 모든 입력값 초기화
- **DEL**: 마지막 숫자 삭제
- **숫자 (0-9)**: 숫자 입력
- **연산자 (+, −, ×, ÷)**: 덧셈, 뺄셈, 곱셈, 나눗셈
- **소수점 (.)**: 소수 입력
- **등호 (=)**: 계산 실행

### 키보드 단축키
| 키 | 기능 |
|---|---|
| `0-9` | 숫자 입력 |
| `.` | 소수점 입력 |
| `+` | 덧셈 |
| `-` | 뺄셈 |
| `*` | 곱셈 |
| `/` | 나눗셈 |
| `Enter` | 계산 실행 |
| `Backspace` | 마지막 숫자 삭제 |
| `Escape` | 초기화 |

---

## 💻 기술 스택

| 항목 | 설명 |
|---|---|
| **언어** | Python 3.11+ |
| **GUI 프레임워크** | Tkinter (Python 기본 내장) |
| **배포 도구** | PyInstaller |
| **OS** | Windows (다른 OS도 동작 가능) |

---

## 📥 설치

### 방법 1: 실행 파일 (.exe) 사용 (권장)

1. **[Releases](releases) 페이지에서 최신 `calculator.exe` 다운로드**
2. 더블클릭으로 실행
   ```
   Python 설치 불필요!
   ```

### 방법 2: Python 코드로 실행

#### 요구 사항
- Python 3.11 이상

#### 설치 및 실행
```bash
# 1. 저장소 클론
git clone https://github.com/[your-username]/calculator.git
cd calculator

# 2. calculator.py 실행
python calculator.py
```

### 방법 3: .exe 파일 직접 생성

#### 요구 사항
- Python 3.11+
- pip (Python 패키지 매니저)

#### 단계별 가이드

**Step 1: PyInstaller 설치**
```bash
pip install pyinstaller
```

**Step 2: .exe 생성**
```bash
pyinstaller --onefile --windowed calculator.py
```

**Step 3: 실행**
```
dist/calculator.exe 더블클릭
```

---

## 🚀 사용 방법

### 기본 계산
1. 숫자 입력 (마우스 또는 키보드)
2. 연산자 선택
3. 다음 숫자 입력
4. `=` 버튼 클릭 또는 `Enter` 키 입력

### 예시
```
25 + 17 = 42

Step 1: [2] [5] → "25" 표시
Step 2: [+] → "25 +" 표시
Step 3: [1] [7] → "17" 표시
Step 4: [=] → "42" 결과 표시
```

---

## 📁 파일 구조

```
calculator/
├── calculator.py           # 메인 프로그램 (Python 소스코드)
├── README.md               # 이 파일
├── .gitignore             # Git 무시 설정
├── LICENSE                # 라이선스
└── dist/
    └── calculator.exe     # 컴파일된 실행 파일 (Windows)
```

---

## ⚙️ 개발 환경 설정

### 개발자용 설치

```bash
# 1. 저장소 클론
git clone https://github.com/[your-username]/calculator.git
cd calculator

# 2. 코드 실행 (수정 후 테스트)
python calculator.py

# 3. .exe로 배포 준비
pip install pyinstaller
pyinstaller --onefile --windowed calculator.py
```

### 코드 수정

`calculator.py`를 텍스트 에디터로 열고 수정:
- **디자인 변경**: `setup_ui()` 메서드 수정
- **기능 추가**: `compute()` 또는 새 메서드 추가
- **색상 변경**: 코드 상단의 색상 값 수정

수정 후:
```bash
# 수정 확인
python calculator.py

# .exe 재생성
pyinstaller --onefile --windowed calculator.py
```

---

## 🎨 UI 디자인

### 다크 모드 테마
- **배경**: 진회색 (#1e1e2e)
- **주요 색상**: 파란색 (#667eea) - 연산자
- **강조색**: 
  - 초록색 (#10b981) - 계산 버튼
  - 주황색 (#f59e0b) - 삭제 버튼
  - 빨강색 (#ef4444) - 초기화 버튼

### 반응형 디자인
- **기본 크기**: 400×550px
- **모바일**: 작은 화면에 최적화

---

## 🐛 문제 해결

### .exe 실행 안 됨

**Windows Defender 경고**
1. "자세히 보기" 클릭
2. "실행" 클릭
3. 계산기 실행

**Python 설치 확인**
```bash
python --version
```

### 한글 입력 불가

현재 계산기는 숫자만 지원합니다. 한글 입력이 필요하면 이슈 생성 후 논의하세요.

### 계산 오류

버튼 클릭 또는 Enter 키를 눌렀는데도 계산이 안 되면:
1. 모든 입력값 확인
2. AC 버튼으로 초기화
3. 다시 시도

문제 지속 시 이슈 등록하세요.

---

## 📊 향후 계획

### V2.0 (계획중)
- [ ] 과학 계산기 (sin, cos, tan 등)
- [ ] 계산 히스토리 저장
- [ ] 환율 변환 기능
- [ ] 다국어 지원

### V3.0 (장기계획)
- [ ] 프로그래머용 계산기 (이진, 16진법)
- [ ] 클라우드 동기화
- [ ] 모바일 앱 (Android, iOS)

---

## 📝 라이선스

이 프로젝트는 **MIT 라이선스**를 따릅니다.
자세한 내용은 [LICENSE](LICENSE) 파일을 참고하세요.

---

## 🤝 기여하기

이슈 리포트, 버그 제보, 기능 제안을 환영합니다!

### 기여 방법

1. **이 저장소를 포크(Fork)합니다**
2. **기능 브랜치 생성** (`git checkout -b feature/AmazingFeature`)
3. **변경사항 커밋** (`git commit -m 'Add some AmazingFeature'`)
4. **브랜치에 푸시** (`git push origin feature/AmazingFeature`)
5. **Pull Request 생성**

---

## 📮 연락처

- **이메일**: [your-email@example.com]
- **GitHub Issues**: [프로젝트 이슈 페이지](../../issues)
- **문의**: 언제든지 이슈나 토론 게시판에서 물어보세요!

---

## 🙏 감사의 말

- Python 커뮤니티
- Tkinter 개발자
- PyInstaller 개발 팀

---

## 📚 참고 자료

- [Python 공식 문서](https://python.org)
- [Tkinter 튜토리얼](https://docs.python.org/3/library/tkinter.html)
- [PyInstaller 가이드](https://pyinstaller.org)

---

**⭐ 이 프로젝트가 도움이 되었다면 Star를 눌러주세요!**

```
Made with ❤️ by [Your Name]
Last updated: 2025-01-15
```
