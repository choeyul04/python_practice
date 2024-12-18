#3 단계으이
#두 리스트 생성 후 겹치는 번호 개수 출려끄~

def counting_match_num(num, winning_num):
    cnt = 0
    for number in num:
        if number in winning_num:
            cnt += 1
    return cnt

#겹치는 숫자 맞춰볼 예시 리스트
print(counting_match_num([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(counting_match_num([2, 7, 11, 14, 25, 40], [14]))
