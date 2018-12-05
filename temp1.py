# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a={}
b={1,2,3,4,5}
b.add(1)
b.remove(2)
type(b)
c={1,5,6,9,8,7}
type(c)
b|c
a|c
b={1,2,3,4,5}
c={1,2,7,9,4}
b&c
b<c
b-c
e={"SQL":1,"Java":2,"Scala":3,"Python":4}
f={"Anaconda":1,"Spyder":2,"Jupiter":3}
e.add(f)
a={1,5}
b={2,9,7,6,3}
b.add(9)
b
c=b.copy()
b.remove(2)
b.discard
b=a
b.copy()
b.add(4)
b.discard(4)
b
d=1,2,3,4,"PC","hyd",True
d[3:6]
e=(1,2,3,[1,2,3],[1,9,8])
e[1][2]=1000
f=(5,9,7,[2,3,4])
f.append(e)
f=(1,2,2,4,6,9)
type(f)
f=f+(15,)
f
i=1000
print(id(i))
j=2000
print(i is j)
print(i is not j)
k=3000
print(k)
print(k is i)
p=[10,20,30]
q=[10,20,30]
print(p is q)
print(id(p))
print(id(q))
a="python"
print("y" in a)
obj1=["nb","python","prudent"]
"nb" in obj1
print("Begin")
x=input("Enter a Number:")
x=int(x)
if (x<10):
    print("the number is:" +str(x))
    print("end")    
a=5
b=10
if(a>b):
    print("Lesser")
else:
    print("greater")
x=-1
if(x>0):
    print("positive")
else:
    print("Negative")
x=10
y=-1
if ((x>0) and (y<0)):
    print("correct")
else:
    print("wrong")
x=100
if x<=10:
    print("less than 10")
elif (10<x<20):
    print("x is between 10 and 20")
else:
    print("x is greater than 30")
x=1
while (x<=10):
    print(x)
    x=x+1
    print("new x=" + str(x))
x= input("enter a number:")
while (x<10):
    x=x+1
    print("new x i:" + str(x))
i=0
sum1=0
while (i<=100):
    sum1=sum1+i
    i=i+1
    print(i)
    if (i%2==0):
        print("I value is:", i)
print("total sum:", sum1)
i=0
sum1=0
while (i<=50):
    if(i%2==0):
        sum1=sum1+i
    if (sum1>=200):
        print("total sum:", sum1)
        print("i value:", i)
        break
    i=i+1
i=0
while i<=5:
    i=i+1
    print("welcome",i)
a=range(20)
list(a)
for i in a:
    print(i)
x=range(1,25,5)
list(x)
for i in x:
    print(i)
x=range(25,0,-2)
list(x)
x="python"
for i in x:
    print(i)
x=range(25,0,-2)
for i in x:
    print(i*2)
for i in range(10):
    print("*"*i)
for i in range(5,0,-1):
    print("*"*i)
a=list(range(5,0,-1)) + list(range(2,6))
for i in a:
    print("*"*i)
x=range(1,11)
for i in x:
    print(str(i)*i)
x=range(5,0,-1)
for i in x:
    print("*"*i)
a=list(range(5,0,-1))+list(range(2,6))
for i in a:
    print("*"*i)
a=list(range(1,10,1))+list(range(8,0,-1))
for i in a:
    print(str(i)*i)
x=range(1,10)
sum1=0
for i in x:
    sum1=sum1+i
    print(sum1)
x=range(1,10)
sum1=0
for i in x:
    sum1=sum1+i
    if (i==max(x)):
        print("total sum is:", sum1)
for i in range(10):
    if i%2==0:
        continue
    print(i)
    print("i value is", i)
for i in range(10):
    if i%3==0:
        continue
    print(i)
    a.append(i)
y=[]
x=[1,3,5,2,6,8,9]
for i in range(len(x)):
    y.append(x[i])
    print(y)
a=0
for i in range(20):
    if i%2==0:
        continue
    print("adding:", str(i))
    a=a+i
