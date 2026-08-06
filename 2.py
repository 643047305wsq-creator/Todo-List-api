# print(4)
# print(7//2)
# a=1
# b=2
# print(f"a比b大:{a>b}")
# print(False)
# a=12
# if a>11:
#     print(True)
#     print(1)
# if a>10:
#     print(False)
# print(f"{1+1}")
# a=int(input('''欢迎来到游乐园
# 请输入你的年龄：
#         '''))
# print(type(a))
# if a>=18:
#     print('''你已成年,游玩需要补票10元
# 祝你游玩愉快
#           ''')
# print('''nihao
#     wobuaho'''
#     )
# h=input("请输入你的身高:")
# if h>"120":
#     print("你的身高超出120cm,游玩需要购票10元")
# else:
#     print("你的身高未超出120cm,可以游玩")
# print("祝你游玩愉快")
# print(f"{int(1.3)}")
# a=int(input("输入猜想数字："))
# if int(input("第一次猜想数字:"))==a:
#     print(True)
# elif int(input("不对再猜一次："))==a:
#      print(True)
# elif int(input("不对再猜最后一次："))==a:
#     print(True)
# else :
#     print("sorry,全部猜错了,我想的是:10")
# import random
# a=random.randint(1,20)
# b=int(input("第一次猜想数字:"))
# if b==a:
#     print(True)
# else :
#     if b>a:
#         print("太大了")
#     else:
#         print("太小了")
#     b=int(input("第二次猜想数字:"))
#     if b==a:
#          print(True)
#     else :
#         if b>a:
#           print("太大了")
#         else:
#           print("太小了")
#         b=int(input("第三次猜想数字:"))
#         if b==a:
#            print(True)
#         else :
#            if b>a :
#              print("太大了")
#             else :
#              print("太小了")
#             print(a)
# import random
# a=random.randint(1,12)
# b=int(input("第一次猜想数字:"))
# if b==a:
#    print(True)
# else :
#    if b>a:
#       print("太大了")
#    else :
#       print("太小了")
#    b=int(input("第二次猜想数字:"))
#    if b==a:
#     print(True)
#    else :
#      if b>a:
#       print("太大了")
#      else :
#       print("太小了")
#      b=a
#      b=int(input("第三次猜想数字:"))       
#      if b==a:
#       print(True)
#      else :
#       if b>a:
#        print("太大了")
#       else :
#        print("太小了")
#      print(a)
# a=int(input("输入年龄"))
# if 6<=a<65:
#     print("年龄以满足,还需满足以下条件")
#     if input("是否为本地居民:")=="True":
#         print("你已满足条件,可以办证")
#     elif int(input("输入已交纳押金:"))>=100:
#         print("你已满足条件,可以办证")
#     else:
#         print("你只满足了年龄条件,无法办证")
# else:
#     print("未满足年龄条件,无法办证")
# a=1
# s=0
# while a<=100:
#     s=s+a
#     a=a+1
# print(s)
# import random
# a=random.randint(1,100)
# c=False
# d=0
# while c==False:
#     d+=1
#     b=int(input("输入猜测数字:"))
#     if b>a:
#         print("太大了")
#     else:
#         print("太小了")
#     print(f"你猜测了{d}次")
#     c=b==a
# print("恭喜你猜中了")
# print("jin",end='')
# print("li",end='')
# print(1,end='')
# print(2,end='')

# print("ni\thao")
# print("wof\tbu")
# i=9
# a=0
# while i>=1:
#     j=9
#     a+=1
#     while j>=a:
#         print(f"{j}*{i}={j*i}\t",end='')
#         j-=1
#     print()
#     i-=1
# i=9
# while i>=1:
#     j=1
#     while j<=i:
#         print(f"{j}*{i}={j*i}\t",end='')
#         j+=1
#     print()
#     i-=1
# i = 1
# while i <= 5:
#     # 第一步:打印前导空格,让图形居中
#     k = 0
#     while k < (5 - i) * 2:
#         print(" ", end='')
#         k += 1
    
#     # 第二步:打印递增数字 1 到 i
#     j = 1
#     while j <= i:
#         print(j, end=' ')
#         j += 1
    
#     # 第三步:打印递减数字 i-1 到 1
#     j = i - 1
#     while j >= 1:
#         print(j, end=' ')
#         j -= 1
    
