import random

vocab = {}
with open('vocabulary.txt', 'r', encoding='utf-8') as f:
    for line in f:
        data = line.strip().split(": ")
        enW, koW = data[0], data[1]
        vocab[enW] = koW

keys = list(vocab.keys())

while True:
    idx = random.randint(0, len(keys) - 1)
    enW = keys[idx]
    koW = vocab[enW]

    quest = input(f"{koW}: ")

    if quest == 'q':
        break
    if quest == enW:
        print("정답입니다!\n")
    else:
        print(f"틀렸습니다. 정답은 {enW}입니다.\n")
