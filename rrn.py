from presidio_analyzer import AnalyzerEngine, RecognizerRegistry
from presidio_analyzer.predefined_recognizers import KrRrnRecognizer
from presidio_analyzer.nlp_engine import NlpEngineProvider
from presidio_anonymizer import AnonymizerEngine

# 한국어 NLP 엔진 설정
kr_nlp_configuration = {
    "nlp_engine_name": "spacy",
    "models": [
        {"lang_code": "kr", "model_name": "ko_core_news_sm"}
    ]
}

# NLP 엔진 생성
kr_nlp_engine = NlpEngineProvider(nlp_configuration=kr_nlp_configuration).create_engine()

# 주민등록번호(RRN) 인식기를 레지스트리에 등록
registry = RecognizerRegistry()
registry.add_recognizer(KrRrnRecognizer())

# 레지스트리와 NLP 엔진을 사용하여 분석기 생성
analyzer = AnalyzerEngine(registry=registry, nlp_engine=kr_nlp_engine)

# 테스트 텍스트에서 한국 RRN 탐지
test_text = "제 주민등록 번호는 000000-0000000 입니다." # 실제 주민등록번호를 입력하세요.
results = analyzer.analyze(text=test_text, language="kr")

# 테스트 텍스트에서 한국 RRN 익명화
anonymizer = AnonymizerEngine()
anonymized_text = anonymizer.anonymize(text=test_text, analyzer_results=results)

# 한국 RRN 익명화 결과 출력
print(anonymized_text.text)