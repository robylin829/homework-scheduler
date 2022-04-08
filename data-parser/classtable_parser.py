#此程式應置於欲處理之課表html資料夾中
#處理結果於此程式所出位置資料夾all_classtable.txt中

import os
classtable={}
f=open('all_classtable.txt','w+',encoding='utf-8')
f.close()
for all_class in range(len(os.listdir())-1):
  class_num = os.listdir()[all_class][:os.listdir()[all_class].find('.')]
  f=open(os.listdir()[all_class],'r',encoding='utf-8')
  dumb=f.read()
  dumb=dumb.replace(' ','').replace('\n','')
  f.close()
  if len(dumb) > 1000 and os.listdir()[all_class] not in ['all_classtable.txt',os.path.basename(__file__)]:
    day=[[],[],[],[],[],[],[]]
    dumb = dumb.split('</tr>')
    dumb = dumb[2:]
    dumb.pop(4)
    dumb.pop(-1)
    for i in range(len(dumb)):
      dumb[i]=dumb[i][dumb[i].find('節<BR></td>'):]
    for i in range(len(dumb)):
      if dumb[i].find('</td>') != -1:
        dumb[i]=dumb[i].split('</td>')
        dumb[i].pop(-1)
        
        for j in range(len(dumb[i])):
          dumb[i][j]=dumb[i][j][(len(dumb[i][j])-dumb[i][j].rfind('>')):]
          if dumb[i][j].find('</a>') != -1:
            dumb[i][j]=dumb[i][j].split('</a>')
            dumb[i][j].pop(-1)
            for k in range(len(dumb[i][j])):
              dumb[i][j][k]=dumb[i][j][k][(dumb[i][j][k].rfind('>')+1):]
          else:
            dumb[i][j]=''
          day[j].append(dumb[i][j])
    classtable[class_num]=day
    f=open('all_classtable.txt','r',encoding='utf-8')
    if str(day) not in f.read():
        f=open('all_classtable.txt','a',encoding='utf-8')
        f.write(os.listdir()[all_class][:os.listdir()[all_class].find('.')]+str(day)+'\n')
    f.close()
print('done!')
os.system('pause')


##########字典或許有用##########
############暫時保留############
'''
從字典中以鍵找班級(鍵為int)，值
為一個list，此list的每一項對應週
日至週六，每一項也是一個list，此
時每一項對應第0~9節(早自習為0)
'''
