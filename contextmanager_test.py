from contextlib import contextmanager
#我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
@contextmanager
def tag(name):
    print("<%s>" %name)
    yield
    print("</%s>" %name)
with tag("h1"):
    print("wujie")
    print("love")
    print("LiuZheng")
#代码执行顺序是：
#1.with语句首先执行yield之前的语句，因此打印出<h1>；
#2.yield调用会执行with语句内部的所有语句，因此打印出print里面的内容；
#3.最后执行yield之后的语句，打印出</h1>。
#执行结果：
""" <h1>
wujie
love
LiuZheng
</h1> """