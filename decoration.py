#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import time
import types


def log(obj=None):
    prefix = ''

    def decorator(func):
        functools.wraps(func)

        def wrapper(*argv, **kw):
            print("{0}begin call {1}".format(prefix, func.__name__))
            ret = func(*argv, **kw)
            print("{0}end call {1}".format(prefix, func.__name__))
            return ret
        return wrapper

    if isinstance(obj, types.BuiltinFunctionType) or isinstance(obj, types.FunctionType):
        return decorator(obj)
    elif obj is None:
        return decorator
    else:
        prefix = obj + ' '
        return decorator


@log
def f1(x, y):
    print (x, y)


@log('execute')
def f2(x, y):
    print (x, y)


@log()
def f3(x, y):
    print (x, y)

f1(1,2)
f2(3,4)
f3(5,6)
