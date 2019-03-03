from html.parser import HTMLParser
from urllib import request

class MyHtmlParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)#预定义各个标志位
        self.is_title=False  #会议名称
        self.is_location=False #会议地址
        self.is_time=False #会议时间
        self.times=[]
        self.event={}
        self.eventlist=[]
    #遇到开始标签时，设置各个标志位为True
    def handle_starttag(self,tag,attrs):
        if('class','event-title')in attrs:
            self.is_title=True
        if('class','event-location')in attrs:
            self.is_location=True
        if tag=='time':
            self.is_time=True
    
    #遇到结束标签时，设置各个标志位为False，以便下一次的解析
    def handle_endtag(self,tag):
        if tag=='h3':
            self.is_title=False
        if tag=='span':
            self.is_location=False
        if tag=='time':
            #完成event[time]属性的组装
            self.event['time']=' '.join(self.times)
            #重置数据
            self.is_time=False
            self.times=[]
        #当遇到li结束标签时，将event对象放入eventlist
        if tag=='li':
            #如果event对象不为空，将event对象放入eventlist（去掉无用的li标签的解析）
            if self.event:
                self.eventlist.append(self.event)
                #同时初始化event
                self.event={}
    

    #解析数据
    #将各个数据组装成一个event（dict）
    def handle_data(self,data):
        if self.is_title:
            self.event['title']=data
        if self.is_location:
            self.event['location']=data
        if self.is_time:
            self.times.append(data)
    
    #统一打印eventlist对象
    def showEvent(self):
        print(self.eventlist)
        for event in self.eventlist:
            print('title:',event['title'])
            print('location:',event['location'])
            print('time:',event['time'])
            print('---------------------------------')

with request.urlopen('https://www.python.org/events/python-events/') as f:
    data=f.read()
    print(data)
parser=MyHtmlParser()
parser.feed(data.decode('gbk'))
parser.showEvent()