# [미션] 파이썬 연산자의 종류 조사 및 예제 구현
# 파일명: python_operators_mission.py
# 목적: 파이썬에서 사용하는 주요 연산자 7종을 정리하고 실제 작동 예시를 확인합니다.

def run_mission():
    print("=== [1] 산술 연산자 (Arithmetic Operators) ===")
    # 산술적인 계산을 수행할 때 사용
    a, b = 10, 3
    print(f"{a} + {b} = {a + b}")    # 더하기
    print(f"{a} - {b} = {a - b}")    # 빼기
    print(f"{a} * {b} = {a * b}")    # 곱하기
    print(f"{a} / {b} = {a / b}")    # 나누기 (실수)
    print(f"{a} // {b} = {a // b}")  # 몫 (정수)
    print(f"{a} % {b} = {a % b}")    # 나머지
    print(f"{a} ** {b} = {a ** b}")  # 거듭제곱
    print()

    print("=== [2] 비교 연산자 (Comparison Operators) ===")
    # 값의 크기를 비교하여 True/False 반환
    x, y = 5, 10
    print(f"{x} == {y} : {x == y}")  # 같음
    print(f"{x} != {y} : {x != y}")  # 다름
    print(f"{x} > {y}  : {x > y}")   # 큼
    print(f"{x} <= {y} : {x <= y}")  # 작거나 같음
    print()

    print("=== [3] 할당 연산자 (Assignment Operators) ===")
    # 변수에 값을 대입하거나 연산 후 결과를 다시 저장
    c = 10
    print(f"초기 c: {c}")
    c += 5  # c = c + 5
    print(f"c += 5 실행 후: {c}")
    c *= 2  # c = c * 2
    print(f"c *= 2 실행 후: {c}")
    print()

    print("=== [4] 논리 연산자 (Logical Operators) ===")
    # 조건을 결합 (and, or, not)
    p, q = True, False
    print(f"{p} and {q} : {p and q}")  # 둘 다 참일 때 참
    print(f"{p} or {q}  : {p or q}")   # 하나라도 참이면 참
    print(f"not {p}     : {not p}")     # 상태 반전
    print()

    print("=== [5] 비트 연산자 (Bitwise Operators) ===")
    # 비트 단위로 연산 (메모리 효율 및 하드웨어 제어 시 활용)
    m, n = 10, 3  # (10: 1010, 3: 0011)
    print(f"{m} & {n}  : {m & n}")    # 비트 AND (0010 -> 2)
    print(f"{m} | {n}  : {m | n}")    # 비트 OR  (1011 -> 11)
    print()

    print("=== [6] 멤버십 연산자 (Membership Operators) ===")
    # 특정 값이 리스트 등에 포함되어 있는지 확인
    # 안티그래비티 프로젝트에서 기술 스택 포함 여부를 체크할 때 유용합니다.
    tech_stack = ['Hadoop', 'Tableau', 'TensorFlow']
    print(f"'Hadoop' in tech_stack     : {'Hadoop' in tech_stack}")
    print(f"'Python' not in tech_stack : {'Python' not in tech_stack}")
    print()

    print("=== [7] 식별 연산자 (Identity Operators) ===")
    # 두 객체가 메모리상 동일한 객체인지 확인 (is, is not)
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    list_c = list_a
    print(f"list_a is list_b     : {list_a is list_b}")     # 값은 같지만 다른 객체
    print(f"list_a is list_c     : {list_a is list_c}")     # 같은 메모리 주소 참조
    print()

if __name__ == '__main__':
    run_mission()