#     print()  # 一行打印完,换行
#     i += 1
# i=4 
# a=2
# while i>=1:
#     k=1
#     while k<=a:
#         print(" ",end='') 
#         k+=1
#     b=1
#     while b<=i:
#         print(b,end=' ')    
#         b+=1
#     c=i-1
#     while c>=1:
#         print(c,end=' ')
#         c-=1
#     print()
#     i-=1
#     a+=2     
# for x in range(1,10):
#     for y in range(1,x+1):
#         print(f"{y}*{x}={y*x}\t",end='')
#     print() 
# m=10000
# while m>0:
#  for x in range(1,21):
#     import random
#     n=random.randint(1,10)
#     if n<5:
#         print(f"员工{x},绩效分{n},低于5,不发工资")
#         continue
#     else:
#         print(f"向员工{x}发放工资1000,账户还剩余{m-1000}")
#         m-=1000
#     if m==0:
#        print("工资发完了下个月领吧")
#        break
# def add(x,y):
#     a=x+y
#     print(f"{x}+{y}的结果是:{a}")
#     print("%d+%d=%d"%(x,y,x+y))
# b=add(1,2)    
# print(b)   
# balance=200
# name=input("请输入你的名字:")     
# def main():
#     print("----主菜单----")
#     print(f"{name},你好,欢迎来到黑马奶茶。请选择操作:")
#     print("查询余额\t[输入1]")
#     print("点单消费\t[输入2]")
#     print("充值\t\t[输入3]")
#     print("退出\t\t[输入4]")
#     c=int(input("请输入你的选择:"))
#     return c
# def check():
#     print("----查询余额----")
#     print(f"{name},你好,你的余额剩余:{balance}元")
# def order():
#     global balance
#     a=int(input("----点单消费----"))
#     if balance>a:
#       balance-=a
#       print(f"{name},你好,你消费{a}元成功")
#       print(f"{name},你好,你的余额剩余:{balance}元")
#     else:
#         print(f"余额不足")
# def save():
#     global balance
#     a=int(input("----充值----"))
#     balance+=a 
#     print(f"{name},你好,你充值{a}元成功")
#     print(f"{name},你好,你的余额剩余:{balance}元")
# while True:
#     d=main()
#     if d==1:
#         check()
#     elif d==2:
#         order()
#     elif d==3:
#         save()
#     else:
#         break
# book_count=50
# name=input("请输入姓名:")
# def main():
#     print("----主菜单----")
#     print(f"{name},你好,欢迎来到黑马图书馆。请选择操作:")
#     print("查询库存\t[输入1]")
#     print("借书\t\t[输入2]")
#     print("还书\t\t[输入3]")
#     print("退出\t\t[输入4]")
#     return int(input("请输入你的选择:"))
# def check(x):
#     if x:    
#      print("----查询库存----")
#     print(f"{name},你好,当前图书库剩余:{book_count}本")
# def lend(x):
#     global book_count
#     if book_count>x:  
#      book_count-=x
#      print(f"{name},你好,你借阅{x}本图书成功")
#      check(False)
# def back(x):
#    global book_count
#    book_count+=x
#    print(f"{name},你好,你归还{x}本图书成功")
#    check(False)
# while True:
#    d=main()
#    if d==1:
#       check(True)
#    elif d==2:
#       num=int(input("---借书---"))
#       lend(num)
#    elif d==3:
#       num=int(input("----还书----"))
#       back(num)
#    else:
#       print("退出")
#       break
# a=[21,25,21,23,21,20]
# a.append(31)
# b=[29,33,30]
# a.extend(b)
# d=a.pop(0)
# print(f"取出第一个元素是:{d}")
# e=a.pop(-1)
# print(f"取出最后一个元素是:{e}")
# c=a.index(31)
# print(f"元素31,在列表中的下标位置是:{c}")
# f=len(a)       
# print(f)
# a=[1,2,3,4,5,6,7,8,9,10]
# b=0
# c=[]
# while b<len(a):
#     d=a[b]
#     if d%2==0:
#          c.append(d)
#     b+=1
# print(c)
# for i in a:
#     if i%2==0:
#         c.append(i)
# print(c)       
# a=("周杰伦",11,["football","music"])
# b=["football","music"]
# print(a.index(11))
# print(f"学生的姓名是:{a[0]}")
# del a[2][0]
# a[2].append("coding")
# print(a) 
# a="itheima itcast boxuegu"
# print(f"有{a.count("it")}个it字符")
# c=a.replace(" ","|")
# print(c)
# b=c.split("|")
# print(f"将{c}进行分裂,得到的列表是:{b}")
# a=range(5)
# print(a)
# print(list(a))   
# a=[1,2,3,4,5]
# b=a[-1:-4:-1]
# print(b)
# a="万过薪月,员序程马黑来,nohtyp学"
# b=a[-10:-15:-1]
# print(b)
# c=a.split(",")
# d=c[1]
# print(d[-2::-1])
# e=d.strip("来")
# g=d.replace("来","")
# h=g[-1::-1]
# print(h)
# f=e[::-1]
# print(f)
# a=[1,2,1,2,3,4,3,4,5]
# b=set()
# for x in a:
#     if x not in b:    
#      b.add(x)
# print(b)
#  a={1,1,2}
# b={1,2,3}
# c=a.union(b) 
# print(c)
# a={"我":1,"它":2,"他":3}
# print(list(a.keys()))
# print(a["我"])
# a=[1]
# print(a,type(a))
# b=(1,)
# print(b,type(b))
# c="1"
# print(c,type(c))
# d=set()
# print(d,type(d))
# e={1}
# print(e,type(e))
# a={"王力宏":{"部门":"科技部","工资":3000,"级别":1},
#    "周杰伦":{"部门":"市场部","工资":5000,"级别":2},
#    "林俊杰":{"部门":"市场部","工资":7000,"级别":3},
#    "张学友":{"部门":"科技部","工资":4000,"级别":1} 
#    }
# print(f"全体员工当前信息如下:{a}")
# for x in a.keys():
#     if a[x]["级别"]==1:
#         a[x]["级别"]+=1
#         a[x]["工资"]+=1000
# print(f"级别为1的员工升职加薪后,员工信息如下:{a}")
# def a(x):
#     b=x(1,2)
#     print(b)
#     d=x(1,2)
#     print(d)


    
# def c(x,y):
#     return x+y
# a(c)
# a(lambda x,y:x+y)
# b=0
# a=["123","123","132"]
# for x in a:
#     c=x.count("1")
#     b+=c
# print(b)
# f=open("D:/test.txt","w",encoding="UTF-8")
# f.write("nihao")
# f.write("jinli")  
# try:
#       name
# except NameError as e:
#     print(e)
# except Exception as e:
#       print(e)
# import time
# print(1)
# time.sleep(5)
# print(5)
# from time import sleep
# print(1)
# sleep(5)
# print(5)
# from time import *
# from time import *
# print(1)
# sleep(5)
# print(5)
# from my_module import *
# sum(1,2)
# sum_2(1,2)
# my_module.sum(1,2)
# a="nihao,tahao.wohao"
# b=a.split(",",".")
# print(b)
# import json
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,LabelOpts
# f1=open("D:/数据可视化/日本.txt","r",encoding="UTF-8")
# f2=open("D:/数据可视化/美国-1.txt","r",encoding="UTF-8")
# f3=open("D:/数据可视化/印度.txt","r",encoding="UTF-8")
# a=f1.read()
# b=f2.read()
# c=f3.read()
# a=a.replace("jsonp_1629344292311_69436(","")
# b=b.replace("jsonp_1629344292311_69436(","")
# c=c.replace("jsonp_1629344292311_69436(","")
# a=a[:-1]
# b=b[:-1]
# c=c[:-1]
# a=json.loads(a)
# b=json.loads(b)
# c=json.loads(c)
# x=b["data"][0]["trend"]["updateDate"]
# y1=a["data"][0]["trend"]["list"][0]["data"]
# y2=b["data"][0]["trend"]["list"][0]["data"]
# y3=c["data"][0]["trend"]["list"][0]["data"]
# line=Line()
# line.add_xaxis(x)
# line.add_yaxis("日本确诊人数",y1,label_opts=LabelOpts(is_show=False))
# line.add_yaxis("美国确诊人数",y2,label_opts=LabelOpts(is_show=False))
# line.add_yaxis("印度确诊人数",y3,label_opts=LabelOpts(is_show=False))
# line.set_global_opts(
#     title_opts=TitleOpts(title="美日印三国确诊人数对比折线图",pos_left="center",pos_bottom="%1"),
#     legend_opts=LegendOpts(is_show=True),
#     toolbox_opts=ToolboxOpts(is_show=True),  
# )
# line.render()
# f1.close()
# f2.close()
# f3.close()
# import json
# from pyecharts.charts import Map
# from pyecharts.options import*
# f=open("D:/数据可视化/疫情-1.txt","r",encoding="UTF-8")
# f1=f.read()
# f.close()
# f1=json.loads(f1)
# a=[]
# f2=f1["data"]["areaTree"][0]["children"]
# for x in f2:
#     a.append((x["name"],x["total"]["confirm"]))
# print(a)
# map=Map()
# map.add("各省份确诊人数",a,"china")
# map.set_global_opts(
#     title_opts=TitleOpts(title="全国疫情地图",pos_left="center",pos_bottom="%1"),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {"min":10,"max":99,"label":"10-99人","color":"#FFFF00"},
#             {"min":100,"max":499,"label":"100-499人","color":"#FF8000"},
#             {"min":500,"max":999,"label":"500-999人","color":"#DF3A01"},
#             {"min":1000,"max":9999,"label":"1000-9999人","color":"#B40404"},
#             {"min":10000,"max":99999,"label":"10000-99999人","color":"#8A0808"}
#         ]
#     )
# )
# map.render("map.html")
# from pyecharts.charts import Bar,Timeline
# from pyecharts.options import *
# from pyecharts.globals import ThemeType
# with open("D:/数据可视化/1960-2019全球GDP数据.txt","r",encoding="UTF-8") as f:
#     f=f.readlines()
# f=f[:0:-1]
# d={}
# for x in f:
#     y=int(x.split(",")[0])
#     c=x.split(",")[1]
#     g=float(x.split(",")[2])
#     try:
#         d[y].append([c,g])
#     except KeyError:
#         d[y]=[]
#         d[y].append([c,g])
# timeline=Timeline({"theme":ThemeType.LIGHT})
# h=sorted(d.keys())
# for y in h:
#     k=sorted(d[y],key=lambda e:e[1],reverse=True)[:8]
#     x_d=[]
#     y_d=[]
#     for x in k:
#         x_d.append(x[0])
#         y_d.append(x[1]/100000000)
#     bar=Bar()
#     x_d.reverse()
#     y_d.reverse()
#     bar.add_xaxis(x_d)
#     bar.add_yaxis("GDP(亿)",y_d,label_opts=LabelOpts(position="right"))
#     bar.reversal_axis()
#     bar.set_global_opts(
#         title_opts=TitleOpts(title=f"{y}年全球前8GDP数据",pos_left="center",pos_top="30"),
#         legend_opts=LegendOpts(pos_top="1",pos_left="1")
#     )
#     timeline.add(bar,str(y))
# timeline.add_schema(
#     play_interval=1000,
#     is_timeline_show=True,
#     is_auto_play=True,
#     is_loop_play=True
# )
# timeline.render("1960-2019全球前8GDP数据.html")
# countries_gdp = [
#     ("美国", 51532.5, "北美洲"),
#     ("中国", 14791.34, "亚洲"),
#     ("日本", 3844.62, "亚洲"),
#     ("德国", 2135.78, "欧洲"),
#     ("印度", 6294.09, "亚洲"),
#     ("法国", 3433.2, "欧洲"),
# ]
# a=[x[0]for x in countries_gdp if x[1]>3000]
# print(a)
# b=(x[1]/10000 for x in countries_gdp)
# c=tuple(x[1]/10000 for x in countries_gdp)
# print(c)
# d={x[2]for x in countries_gdp}
# print(d)
# e={x[0]:x[2]for x in countries_gdp}
# print(e)
# records = [
#     ("亚洲", "中国"),
#     ("欧洲", "法国"),
#     ("亚洲", "日本"),
#     ("北美洲", "美国"),
#     ("欧洲", "德国"),
#     ("亚洲", "印度"),
#     ("北美洲", "加拿大"),
# ]
# a={}
# for x in records:
#     a.setdefault(x[0],[]).append(x[1])
# print(a)
# students = [
#     ("张三", 85, "三班"),
#     ("李四", 92, "一班"),
#     ("王五", 78, "二班"),
#     ("赵六", 92, "三班"),
#     ("孙七", 88, "一班"),
#     ("周八", 78, "二班"),
# ]
# e=sorted(students,key=lambda x :x[1],reverse=True)
# print(e)
# a=[x[0]for x in sorted(students,key=lambda x :x[1])]
# print(a)
# b=sorted(students,key=lambda x :x[1],reverse=True)[0][0]
# print(b)
# f={"一班":1,"二班":2,"三班":3}
# c=sorted(students,key=lambda x:(f[x[2]],-x[1]))
# print(c)
# a=lambda x:3
# print(a(0))
# def a():
#    return 3
# b=a()
# print(b)
# class student:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
# for i in range(1,11):
#     print(f"当前录入第{i}位学生信息,总共需录入10位学生信息")
#     a=input("请输入学生姓名:")
#     b=int(input("请输入学生年龄:"))
#     c=input("请输入学生地址:")
#     stu=student(a,b,c)
#     print(f"学生{i}信息录入完成,信息为【学生名字:{a},年龄:{b},地址:{c}】")
# class Phone:
#     def __init__(self,a):
#         self.__is_5g_enable=a
#     def call_by_5g(self):
#         self.__check_5g()
#         print("正在通话中")
#     def __check_5g(self):
#         if self.__is_5g_enable:
#             print("5g开启")
#         else:
#             print("5g关闭,使用4g网络")
# phone=Phone(input("请输入数据:\n"))
# phone.call_by_5g()
# a=1.256
# print(f"{a:.2f}")
# a:tuple[int]=(1,2,3,"nihao")
# print((1+2)==3)
# def main(x:list,y:tuple)->int:
#     return x+y
# print(main(1,2))
# from typing import Union
# a:list[Union[int,str]]=["nihao",1,2,3]
# def b(x:Union[int,str])->Union[int,str]:
#     pass
# b()
# class a:
#     def cold(self):
#         pass
#     def hot(self):
#         pass
#     def swing(self):
#         pass
# class b(a):
#     def cold(self):
#         print("格力制冷")
#     def hot(self):
#         print("格力制热")
#     def swing(self):
#         print("左右摆风")
# class c(a):
#     def cold(self):
#         print("小米制冷")
#     def hot(self):
#         print("小米制热")
#     def swing(self):
#         print("小米摆风")
# def d(e:a):
#     e.cold()
# B=b()
# C=c()
# d(B)
# d(C)
# a=[1,2,3]
# x=[1,2,3]
# b=a+x
# print(b)
# from pymysql import Connection
# conn=Connection(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="643047305+wsq",
#     autocommit=False
# )
# # print(conn.get_server_info())
# a=conn.cursor()
# conn.select_db("practice")
# # a.execute("create table test(id int,name varchar(10))")
# a.execute('''select age,count(*) from student where age > 33 
# group by age order by age desc limit 3
# ''')
# b=a.fetchall()
# print(b)
# for x in b:
#     print(x)
# a.execute("insert into student values(1,'张三',34,'男'),(2,'李',35,'男')")
# conn.commit()
# conn.close()
# print(len(range(5)))
# print(list(range(5)[:3]))
# from class_2 import C,D
# from pyecharts.options import *
# from pyecharts.charts import Bar
# from pyecharts.globals import ThemeType
# c=C("D:/数据可视化/2011年1月销售数据.txt")
# d=D("D:/数据可视化/2011年2月销售数据JSON.txt")
# a=c.read()
# b=d.read()
# f=a+b
# g={}
# for x in f:
#     g[x.data]=g.setdefault(x.data,0)+int(x.money)
# bar=Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
# bar.add_xaxis(list(g.keys()))
# bar.add_yaxis("销售额",list(g.values()),label_opts=LabelOpts(is_show=False))
# bar.set_global_opts(
#     title_opts=TitleOpts(title="每日销售额",pos_left="center",pos_top=30)
# )
# bar.render("每日销售额柱状图.html")
# from class_2 import C,D
# from pymysql import Connection
# c=C("D:/数据可视化/2011年1月销售数据.txt")
# d=D("D:/数据可视化/2011年2月销售数据JSON.txt")
# a=c.read()
# b=d.read()
# e=a+b
# conn=Connection(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="643047305+wsq",
#     autocommit=True
# )
# cursor=conn.cursor()
# conn.select_db("practice")
# for x in e:
#     cursor.execute(f"insert into record "
#                    f"values('{x.data}','{x.id}',{int(x.money)},'{x.province}')")
# conn.close()


