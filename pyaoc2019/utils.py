import time
from collections import deque
from contextlib import contextmanager
from itertools import islice
from pathlib import Path

__author__ = 'acushner'

from typing import Any, Iterable

path = Path('/Users/acushner/software/pyaoc2019/pyaoc2019/inputs')


def read_file(name):
    if isinstance(name, int):
        name = f'{name:02d}'
    with open(path / name) as f:
        return list(map(str.strip, f.readlines()))


@contextmanager
def localtimer():
    start = time.perf_counter()
    yield
    print('func took', time.perf_counter() - start)


def chunks(it: Iterable[Any], size):
    it = iter(it)
    yield from iter(lambda: list(islice(it, size)), [])


def __main():
    pass


if __name__ == '__main__':
    __main()


class Atom:
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self._val

    @value.setter
    def value(self, val):
        self._val = val

    def __str__(self):
        return f'Atom({self._val})'

    __repr__ = __str__


class classproperty:
    def __init__(self, f):
        self._get = f
        self._set = None

    def __get__(self, instance, cls):
        return self._get(cls)

    def setter(self, f):
        self._set = f
        return self

    def __set__(self, instance, value):
        if not self._set:
            raise AttributeError(f"can't set attribute {self._get.__name__}")
        self._set(type(instance), value)


def exhaust(iterable):
    deque(iterable, maxlen=0)
