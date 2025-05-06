# LoveLog - Couple Diary API

## 프로젝트 소개

**LoveLog**는 연인 커플이 함께한 데이트, 기념일, 소소한 순간들을 기록하고 공유할 수 있도록 돕는 API 프로젝트입니다.  
타임라인, 캘린더, 감정 기록 등 다양한 기능을 통해 커플만의 추억을 쉽고 따뜻하게 관리할 수 있습니다.

---

## 프로젝트 배경

- 커플이 함께한 소중한 순간들을 기록하고, 서로의 감정과 추억을 공유할 수 있는 서비스가 필요하다고 느꼈습니다.
- 단순한 기록을 넘어, 타임라인/캘린더/감정 공유 등 커플만의 특별한 경험을 제공하는 것이 목표입니다.
- 누구나 쉽게 사용할 수 있도록 직관적이고 확장 가능한 API로 설계되었습니다.

---

## 주요 기능

- 데이트 기록(텍스트, 사진, 장소, 태그, 감정 등)
- 커플 타임라인 및 캘린더
- 기념일/이벤트 관리
- 기록 내보내기 및 백업
- 향후 AI 추천, 커플 미션 등 확장 가능

---

## 기술 스택

- **Python 3.12+**
- **FastAPI** : 고성능 비동기 Python 웹 프레임워크
- **Uvicorn** : ASGI 서버 (FastAPI 실행용)
- **Pydantic** : 데이터 검증 및 직렬화
- (추후 DB, 인증 등 확장 가능)

---

## 설치 및 실행 방법

1. **의존성 설치**
   ```bash
   cd couple_diary_api
   pip install poetry
   poetry install
   ```

2. **서버 실행**
   ```bash
   poetry run uvicorn src.couple_diary_api.main:app --reload
   ```
   - (main.py 파일이 없다면, 실제 FastAPI 앱 진입점 파일명을 확인해 주세요.)

3. **API 문서 확인**
   - 서버 실행 후 [http://localhost:8000/docs](http://localhost:8000/docs) 에서 Swagger UI로 API를 테스트할 수 있습니다.

---

## 폴더 구조

```
couple_diary_api/
  ├─ src/
  │   └─ couple_diary_api/
  │        └─ __init__.py
  ├─ tests/
  ├─ pyproject.toml
  ├─ poetry.lock
  └─ README.md
```

---

## 기여 및 문의

- 이 프로젝트는 누구나 기여할 수 있습니다.
- 버그, 제안, 문의사항은 이슈로 남겨주세요.
- 메인테이너: soohyun (developer.shkim@gmail.com)
