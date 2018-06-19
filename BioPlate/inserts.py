from typing import (
    Dict,
    List,
    Tuple,
    Optional,
    Union,
    Any,
    overload,
    Sequence,
    Generator,
)

from collections import OrderedDict

import numpy as np

from BioPlate.array import BioPlateArray
from BioPlate.manipulation import BioPlateManipulation
from BioPlate.stack import BioPlateStack
from BioPlate.matrix import BioPlateMatrix


class BioPlateInserts(BioPlateArray, BioPlateManipulation):
    def __new__(cls, *args, **kwargs):
        return BioPlateArray.__new__(cls, *args, inserts=True)

    def __init__(self, *args, **kwargs):
        self.ID = id(self)

    def __add__(self, other):
        if isinstance(other, BioPlateStack):
            newstack = BioPlateArray._get_stack_in_cache(other.ID)
            newstack = [self.ID] + newstack
        else:
            newstack = [self.ID, other.ID]
        newstack = list(OrderedDict.fromkeys(newstack))
        return BioPlateStack(newstack)

    def __getitem__(self, index):
        if isinstance(index, tuple):
            if isinstance(index[1], str):
                ind = {"top" : 0, "bot" : 1, "0" : 0, "1":1, 0 : 0, 1 : 1}
                plt = self[ind[index[0]]]
                if isinstance(index[1], str):
                    well = BioPlateMatrix(index[1])
                    return plt[well.row, well.column]
        return super(BioPlateInserts, self).__getitem__(index)
            
    def __setitem__(self, index, value):
        if isinstance(index, tuple):
            if isinstance(index[1], str):
                ind = {"top" : 0, "bot" : 1, 0 : 0, 1:1}
                plt = self[ind[index[0]]]
                if isinstance(index[1], str):
                    well = BioPlateMatrix(index[1])
                    plt[index[1]] = value
                    if isinstance(value, list):
                        plate_shape = plt[well.row, well.column].shape
                        len_plate_shape = len(plate_shape)
                        if len_plate_shape > 1:
                            if well.pos == "R":
                                resh_val = np.reshape(value, (plate_shape[0], 1))
                            else:
                                resh_val = value
                        plt[well.row, well.column] = resh_val
                        return 
                    else:
                        plt[well.row, well.column][: len(value)] = value
                        return 
        return super(BioPlateInserts, self).__setitem__(index, value)

    @property
    def top(self):
        return self[0]

    @property
    def bot(self):
        return self[1]

    def force_position(func):
        def wrapper(self, *args, **kwargs):
            if len(self.shape) > 2:
                raise ValueError(
                    "You didn't select a part of the plate, either top or bot'"
                )
            else:
                return func(self, *args, **kwargs)

        return wrapper

    @force_position
    def set(self, *args, **kwargs):
        super().set(*args, **kwargs)
        return self

    @force_position
    def get(self, *args):
        return super().get(*args)
