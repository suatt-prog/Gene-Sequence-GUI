from  tkinter import *
from time import sleep
k=int(input("k tuple uzunluğunu giriniz"))
j=input("j dizisini giriniz")
i=input("I dizisini giriniz")
say0=0
while say0<k:
    j=j+"0"
    i=i+"0"
    say0=say0+1
say=0
say1=0
say2=1
a=int()
a={}
say3=0
while say<(len(j)-k):
    while say1<(len(i)-k):
        if j[say]==i[say1]:
            while say2<k:
                if j[say+say2]==i[say1+say2]:
                    if say2==(k-1):
                        a[say3]=say
                        a[say3+1]=say1
                        say3 = say3 + 2
                    say2=say2+1
                else:
                    break
            say2=1
        say1=say1+1
    say1=0
    say=say+1
root=Tk()
Label(root, text="").grid(column=0, row=0)
l=0
while l<(len(j)-k):
    Label(root,text=j[l]).grid(column=l+1,row=0)
    l=l+1
t=0
while t<(len(i)-k):
    Label(root,text=i[t]).grid(column=0,row=t+1)
    t=t+1
y=0
c=1
while y<len(a):
    while c<=k:
        Label(root,text=c,bg="blue").grid(row=a[y+1]+c,column=a[y]+c)
        c=c+1
    c=1
    y=y+2
root.mainloop()
