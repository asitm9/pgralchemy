__author__ = 'asitm9'

from sqlalchemy.types import UserDefinedType, Integer
from sqlalchemy.sql import func
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql.base import ischema_names


class CostResult(object):

    def __init__(self, *args, **kwargs):
        self.seq = kwargs['seq']
        self.id1 = kwargs['id1']
        self.id2 = kwargs['id2']
        self.cost = kwargs['cost']

ischema_names['cost_result'] = CostResult
