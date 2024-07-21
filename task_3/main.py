from timeit import timeit
from pathlib import Path
from tabulate import tabulate

from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search

# Отримуємо абсолютні шляхи до файлів
base_path = Path(__file__).parent
article_1_path = base_path / 'article_1.txt'
article_2_path = base_path / 'article_2.txt'

# Функція для зчитування файлів
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Завантаження статей
article_1 = read_file(article_1_path)
article_2 = read_file(article_2_path)

# Підрядки для тестування
patterns = ["Стаття", "Неіснуючий підрядок для тестування"]

# Функція для вимірювання часу виконання алгоритмів
def measure_time(algorithm, text, pattern):
    return timeit(lambda: algorithm(text, pattern), number=1000)

# Вимірювання часу для кожного алгоритму та підрядка
results = {}
for pattern in patterns:
    results[pattern] = {
        "Boyer-Moore": (measure_time(boyer_moore_search, article_1, pattern), measure_time(boyer_moore_search, article_2, pattern)),
        "KMP": (measure_time(kmp_search, article_1, pattern), measure_time(kmp_search, article_2, pattern)),
        "Rabin-Karp": (measure_time(rabin_karp_search, article_1, pattern), measure_time(rabin_karp_search, article_2, pattern)),
    }

# Формування таблиці результатів
table_data = []
for pattern, result in results.items():
    for algo, times in result.items():
        table_data.append([pattern, algo, f"{times[0]:.6f}", f"{times[1]:.6f}"])

headers = ["Підрядок", "Алгоритм", "Стаття 1 (сек)", "Стаття 2 (сек)"]
table = tabulate(table_data, headers, tablefmt="github")

print(table)