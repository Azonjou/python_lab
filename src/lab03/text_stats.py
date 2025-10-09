import sys
from text import *

def text_info(table: bool = True):
    text = sys.stdin.readline().strip()
    words = sorted(tokenize(normalize(text)), key=len, reverse=True)
    print(f"Всего слов: {len(tokenize(normalize(text)))}")
    print(f"Уникальных слов: {len(set(tokenize(normalize(text))))}")
    print("Топ-5:")
    if table:
        print("слово" + " " * (len(max("Слово", max(words), key=len))-len(min("Слово", max(words), key=len))+1) + "|" + " частота")
        print("-" * (len(max("Слово", max(words), key=len))+1+len("|" + " частота")))
        for w in count_freq(tokenize(normalize(text))):
            word = w.ljust(len(max("Слово", max(words), key=len))+1)
            print(f"{word}| {count_freq(tokenize(normalize(text))).get(w)}")
    else:
        for w in count_freq(tokenize(normalize(text))):
            print(f"{w}:{count_freq(tokenize(normalize(text))).get(w)}")

text_info(True)