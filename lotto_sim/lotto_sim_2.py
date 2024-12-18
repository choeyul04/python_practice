#2 단계ㅔㅔㅇ
#당첨이랑 보너스 번호 도출 해내긩

from random import randint

def generate_numbers(geN):
    numbers = []

    while len(numbers) < geN:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers

def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

print((generate_numbers(6)))
print(draw_winning_numbers())
