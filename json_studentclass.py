import json

class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def info(self):
        return '姓名：{}\n年龄：{}岁\n成绩: {} 分'.format(self.name,self.age,self.score)
    
a=Student('吴婕',20,99)
print(a.info())

print('--------------------------')

json_str='{"age": 22,"score": 88,"name": "刘峥"}'
b=json.loads(json_str,object_hook=lambda x: Student(x['name'],x['age'],x['score']))
print(b.info())