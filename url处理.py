# -*- coding: cp936 -*-
import re,os
def stepone(filename,stye):
    new_file=file('c:\\users\\administrator\\Desktop\\temp.txt','a')
    f=file('c:\\users\\administrator\\desktop\\%s'%filename,'r')
    while True:
        raw=f.readline()
        if len(raw)>0:
            req=r'\.%s\?[iI][dD]'%stye
            result=re.findall(req,raw)
            if len(result)>0:
                new_file.write(raw)
            else:
                continue  
        else:
            break
    f.close()
    new_file.close()
    database=[]
    f1=file('c:\\users\\administrator\\desktop\\temp.txt','r')
    f2=file('c:\\users\\administrator\\desktop\\result.txt','a')
    while True:
        data=f1.readline()
        if len(data)>0:
            test=data.split('.jsp')[0]
            if test not in database:
                database.append(test)
                f2.write(data)
            else:
                continue
        else:
            break
    f1.close()
    os.remove('c:\\users\\administrator\\desktop\\temp.txt')
    f2.close()
filename=raw_input('输入要转换的文件名:')
stye=raw_input('输入格式:')
stepone(filename,stye)
