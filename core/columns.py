import psycopg2
import psycopg2.extras
import pandas as pd
import boto
import StringIO
import datetime
import random
import string
import time
import traceback


def numeric(rows, cardinality, has_nulls):
    pass


def dimension(rows, cardinality, has_nulls):
    pass


def boolean(rows, cardinality, has_nulls):
    pass


def ds(rows, cardinality, has_nulls):
    pass

"""
Build a graph of data model and then automatically the data will be populated
Define table class and it's columns, then define relationship between the objects
Then define a graph and add all classes to it.
define the destination for the data and it will be written there.
Then run the graph and it will generate the data rapidly and then insert it into the corresponding place
"""
"""
Table types:
Fact table, dimension table
if fact tables, will have a timestamp and then corresponding date time
"""


class Graph(object):

    def add_table(self):
        pass


class Table(object):

    def add_columns(self, cols):
        pass

    def add_column(self, col):
        pass


class Column(object):

    def __init__(self):
        pass


class Writer(object):

    def __init__(self, *args, **kwargs):
        pass

    def write(self, table, append=False):
        pass
