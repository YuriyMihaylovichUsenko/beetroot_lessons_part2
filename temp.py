from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Pair:
    key: Any
    value: Any


BLANK = object()


class HashTable:

    def __init__(self, capacity):
        self._pairs = capacity * [BLANK]
        self.cache_ind = []

    def __len__(self):
        return len(self._pairs)

    def __setitem__(self, key, value):
        ind = self._index(key)
        if self._pairs[ind] is None:
            self._pairs[ind] = Pair(key, value)
        else:
            next_ind = self.new_index(ind)
            while self._pairs[next_ind]:
                next_ind = self.new_index(next_ind)
            self._pairs[next_ind] = Pair(key, value)

    def __getitem__(self, key):
        start_ind = self._index(key)
        data = None
        stop = False
        found = False
        position = start_ind
        while self._pairs[position] is not None and not found and not stop:
            if self._pairs[position].key == key:
                found = True
                data = self._pairs[position].value
            else:
                position = self.new_index(position)
                if position == start_ind:
                    stop = True
        return data

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __delitem__(self, key):
        if key in self:
            self[key] = BLANK
        else:
            raise KeyError(key)

    def __iter__(self):
        yield from self._pairs

    def _index(self, key):
        res = hash(key) % len(self)
        return res

    def new_index(self, ind):
        return (ind + 1) % len(self)



    @property
    def pairs(self):
        return {pair for pair in self._pairs}


table = HashTable(3)

# print(len(table))

table['Oleg'] = 'Senior Python developer'
table['Yurii'] = 'Team lead'
table['Tetiana'] = 'Data scientist'

print(table['Oleg'])
print(table['Yurii'])
print(table['Tetiana'])

print('Lev' in table)

print(table.get('Yurii'))

for i in table:
    print(i)

print(table.pairs)