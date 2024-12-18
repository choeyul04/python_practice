import random

RdNum = random.randint(1,20)
cnt = 4

while cnt > 0:
    chance = int(input(f'기회가 {cnt}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:'))
    if chance == RdNum:
        print(f'축하합니다. {5-cnt}번 만에 숫자를 맞히셨습니다.')
        break
    elif chance > 20:
        print('올바르지 않은 값입니다. 1-20 사이의 정수를 입력해주세요')
    elif chance > RdNum:
        print('Down')
        cnt -= 1
    elif chance < RdNum:
        print('Up')
        cnt -= 1
    if cnt == 0 :
        print(f'아쉽군요. 정답은 {RdNum}입니다. 다시 도전해주세요')