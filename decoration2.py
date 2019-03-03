import time, functools  #引入time，functools函数

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()	#函数起始运行
        result = fn(*args, **kw)
        end = time.time()	#函数结束运行
        print('%s executed in %s ms' % (fn.__name__, (end - start) * 1000))	#打印函数名和运行时间
        return result
    return wrapper


#测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('Fail')
elif s != 7986:
    print('Fail')