# -*- coding:utf-8 -*-
from sqlalchemy import Column,String,create_engine,ForeignKey,Integer
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

#一对多，每个User有多个Score

#定义对象类指向表
Base=declarative_base()
class User(Base):
    #表的名字：
    __tablename__='user1'

    #表的结构：
    id=Column(String(20),primary_key=True)
    name=Column(String(20))
    #一对多：
    score=relationship('Score')
    def __str__(self):
        return 'User id:%d,name:%s,score:%s'%(self.id,self.name,self.score)
    __repr__=__str__

class Score(Base):
    __tablename__='score'
    id=Column(String(20),primary_key=True)
    chinese_score=Column(Integer)
    math_score=Column(Integer)
    user1_id=Column(Integer,ForeignKey('user1.id'))
    def __str__(self):
        return 'chinese_score=%d,math_score=%d'%(self.chinese_score,self.math_score)
    __reps__=__str__

#create_engine用来初始化数据库连接
#'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine=create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
DBSession=sessionmaker(bind=engine)
Base.metadata.create_all(engine)

#创建对象session
session=DBSession()
#创建表user以及带外键的表score
#session.execute('create table user1(id int primary key,name varchar(20))')
#session.execute('create table score(id int primary key,chinese_score int,math_score int,user1_id int,constraint id_fk foreign key(user1_id)references user1(id))')

#插入表值
session.merge(User(id=1,name='Ada'))
session.merge(User(id=2,name='Bob'))
session.merge(User(id=3,name='Mike'))
session.merge(Score(id=1,chinese_score=98,math_score=100,user1_id=1))
session.merge(Score(id=3,chinese_score=85,math_score=78,user1_id=2))
session.merge(Score(id=5,chinese_score=90,math_score=91,user1_id=3))

#提交，关闭
session.commit()
session.close()

session=DBSession()
user1=session.query(User).all()
score=session.query(Score).all()
#输入表格内容并关闭表：
for info in user1:
    print(info)
for info in score:
    print('user_id',info.id)
    print('Chinese_Score:',info.chinese_score)
session.close()