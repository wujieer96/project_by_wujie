#正确实现了上下文管理的with语句
#方法一：
""" class Query(object):
    def __init__(self,name):
        self.name=name
    def __enter__(self):
        print('Begin')
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type:
            print('error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...'%self.name)

with Query('WuJie')as q:
    q.query() """

#方法二
from contextlib import contextmanager

class Query(object):
    def __init__(self,name):
        self.name=name
    def query(self):
        print('Query info about %s...'%self.name)
#@contextmanager这个decorator接受一个generator，
#用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了
@contextmanager
def create_query(name):
    print('Begin')
    q=Query(name)
    yield q
    print('End')
with create_query('LiuZheng')as q:
    q.query()
