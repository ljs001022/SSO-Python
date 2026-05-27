class RadarScanner:
    def __init__(self, min_score):
        # 1. 최소 기준 점수를 인스턴스 변수로 저장하세요.
        self.score = min_score

    def process_data(self, companies):
        result_leads = []
        
        # 2. 반복문을 사용하여 companies 리스트를 순회하세요.
        for comp in companies:
            score = comp.get('score')
            
            # 3. isinstance를 사용하여 score가 숫자(int, float)인지 확인하고
            #    아니라면 continue 하세요.
            if isinstance(score, (int,float)) :
                pass
            # 4. score가 100을 넘으면 break 하세요.
            
            # 5. score가 min_score 이상인 경우에만 등급(grade)을 판별하여
            #    result_leads 리스트에 append 하세요.
            pass

        return result_leads

# --- 테스트 코드 (수정하지 마세요) ---
# 샘플 데이터
data = [
    {'name': '삼성전자', 'score': 95},
    {'name': 'LG에너지솔루션', 'score': 82},
    {'name': '현대자동차', 'score': 'N/A'}, # 문자열 (건너뛰어야 함)
    {'name': 'SK하이닉스', 'score': None},  # None (건너뛰어야 함)
    {'name': '스타트업A', 'score': 50},      # 기준 미달 (제외되어야 함)
    {'name': '오류기업', 'score': 150}      # 100 초과 (여기서 멈춰야 함)
]

scanner = RadarScanner(min_score=70)
final_leads = scanner.process_data(data)

print(f"탐지된 유망 리드: {final_leads}")