import timeit
from typing import Callable
from tabulate import tabulate

from bm import boyer_moore_search
from kmp import kmp_search
from rabina import rabin_karp_search


def read_file(filename_1, filename_2):
    with open(filename_1, "r", encoding="cp1251") as f1, open(
        filename_2, "r", encoding="cp1251"
    ) as f2:
        text_1 = f1.read()
        text_2 = f2.read()
    text = text_1 + text_2

    return text_1, text_2


def benchmark(func: Callable, text_: str, pattern_: str):
    setup_code = f"from __main__ import {func.__name__}"
    stmt = f"{func.__name__}(text, pattern)"
    return timeit.timeit(
        stmt=stmt,
        setup=setup_code,
        globals={"text": text_, "pattern": pattern_},
        number=100,
    )


if __name__ == "__main__":
    text_1, text_2 = read_file("article_1.txt", "article_2.txt")
    text_list = [
        text_1,
        text_2,
        text_1 + text_2,
    ]
    text_len = [len(text_list[0]), len(text_list[1]), len(text_list[2])]
    real_pattern = "різних структур даних"
    fake_pattern = "такого точно не існує"

    table = []
    results = []
    for i, text in enumerate(text_list):
        for pattern in (real_pattern, fake_pattern):
            time = benchmark(boyer_moore_search, text, pattern)
            results.append(
                (
                    boyer_moore_search.__name__,
                    pattern,
                    round(time, 10),
                    f"article_{i + 1:<}",
                    text_len[i],
                )
            )
            time = benchmark(kmp_search, text, pattern)
            results.append(
                (
                    kmp_search.__name__,
                    pattern,
                    round(time, 10),
                    f"article_{i + 1:<}",
                    text_len[i],
                )
            )
            time = benchmark(rabin_karp_search, text, pattern)
            results.append(
                (
                    rabin_karp_search.__name__,
                    pattern,
                    round(time, 10),
                    f"article_{i + 1:<}",
                    text_len[i],
                )
            )

    table.append(
        [
            "Алгоритм",
            "Підрядок",
            "Час виконання, сек",
            "Назва тексту",
            "Кількість символів в тексті",
        ]
    )
    for result in results:
        table.append([result[0], result[1], result[2], result[3], result[4]])

    print(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))
