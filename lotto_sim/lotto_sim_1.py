#한 단계씩 만들어 나가깅~
'''
먼저 lotto_sim_1.py 파일의 generate_numbers() 함수를 작성하세요.
이 함수는 파라미터로 정수 n을 받습니다. 무작위로 1과 45 사이의 서로 다른 번호 n개를 뽑고,
그 번호들이 담긴 리스트를 리턴합니다.
참고로 이 함수는 참가자의 번호를 뽑는 데에도 쓰이고, 보너스를 포함한 당첨 번호 7개를 뽑는 데에도 쓰입니다.
'''

from random import randint

def generate_numbers(geN):
    numbers = []

    while len(numbers) < geN:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers

print(generate_numbers(6))
