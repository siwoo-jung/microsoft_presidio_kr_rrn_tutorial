# Microsoft Presidio를 이용한 한국 주민등록번호 인식 및 익명화 튜토리얼

이 튜토리얼은 Microsoft Presidio를 사용하여 한국 주민등록번호(RRN)를 인식 및 익명화하는 방법을 보여줍니다.

## 개요

한국의 주민등록번호는 개인정보보호법에 따라 민감한 개인정보로 분류되어 있습니다. 이 튜토리얼에서는 Presidio의 한국어 지원 기능을 활용하여 RRN을 자동으로 탐지하고 익명화하는 방법을 학습할 수 있습니다.

## Presidio의 한국 주민등록번호 인식기 소스코드

https://github.com/microsoft/presidio/blob/main/presidio-analyzer/presidio_analyzer/predefined_recognizers/country_specific/korea/kr_rrn_recognizer.py

## 설치

### 1. 필요한 패키지 설치

```text
pip install git+https://github.com/microsoft/presidio.git@9a25509b9ead7fa3e6adafff4b64ebef13c0357e#subdirectory=presidio-analyzer

pip install git+https://github.com/microsoft/presidio.git@9a25509b9ead7fa3e6adafff4b64ebef13c0357e#subdirectory=presidio-anonymizer
```

### 2. 한국어 spaCy 모델 다운로드

```bash
python -m spacy download ko_core_news_sm
```

## 사용법

### 기본 사용 예제

```python
python rrn.py
```
### 실행 결과

원본 텍스트:
```python
제 주민등록 번호는 000000-0000000 입니다.
# rrn.py에서 000000-0000000 대신 실제 주민등록번호를 입력해주세요
```

익명화된 텍스트:
```python
제 주민등록 번호는 <KR_RRN> 입니다.
```