x=range(1,100)
sum1=0
for i in x:
    if i%2==0:
        continue
    print("I value is:",i)
    sum1=sum1+i
    if i==max(x):
        print("sum is", sum1)
a=0
for i in range(15):
    a=a+i
    if a>15:
        break
    print(i)
a=0
b=[]
for i in range(25):
    a+= i
    b.append(a)
    if a>100:
        break
x=list (range(1,100,5))
sum1=0
i=1
while i<=len(x):
    sum1=sum1+x[i-1]
    print("x value is:", x[i-1])
    i=i+1
x=[[1,2,3],[4,5,6,7],[8,9]]
x[len(x)-1]
for i in x:
    print(i)
    for j in i:
        print(j)
x=[[1,2,3],[4,5,6,7],[8,9]]
for i in x:
    for j in i:
        print(j)
x=[]
for p in range(10):
    x.append(p)
    print(p)
x = [p for p in range(10)]
print(x)
x=[p*p for p in range(10)]
x=[]
for p in range(10):
    x.append(p*p)
    print(p)
x=[]
for p in range(10):
    if p%2==0:
        x.append(p*p)
        print(x)
x=[p*p for p in range(10) if p%2==0]
print(x)
def f1():
    print("PYTHON")
def add(var1,var2):
    input("var1:",var1)
    input("var2:", var2)
    a=var1+var2
    return(a)
    add(10,20)
a=100
def f2(var1,var2):
    a1=a+var1+var2
    return(a1)
    f2(10,20)
    f2(15,68)
def f3(var1,var2):
    a=var1*var2
    return(a)
    f3(3,6)
def f4(var1,var2):
    var1.extend(var2)
    a=0
    for i in var1:
        a=a+i
        return(a)
def f5(var1,var2):
      var1.extend(var2)

f5([1,2,3,4,5],[9,8,7,6,5])
f5()
a=10
def f6(x):
    a=f7(x)
    return(a)
def f7(x):
    b=10
    a=b+x
    return(a)
f6()
def arb(*a,b):
    print(a)
    print(b)
arb(100,200)
b=10
f2()
c=10
def a3(a,b):
    d=25
    e=b+c+d
    print(e)
f2=a3(1,2)
print(f2)

def arb(*a,b):
    sum1=0
    for i in a:
      sum1=sum1+i 
    b=10
    c=sum1+b
    return(c)
    
arb(1,2,3,b=10)

print(c)
myfunc = lambda x: x*x
x=myfunc(5)
print(x)
def myfunc(x):
    x=5
    x=x*x
print(x)
a = lambda x: x*x*x
x=a(5)
print(x)
li=[5,5,22,97,54,62,77,23,73,61]
final_li = lambda x: x+x
print(li)
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list =list(map(lambda x: x+x,li))
print(final_list(li))
li=[5,7,22,97,54,62,77,23,61]
sum1=0
for i in li:
    sum1=sum1+i
    print(sum1)
li=[5,7,22,97,54,62,77,23,61]
type(li)
final_list = lambda x: [sum(sum1,i) for i in li]
print(final_list(li))
def addition(n):
    return n+n
numbers=(1,2,3,4,5)
result=map(addition,numbers)
print(list(result))
numbers=(1,2,3,4)
result=map(lambda x: x+x, numbers)
print(list(result))
num1=[1,2,3]
num2=[4,5,6]
result = map(lambda x,y:x+y, num1,num2)
print(list(result))
num1=[1,2,3]
num2=[4,5,6]
result=map(lambda x,y:x+y,num1,num2)
print(list(result))
my_list = [1,2,3,4,5,6,7,8,9]
new_list=list(filter(lambda x: x%2, my_list))
print(new_list)
import functools as ft
li=[1,2,3,4,5,6,7]
ft.reduce(lambda a,b:a+b, li)
li=[1,2,3,4,5,6,7]
ft.reduce(lambda a,b: a if a>b else b, li)
numbers=(1,2,3,4)
r=map(lambda x:x+x, numbers)
print(list(r))
name=["Manjeet","Nikhil","sam","Asfa"]
roll_no=[4,1,6,9]
marks=[40,50,60,70]
mapped=zip(name,roll_no,marks)
list(mapped)
print(set(mapped))
namez,roll_numz,marksz=zip(*mapped)
players=["sachin","sehwag","kohli","Gambir","Dravid","Ashwin"]
scores=[150,69,98,46,51]
outlook=zip(players,scores)
list(outlook)
for players,scores in zip(players,scores):
    print("player: %s score: %d" %(players,scores))
