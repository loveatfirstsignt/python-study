import os,re
txt=file('..\\available.txt','a')
for p,d,f in os.walk('.'):
    if 'session.sqlite' in f:
        path=os.path.join(p,'target.txt')
        f=file(path,'r')
        content=f.readline()
        req=r'(^http:.+?) '
        math=re.findall(req,content)
        ok=math[0]
        txt.write(ok+'\n')
txt.close()
