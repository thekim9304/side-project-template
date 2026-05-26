# Docker 기반 AI 사이드 프로젝트 템플릿

이 템플릿은 원래의 `Docker 기반 데이터 분석 프로젝트` 출발점을 유지하면서, AI Engineer가 실제로 자주 하는 작업까지 한 번에 시작할 수 있게 확장한 버전이다.

기존 템플릿이 잘하던 것은 `JupyterLab에서 바로 분석 시작`하는 것이었다.
이번 재구성에서는 그 장점은 유지하고, 아래 목적까지 자연스럽게 이어지도록 구조를 넓혔다.

- 데이터 분석과 EDA
- NLP / Vision / 검색 / 추천 모델 실험
- 추론 API와 간단한 백엔드 구성
- 데모 앱, PoC, 내부 시연 준비

## 왜 재구성했나

원래 구조는 `workspace + src + docs` 정도의 아주 가벼운 분석 템플릿이었다.
그 구조는 빠르게 노트북을 열기에는 좋지만, AI 프로젝트가 커질 때 아래 문제가 생기기 쉽다.

- 노트북 코드와 재사용 코드가 섞임
- 모델 실험 결과와 서비스 코드가 같은 위치에 뒤섞임
- 데이터, 체크포인트, 평가 결과 경계가 흐려짐
- 나중에 API나 데모를 붙일 때 구조를 다시 뜯어야 함

그래서 이번에는 `탐색`, `재사용 코드`, `서비스`, `데이터`, `아티팩트`, `문서`, `검증`의 책임을 처음부터 나눴다.

## 어떻게 재구성했나

### 1. Jupyter 중심 구조를 유지하되 역할을 분리했다

- 기존의 Jupyter 기반 진입점은 유지했다.
- 다만 작업 폴더를 `workspace/`에서 `notebooks/`로 바꿔 목적을 더 분명하게 했다.
- 노트북은 탐색과 빠른 검증용으로 두고, 재사용할 코드는 `src/`로 올리는 흐름을 기본값으로 잡았다.

### 2. API/서빙 시작점을 같이 넣었다

- `src/api/main.py`에 FastAPI 골격을 추가했다.
- 이제 이 템플릿은 분석만 하는 저장소가 아니라, 추론 API와 데모 백엔드를 바로 붙일 수 있는 출발점이 된다.
- `docker compose --profile app up`으로 API 컨테이너까지 함께 띄울 수 있게 구성했다.

### 3. 데이터와 산출물 경계를 분리했다

- `data/raw`, `data/interim`, `data/processed`
- `artifacts/checkpoints`, `artifacts/evals`, `artifacts/predictions`, `artifacts/indexes`

이렇게 나눈 이유는 다음과 같다.

- 데이터 흐름을 추적하기 쉬움
- 체크포인트와 평가 결과를 분리하기 쉬움
- 나중에 실험 재현성과 배포 아티팩트 관리를 더 쉽게 가져갈 수 있음

### 4. 프로젝트 로컬 에이전트 규칙을 추가했다

- 저장소 루트에 [AGENTS.md](/Users/kimtae/Kimtae/Workspace/side-project-template/AGENTS.md)를 추가했다.
- 이 파일은 전역 `/Users/kimtae/AGENTS.md` 위에 덧씌워져서, 이 템플릿 안에서는 AI 실험/데모/API 중심으로 Codex가 행동하게 만든다.

예를 들면:

- 실험 작업이면 데이터 누수, 평가 기준, 재현성을 먼저 보게 됨
- API 작업이면 입출력 스키마, 예외 처리, 모델 로딩 경계를 먼저 보게 됨
- 데모 작업이면 사용자 흐름, 실패 상태, 임시 하드코딩 표시를 먼저 챙기게 됨

### 5. 문서와 반복 실행 지점을 분리했다

- `docs/`: 기획, 실험 기록, 아키텍처, 보고서
- `scripts/`: 전처리, 배치 추론, 평가 리포트 같은 반복 실행 스크립트
- `tests/`: 최소 자동 검증
- `configs/`: 실험/서빙 설정

이렇게 해두면 노트북만 커지는 프로젝트가 아니라, 점점 운영 가능한 구조로 자라기 쉬워진다.

## 폴더 및 파일 구조

