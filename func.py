__author__ = 'asitm9'

from . import types
from sqlalchemy.sql import functions


class GenericFunction(functions.GenericFunction):

    def __init__(self, *args, **kwargs):
        expr = kwargs.pop('expr', None)
        if expr is not None:
            args = (expr,) + args
        functions.GenericFunction.__init__(self, *args, **kwargs)


_FUNCTIONS = [
    ('pgr_tsp', types.CostResult,
     'travelling salesman problem'
     )
]


for name, type_, doc in _FUNCTIONS:
    attributes = {'name': name}
    docs = []

    if type_ is not None:
        attributes['type'] = type_

    globals()[name] = type(name, (GenericFunction,), attributes)