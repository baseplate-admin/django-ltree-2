import string
from itertools import product

from django_ltree.fields import PathValue
import math


class PathGenerator(object):
    # _default_label_size = 6  # Postgres limits this to 256

    def __init__(self, prefix=None, skip=None):
        combinations = string.digits + string.ascii_letters

        self.skip_paths = [] if skip is None else skip[:]
        self.path_prefix = prefix if prefix else []
        self.product_iterator = product(
            combinations,
            repeat=self.guess_the_label_size(
                path_size=len(self.skip_paths), combination_size=len(combinations)
            ),
        )

    def __iter__(self):
        return self

    def __next__(self):
        for val in self.product_iterator:
            label = "".join(val)
            path = PathValue(self.path_prefix + [label])
            if path not in self.skip_paths:
                return path

    next = __next__

    @staticmethod
    def guess_the_label_size(path_size: int, combination_size: int):
        if path_size == 0:
            return 1

        # The theoritical limit for this at the time of writing is 2_538_557_185_841_324_496 (python 3.12.2)
        calculated_path_size = +0
        # The theoritical limit for this at the time of writing is 32 (python 3.12.2)
        label_size = 0

        # THIS IS AN VERY IMPORTANT CHECK
        last = 0

        while calculated_path_size < path_size:
            possible_cominations = math.comb(combination_size, label_size)

            if last > possible_cominations:
                raise ValueError("We approached the limit of `math.comb`")

            last = possible_cominations
            calculated_path_size += possible_cominations
            label_size += 1

        return label_size
