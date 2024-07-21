from timeit import timeit
def read_file(file_path):
    with open(file_path, 'r', encoding='cp1251') as file:
        return file.read()
    
def measure_search_time(func, text, pattern):
    setup_code = f'''from __main__ import {func.__name__}'''
    stmt = f'''{func.__name__}({text}, {pattern})'''
    return timeit(smt, setup=setup_code, globals={'text': text, 'pattern': pattern})