Employee=["Arya","Veda","Simran","Trisha","Nayan","Tina","Lowa"]
salary=[30000,69000,32000,14000,54000,38000,47000]
Emp_table=zip(Employee,salary)
list(Emp_table)
for Employee,salary in zip(Employee,salary):
    print("Name: %s and the salary is:%d" %(Employee,salary))
import numpy as np
col_vec=np.array([[1],[2]])
row_vec=np.array([[1],[2],[3]])
mat=np.array([[[1,2],[3,4],[5,6]]])
mat.ndim
Train_station=["Ambattur","pattaravakkam","korattur","villivakkam","LocoWorks"]
time=[1620,1623,1630,1636]
station_details=zip(Train_station,time)
list(station_details)
for Train_station,time in station_details:
a=[1,2,3]
b=[3,4,5]
c=map(lambda x,y:x+y,a,b)
list(c)
numbers=[1,2,6,9,8,7]
c=lambda x:x+x, numbers
list(c)
#Questons and answers:
#1. pip install  numpy
#2.ID
import numpy as np
a=np.arange(10)
a=np.arange(7)
#3.a.ndim,b. shape, c.size, d.dtype.name
row_vec=np.array([[1],[2],[3]])
row_vec.shape
mat=np.array([[1,2],[3,4],[6,7]])
mat.shape
mat.size
mat.dtype
mat.dtype.name
#4. convert datatype
b=np.array([[1,2,3],[4,5,7]])
b.shape
b.dtype.name
b.astype(float)
#5.
np.zeros([10,10])
#6.
np.ones([10,10])
#7
c=np.array([[1,4],[6,8],[5,3]])
c.dtype.name
c.astype(float)
#8.
np.full([10,5],5)
#9
f=np.random.randint(low=1,high=100,size=10)
#10
g=np.random.randint(low=5,high=90,size=8)
#11 save an object
np.save('save1',a)
import os
os.getcwd()
#12 load a current working directory
h=np.load('save1.npy')
print(h)
#13 load multiple objects
np.savez("allobjsaves",b,c,f,g)
os.getcwd()
d=np.load('allobjsaves.npz')
print(d['arr_0'])
print(d['arr_1'])
print(d['arr_2'])
#*****************
#1.avg of n observations:
num=int(input("how many numbers:"))
tsum=0
for n in range(num):
    numbers=float(input("enter a num:"))
    tsum=tsum+numbers
avg=tsum/num
print("avg is:", avg)
#2.coeff of variation
np.exp(8)
i=np.mean(range(10))
j=np.std(range(10))
coeff=i/j
#3.even numbers extract
num=int(input("how many numbers:"))
tsum=0
for i in range(num):
    j=int(input("enter number:"))
    if j%2==0:
        print("the number is:", j)    
#4. highest observation
k=np.arange(10)
l=max(k)
m=np.random.randint(low=1,high=10,size=10)
max(m)
n=[1,6,8,4,7,11,5]
max(n)
#5 mean absolute deviation:
num=int(input("how many numbers:"))
tsum=0
for n in range(num):
    numbers=float(input("enter a number:"))
    tsum=tsum+numbers
