import numpy as np

# 1. 배열 차원 (Scalar ~ Tensor)
s = 75000                     # 0차원: 스칼라 (Scalar)
v = [10, 20, 30]              # 1차원: 벡터 (Vector)
m = [[1, 2], [3, 4]]          # 2차원: 행렬 (Matrix)
t = np.array([m, m])          # 3차원 이상: 텐서 (Tensor)
print(t)

# 2. 필수 자료구조
# 수정 가능(List), 수정 불가(Tuple), 중복 불가(Set), 키-값(Dict)[cite: 1]
user_list = ['admin', 'user']
pos_tuple = (126.97, 37.56)    # 좌표 등 불변 데이터에 사용[cite: 1]
unique_ids = {101, 102, 101}   # 결과는 {101, 102} (중복 제거)[cite: 1]
company_map = {'name': 'Samsung', 'score': 95} # 자바의 Map 대응[cite: 1]

# 3. 타입 캐스팅 (Casting)
# int: 소수점 버림 / str: 만능 변환 / bool: 빈 값 체크[cite: 1]
score_int = int(98.9)          # 98 (내림)[cite: 1]
status_str = str(True)         # "True"[cite: 1]
is_empty = bool([])            # False (빈 리스트, 0, None 등은 False)[cite: 1]

# 4. 인스턴스 검사 및 함수 구조
def process_data(data):
    # 자바의 'data instanceof String'과 동일[cite: 1]
    if isinstance(data, str):
        return data.strip()
    
    # 파이썬은 NULL 대신 None 사용[cite: 1]
    if data is None:
        return "No Data"
        
    return data

# 5. 실행 제어 (Main Entry)
if __name__ == "__main__":
    # 인스턴스 확인 테스트
    sample = "  Antigravity  "
    result = process_data(sample)
    
    print(f"Type: {type(result)}") # <class 'str'>[cite: 1]
    print(f"Result: {result}")
    
    # NumPy 배열(ndarray) 타입 확인[cite: 1]
    print(f"Is Tensor: {isinstance(t, np.ndarray)}") # True[cite: 1]

numberlist = []
answer = {}

def _func() :
    for x in range(10):
        a = 0
        for i in range(10):
            a += np.random.randint(low=0, high=2)
        answer = {'result' : a}
        numberlist.insert(x, answer)
_func()
print(numberlist)