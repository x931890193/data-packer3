# coding=utf-8
from .field import *
from . import field, checker, converter, container, constant, err

__title__ = 'data_packer3'
__version__ = '2.0.1'
__author__ = 'sato'
__license__ = 'MIT'


def run(src, dst, fields):
    """

    :param src:
    :type src:
    :param dst:
    :type dst:
    :param fields:
    :type fields: list[_IField]
    :return:
    :rtype:
    """

    for field in fields:
        field.run(src, dst)


class DataPacker(object):

    def __init__(self, fields):
        """

        :param fields:
        :type fields: list[_IField]
        """

        self.fields = fields

    def run(self, src, dst):
        run(src, dst, self.fields)
