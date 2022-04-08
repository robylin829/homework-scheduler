#此程式應置於欲處理之課表html資料夾中
#處理結果於此程式所出位置資料夾all_classtable.txt中

import os
classtable={}
f=open('all_classtable.txt','w+',encoding='utf-8')
f.close()
for all_class in range(len(os.listdir())-1):
  class_num = os.listdir()[all_class][:os.listdir()[all_class].find('.')]
  f=open(os.listdir()[all_class],'r',encoding='utf-8')
  original_html=f.read()
  original_html=original_html.replace(' ','').replace('\n','')
  f.close()
  if len(original_html) > 1000 and os.listdir()[all_class] not in ['all_classtable.txt',os.path.basename(__file__)]:
    class_daily=[[],[],[],[],[],[],[]]
    original_html = original_html.split('</tr>')
    original_html = original_html[2:]
    original_html.pop(4)
    original_html.pop(-1)
    for i in range(len(original_html)):
      original_html[i]=original_html[i][original_html[i].find('節<BR></td>'):]
    for i in range(len(original_html)):
      if original_html[i].find('</td>') != -1:
        original_html[i]=original_html[i].split('</td>')
        original_html[i].pop(-1)
        
        for j in range(len(original_html[i])):
          original_html[i][j]=original_html[i][j][(len(original_html[i][j])-original_html[i][j].rfind('>')):]
          if original_html[i][j].find('</a>') != -1:
            original_html[i][j]=original_html[i][j].split('</a>')
            original_html[i][j].pop(-1)
            for k in range(len(original_html[i][j])):
              original_html[i][j][k]=original_html[i][j][k][(original_html[i][j][k].rfind('>')+1):]
          else:
            original_html[i][j]=''
          class_daily[j].append(original_html[i][j])
    classtable[class_num]=class_daily
    f=open('all_classtable.txt','r',encoding='utf-8')
    if str(class_daily) not in f.read():
        f=open('all_classtable.txt','a',encoding='utf-8')
        f.write(os.listdir()[all_class][:os.listdir()[all_class].find('.')]+str(class_daily)+'\n')
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