mean=tsum/num
print("Mean is:", mean)
l=[5,7,9,0]
np.mean(l)
#6.median
l=[3,2,1,7,9,0,8]
np.median(l)
#7mode]
import statistics
from statistics import mode
l=[1,1,5,7,9,3,1]
statistics.mode(l)
m=[5,8,6,3,5,8,6,4,6,7]
statistics.mode(m)
#8 std
n=[1,5,8,0,4,5]
np.std(n)
a=np.random.random([5,5])
a[1]
a[0]
a[2,:]
a[:,1]
a[0,3]
a[0,4]
a[0:2,2:3]
a[1:2,3:3]
a=np.random.random([5,5])
a[1]
a[0]
a[2,:]
a[:,1]
a[0,3]
a[0:2,2:3]
a[0:2,2:4]
a=np.random.random([5,5])
a.sum()
a.min()
a.max()
a.max(axis=0)
a.cumsum(axis=0)
a.min(axis=1)
a[1].min(axis=0)
a[1].max(axis=0)
a[3].min(axis=1)
import pandas as pd
df=pd.read_csv("C:/Users/Prabhu/Desktop/vid personal/python_trial.csv")
df.to_pickle("C:/Users/Prabhu/Desktop/vid personal/python_trial.csv")
a=np.linspace(1,50,10)
a.astype(int)
a1=pd.Series(a)
a2=pd.DataFrame(a)
a=np.linspace(0,50,15)
a1=pd.Series(a)
a2=pd.DataFrame(a)
a3=np.linspace(10,75,15)
a4=pd.Series(a3)
df1=pd.DataFrame({'col1':[1,3,5],'col2':[2,4,6]})
df1.shape
import pandas as pd
import numpy as np
df=pd.read_csv("C://Users//Prabhu//Desktop//vid personal//python_trial.csv")
a=np.linspace(1,100,15)
a1=pd.Series(a)
a2=pd.DataFrame(a)
a=np.linspace(1,50,5)
b=np.linspace(51,100,5)
df={'col1':a,'col2':b}
c=pd.DataFrame(df)
a=np.linspace(1,10,5)
b=np.linspace(11,20,5)
df={'first_column':a,'second_column':b}
c=pd.DataFrame(df)
c=pd.Series(df)
c.index
d=pd.DataFrame({'col1':[1,2,3],'col2':[4,5,6]})
d=pd.DataFrame({'col1':[1,2,3],'col2':[4,5,6]})
#two ways to create dataframes:
a=np.linspace(1,10,5)
b=np.linspace(11,20,5)
c={'first_column':a,'second_column':b}
d=pd.DataFrame(c)
e=pd.DataFrame({'first_column':[1,3.25,5.50,7.75,10.00],'second_column':[11.00,13.25,15.50,17.75,20.00]})
e.shape
d.index
e.columns
list(e)
f=pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10,np.nan,np.nan],'col2':[np.nan,3,4,10,23,21,24,32,np.nan,4,6,9]})
f.col1.isnull()
f.col1.isnull().sum()
f.shape
f.index
f.col1.isnull()
f.col1.isnull().sum()
f.col1.notnull()
f.col1.notnull().sum()
f.isnull().sum()
f.notnull().sum()
f.describe()
np.where(f.isnull())
np.where(f.col2.isnull())
np.where(f.col1.isnull())
f[col1].fillna(9999,inplace=True)
import pandas as pd
import numpy as np
a=pd.DataFrame({'A':[1,2,3,4,5,np.nan,6,7,8,np.nan], 'B':[11,12,np.nan,14,15,16,17,np.nan,19,20],'C':[21,22,23,np.nan,25,26,np.nan,28,29,np.nan]})
a.shape
a.index
a.isnull().sum()
np.where(a.isnull())
a
np.where(a.A.isnull())
a['A'].fillna(9999,inplace=True)
a['B'].fillna(9999,inplace=True)
a['C'].fillna(9999,inplace=True)
a['A'].fillna(a.A.mean(),inplace=True)
a['B'].fillna(a.B.mean(),inplace=True)
import pandas as pd
import numpy as np
a=pd.DataFrame({'A':[1,2,3,4,5,np.nan,6,7,8,np.nan], 'B':[11,12,np.nan,14,15,16,17,np.nan,19,20],'C':[21,22,23,np.nan,25,26,np.nan,28,29,np.nan]})
np.where(a.A.isnull())
np.where(a.B.isnull())
np.where(a.C.isnull())
a['A'].fillna(9999,inplace=True)
a.fillna(9999,inplace=True)
a.A.fillna(9999,inplace=True)
a.A.fillna(1111,inplace=True)
a.B.isnull().sum()
a.describe()
a.info()
a.fillna(1111,inplace=True,axis=0)
a.fillna(a.mean(),inplace=True)
a.astype(int)
a.astype(float)
a.mean()
a.fillna(a.mean())
a.head()
a.tail()
a.head(6)
a.tail(2)
a.info()
c=np.random.random([10,10])
c1=pd.DataFrame(c)
c1.shape
b=np.random.random([2,10])
d=b1.append(c1)
d.reset_index()
import pandas as pd
import numpy as np
x=pd.DataFrame({'X1':[1,2,3,np.nan,5,6,np.nan,8,9,np.nan],'X2':[11,np.nan,13,14,np.nan,16,17,18,np.nan,20],'X3':[21,np.nan,23,np.nan,25,26,np.nan,28,29,30]})
x.shape
np.where(x.isnull())
x.columns
x.X1.fillna(9999,inplace=True)
x.fillna(9999,inplace=True)
x.head(2)
x.tail(2)
x.describe()
x.info()
y1=np.random.random([5,3])
y2=y.rename(columns={0:'X1',1:'X2',2:'X3'})
y=pd.DataFrame(y1)

