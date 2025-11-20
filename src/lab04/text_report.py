from collections import Counter
import csv
from pathlib import Path
from typing import Iterable, Sequence
import argparse
from src.lab03.text_stats import text_info


# Ваши существующие функции
def frequencies_from_text(text: str) -> dict[str, int]:
    from text import normalize, tokenize

    tokens = tokenize(normalize(text))
    return Counter(tokens)


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def write_csv(
    rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


def main():
    parser = argparse.ArgumentParser(description="Анализ частоты слов")
    parser.add_argument("--input", "-i", default="../data/lab04/input.txt")
    parser.add_argument("--output", "-o", default="../data/lab04/report.csv")
    parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    # Обработка
    with open(args.input, "r", encoding="utf-8") as f:
        text = f.read()
        text_info(text, False)

    freq = frequencies_from_text(text)
    sorted_counts = sorted_word_counts(freq)

    # Сохраняем CSV
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    write_csv(sorted_counts, args.output, header=("word", "count"))


if __name__ == "__main__":
    main()
# python src/lab04/text_report.py --input data/input.txt --output data/report.csv
