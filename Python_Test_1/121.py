with open('vocabulary.txt', 'w', encoding='utf-8') as f:
    while True:
        enW = input('영어 단어를 입력하세요: ')
        if enW == 'q':
            break

        koW= input('한국어 뜻을 입력하세요: ')
        if koW == 'q':
            break

        f.write('{}: {}\n'.format(enW, koW))