z=x.append(y2)
z.reset_index()
z.fillna(9999,inplace=True)
z.astype(int,inplace=True)
z.columns
z.reset_index().drop('index',axis=1)
z.fillna(9999, inplace=True)
z.rename(columns={0:'X4',1:'X5',2:'X6'})
z[1]
z[0]
e=np.random.randint(1,100,100)
e.reshape([10,10])
f=pd.DataFrame(e)
f.reshape(10,10)
e=np.random.randint(1,100,100).reshape(10,10)
f=pd.DataFrame(e)
f.columns
list(f)
f.rename(columns={0:'col1',1:'col2',2:'col3',3:'col4',4:'col5',5:'col6',6:'col7',7:'col8',8:'col9',9:'col10'})
f.shape
f.isnull().sum()
f.index
list(f.index)
g=pd.Series(f).value_counts()
d1=pd.DataFrame(np.random.random([5,5]))
d1[0]
d1[0,3]
z
d1.iloc[0,0]
f.loc(f.0>30)
x
x.set_index('index')
list(x)[:2]
df=pd.DataFrame({'col1':[2,1,2,4,3], 'col2':[2,2,2,3,4],'col3':[4,3,5,2,1]})
df.sort_values(['col1','col3'])
df.sort_values(['col1','col3'],ascending=[True,False])
a=df.groupby('col1')
df['new']=[1,2,2,3,4]
a=df.groupby('new')
a.groups.keys()
a.groups.values()
list(a)[0]
list(a)[1]
list(a)[2][1]
df=pd.DataFrame({'col1':[1,4,6,2,5],'col2':[4,6,2,4,1],'col3':[5,2,4,7,1]})
df['new']=[1,3,2,5,1]
a=df.groupby('new')
list(a)[1]
a.groups.keys()
df.groupby('new')['col2','col1','col3'].mean()
df.groupby('new')['col1','col2','col3'].mean()
a=np.random.randint(1,100,15).reshape(5,3)
b=pd.DataFrame(a)
c=b.rename(columns={0:'X1',1:'X2',2:'X3'})
d=z.append(c)
d.reset_index().drop('index',axis=1)
d.fillna(9999,inplace=True)
d.astype(int)