```text
.
├── AGENTS.md
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── requirements.txt
├── artifacts/
│   ├── checkpoints/
│   ├── evals/
│   ├── indexes/
│   └── predictions/
├── configs/
├── data/
│   ├── interim/
│   ├── processed/
│   └── raw/
├── docs/
├── jupyter_config/
├── notebooks/
├── scripts/
├── src/
│   ├── api/
│   └── common/
└── tests/
```

## 폴더 설명

- `notebooks/`: 메인 탐색 공간. EDA, 시각화, 빠른 가설 검증용 노트북
- `src/`: 재사용 가능한 소스 코드
- `src/api/`: FastAPI 기반 API 진입점
- `src/common/`: 공용 설정, 경로, 유틸
- `docs/`: 기획, 아키텍처, 실험 메모, 최종 보고서
- `configs/`: 실험/서빙/데모 설정 파일
- `scripts/`: 반복 실행 스크립트
- `tests/`: 자동 검증 코드
- `data/`: 로컬 데이터 작업 공간
- `artifacts/`: 체크포인트, 인덱스, 평가 결과, 예측 결과
- `jupyter_config/`: JupyterLab UI 설정

## 시작하기

### 사전 요구사항

- [Docker](https://www.docker.com/get-started) 설치

### 실행 순서

0. 환경 변수 설정

먼저 `.env.example` 파일을 복사해 `.env` 파일을 만든다.

```bash
cp .env.example .env
```

필요하면 `.env`에서 API 키, 데이터 경로, 아티팩트 경로를 수정한다.

1. 라이브러리 추가

필요한 Python 라이브러리를 `requirements.txt`에 추가한다.
이 템플릿은 일부러 가볍게 유지했기 때문에, 실제 프로젝트에 필요한 프레임워크를 직접 추가하는 방식이다.

예:

- NLP: `transformers`, `datasets`, `sentence-transformers`
- Vision: `torch`, `torchvision`, `opencv-python`, `ultralytics`
- 추천/검색: `faiss-cpu`, `lightfm`, `implicit`

2. JupyterLab 실행

분석과 실험만 먼저 시작하고 싶으면 아래 명령으로 JupyterLab만 띄운다.

```bash
docker compose up --build lab -d
```

3. JupyterLab 접속

웹 브라우저에서 아래 주소로 접속한다.

- `http://localhost:8888`

4. API까지 같이 실행

API/데모 백엔드까지 같이 보고 싶으면 아래 명령을 사용한다.

```bash
docker compose --profile app up --build -d
```

5. API 확인

헬스체크:

```bash
curl http://localhost:8000/health
```

런타임 경로 확인:

```bash
curl http://localhost:8000/meta/runtime
```

6. 종료

작업을 마친 뒤 컨테이너를 종료한다.

```bash
docker compose down
```

## 권장 작업 흐름

1. `notebooks/`에서 문제 정의와 데이터 구조를 빠르게 확인한다.
2. 재사용할 로직은 `src/`로 옮긴다.
3. 공통 경로/설정 로직은 `src/common/`에 둔다.
4. 추론/백엔드 엔드포인트는 `src/api/`에 붙인다.
5. 결과물과 체크포인트는 `artifacts/`에 둔다.
6. 실험/서빙 설정은 `configs/`에 남긴다.
7. 프로젝트별 추가 규칙은 `AGENTS.md`를 기반으로 구체화한다.

## 이 템플릿에서 바로 제공하는 것

- Docker 기반 JupyterLab 개발 환경
- FastAPI 기반 API 시작점
- AI Engineer용 로컬 `AGENTS.md`
- 데이터/아티팩트/설정/문서 경계가 있는 폴더 구조
- 실험에서 서비스/데모로 이어가기 쉬운 기본 형태

## 이 템플릿이 특히 잘 맞는 경우

- 모델을 빠르게 실험하고 나중에 API까지 붙일 가능성이 높은 프로젝트
- 검색/추천/비전/NLP 중 무엇으로 갈지 아직 탐색 중인 프로젝트
- 내부 PoC나 데모를 빠르게 만들어야 하는 프로젝트
- 노트북에서 시작하지만 코드 구조를 너무 망가뜨리고 싶지 않은 프로젝트

## 다음 추천 작업

- `docs/project-brief.md` 작성
- `configs/train.yaml` 또는 `configs/inference.yaml` 추가
- `notebooks/`에 첫 탐색 노트북 추가
- `src/api/main.py`에 실제 추론 엔드포인트 추가
- `tests/`에 최소 스모크 테스트 추가
