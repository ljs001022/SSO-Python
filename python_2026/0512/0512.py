# 파일명: day1_review.py
# 목적: 연산자, 예외 처리, 함수 구조, Pandas 기초 통합 실습

import sys

# [1] 라이브러리 체크 (try-except)
# 가상환경(penv)에 필수 라이브러리가 있는지 확인합니다.
try:
    import numpy as np
    import pandas as pd
    HAS_LIBS = True
except ImportError:
    HAS_LIBS = False

# [2] 연산자 및 로직 함수
def analyze_lead_score(score):
    """오늘 배운 비교 및 논리 연산자 활용"""
    print(f"\n--- [Step 2] 연산자 활용 분석 ---")
    is_high_quality = score > 80  # 비교 연산자
    is_hot_lead = (score >= 90) or (score == 100)  # 논리 연산자
    
    print(f"현재 점수: {score}")
    print(f"고품질 리드인가? {is_high_quality}")
    print(f"즉시 컨택 대상인가? {is_hot_lead}")

# [3] Pandas 데이터 구조 함수
def demonstrate_pandas_series():
    """오늘 배운 Pandas Series 생성 3가지 방식"""
    print(f"\n--- [Step 3] Pandas Series 생성 ---")
    if not HAS_LIBS:
        print("Pandas가 설치되지 않아 이 단계를 건너뜁니다.")
        return

    # 리스트로 생성 (인덱스 자동)
    s_list = pd.Series([1000, 2000, 3000], name="Sales")
    
    # 딕셔너리로 생성 (Key가 인덱스가 됨)
    s_dict = pd.Series({'삼성': 75000, 'LG': 420000}, name="Stock")
    
    # 튜플로 생성
    s_tuple = pd.Series((1.5, 2.5, 3.5), index=['a', 'b', 'c'])

    print("리스트 기반 시리즈:\n", s_list)
    print("딕셔너리 기반 시리즈(기업주가):\n", s_dict)

# [4] 메인 실행부
def main():
    print("main() 함수를 시작합니다.")
    
    # 라이브러리 설치 여부 출력
    if HAS_LIBS:
        print("✅ NumPy와 Pandas가 정상적으로 로드되었습니다.")
    else:
        print("❌ 라이브러리가 없습니다. 'pip install numpy pandas'를 실행하세요.")

    # 분석 로직 실행
    analyze_lead_score(95)
    
    # 데이터 구조 실습 실행
    demonstrate_pandas_series()

# ---------------------------------------------------------
# [5] Python 실행 흐름 제어
# ---------------------------------------------------------
print("Start!")  # 프로그램 시작 시 무조건 실행

if __name__ == "__main__":
    # 이 파일이 직접 실행될 때만 main()을 호출합니다.
    # 다른 파일에서 이 파일을 import할 때는 실행되지 않습니다.
    main()

print("End!")    # 프로그램 종료 시 무조건 실행