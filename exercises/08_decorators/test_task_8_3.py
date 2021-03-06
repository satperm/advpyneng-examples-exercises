import time
import pytest
import task_8_3
import sys
sys.path.append('..')

from common_functions import check_function_exists, check_function_params


def test_func_created():
    '''Проверяем, что декоратор создан'''
    check_function_exists(task_8_3, 'add_verbose')


def test_add_verbose(capsys):
    @task_8_3.add_verbose
    def do_thing(a, b):
        return a + b

    return_value = do_thing(2, 3)
    # проверка базовой работы функции
    assert return_value == 5

def test_add_verbose_args(capsys):
    @task_8_3.add_verbose
    def do_thing(a, b):
        return a + b

    # должно выводиться сообщение
    return_value = do_thing(2, 3, verbose=True)
    correct_stdout = 'Позиционные аргументы'
    out, err = capsys.readouterr()
    assert out != '', "На stdout не выведена информация"
    assert correct_stdout in out, "На stdout не выведена информация про аргументы функции"


def test_add_verbose_kwargs(capsys):
    @task_8_3.add_verbose
    def do_thing(a, b):
        return a + b

    # должно выводиться сообщение
    return_value = do_thing(a=2, b=3, verbose=True)
    correct_stdout = 'Ключевые аргументы'
    out, err = capsys.readouterr()
    assert out != '', "На stdout не выведена информация"
    assert correct_stdout in out, "На stdout не выведена информация про аргументы функции"


def test_add_verbose_args_kwargs(capsys):
    @task_8_3.add_verbose
    def do_thing(a, b):
        return a + b

    # должно выводиться сообщение
    return_value = do_thing(2, b=3, verbose=True)
    stdout = 'Ключевые аргументы'
    out, err = capsys.readouterr()
    assert out != '', "На stdout не выведена информация"
    assert 'Позиционные аргументы' in out and 'Ключевые аргументы' in out, "На stdout не выведена информация про аргументы функции"
