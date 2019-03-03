# Completed implementation of a queue ADT
class Queue:
   def __init__(self):
      self.items = []
   def is_empty(self):
      return self.items == []
   def enqueue(self, item):
      self.items.insert(0,item)
   def dequeue(self):
      return self.items.pop()#函数用于移除列表中的一个元素(默认最后一个元素),并且返回该元素的值
   def size(self):
      return len(self.items)

q = Queue()
q.enqueue('hello')
q.enqueue('dog')
print(q.items)
q.enqueue(3)
q.dequeue()#函数用于移除列表中的最后一个元素
print(q.items)



# Completed implementation of a deque ADT
#双向队列：左右两边都可以插入和删除的队列
class Deque:
   def __init__(self):
      self.items = []
   def is_empty(self):
      return self.items == []
   def add_front(self, item):#右端为front，左端为rear
       self.items.append(item)
   def add_rear(self, item):
      self.items.insert(0,item)
   def remove_front(self):#删除
      return self.items.pop()
   def remove_rear(self):
      return self.items.pop(0)
   def size(self):
      return len(self.items)

dq=Deque()
dq.add_front('dog')
dq.add_rear('cat')
print(dq.items)
dq.remove_front()#删除右端
dq.add_front('pig')
print(dq.items)