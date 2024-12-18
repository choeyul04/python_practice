with open('vocabulary.txt', 'r', encoding='utf-8') as f:
    for i in f:
        data = i.strip().split(": ")
        enW = data[0]
        koW = data[1]

        while True:
            quest = input(koW + ': ')
            if enW == quest:
                print("맞았습니다!\n")
                break
            else:
                print('틀렸습니다 다시 입력해주세요.\n')
                continue




