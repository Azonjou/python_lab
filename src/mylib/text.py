import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if "\\" in text:
        text = bytes(text, "utf-8").decode("unicode_escape")
    text = re.sub(
        r"[\x00-\x1F\x7F]+", " ", text
    )  # перебирает ASCII символы с кодами от 0 до 31
    text = (
        text.casefold() if casefold else text
    )  # функция casefold создаёт копию строки и преобразовывает све символы в нижний регистр
    # text = text.replace("\\r\\", " ")
    text = re.sub(r"\s+", " ", text.strip())
    text = text.replace("ё", "е") if yo2e else text
    return text


print(normalize("ПрИвЕт\\nМИр\\t"))


def tokenize(text: str) -> list[str]:
    allowed_chars = "a-zA-Zа-яёА-ЯЯЁ0-9- "
    text = re.sub(f"[^{allowed_chars}]", " ", text)
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text.split()


def count_freq(tokens: list[str]) -> dict[str, int]:
    counts = {}
    for tok in tokens:
        counts[tok] = (
            counts.get(tok, 0) + 1
        )  # функция задаёт ключу словаря значение, сначала считает их количество в словаре, а потом добавляет к нему 1 и сохраняет в словаре
    return counts


def top_n(freq: dict[str, int], n: int = 2) -> list[tuple[str, int]]:
    words = list(sorted(freq.items(), key=lambda x: (-x[1], x[0])))[:n]
    return words


# normalize
assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
assert normalize("ёжик, Ёлка") == "ежик, елка"
assert normalize("Hello\\r\\nWorld") == "hello world"
assert normalize("  двойные   пробелы  ") == "двойные пробелы"

# tokenize
assert tokenize("привет, мир!") == ["привет", "мир"]
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
assert tokenize("2025 год") == ["2025", "год"]
assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"]


# count_freq + top_n
freq = count_freq(["a", "b", "a", "c", "b", "a"])
assert freq == {"a": 3, "b": 2, "c": 1}
assert top_n(freq, 2) == [("a", 3), ("b", 2)]

# тай-брейк по слову при равной частоте
freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
assert top_n(freq2, 2) == [("aa", 2), ("bb", 2)]
