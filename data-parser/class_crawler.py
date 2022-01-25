#請置頂
classtable={}
#請置頂

#爬蟲抓的班級代碼
class_num=''
#爬蟲抓的班級代碼，如下：
#https://grades.hs.ntnu.edu.tw/classtable/down.asp?sqlstr=「此為class_num」&type=class&selArrange=L&selWindow=Right

#以下是dumb(爬到的課表)示例
dumb='<tablealign="center"border="1"cellpadding="2"cellspacing="0"class="classTable"id="classTable"><trstyle="background-color:#003366;"><tdclass="titleclasstable_titlecenter"colspan="9"><spanclass="view_title"style="display:none;">110學年第1學期　課表</span><spanclass="prn_title"style="display:none;"><spanclass="prn_school_name">國立台灣師範大學附屬高級中學</span><spanclass="prn_syear">110</span>學年度第<spanclass="prn_sterm">1</span>學期課程表</span></td></tr><!--星期最上方橫欄--><tr><tdclass="tdHeadertermcenteredge_Ledge_T"colspan="3"></td><tdclass="tdHeaderedge_T">一</td><tdclass="tdHeaderedge_T">二</td><tdclass="tdHeaderedge_T">三</td><tdclass="tdHeaderedge_T">四</td><tdclass="tdHeaderedge_T">五</td><tdclass="tdHeaderedge_Tedge_R">六</td></tr><!--節數--><tr><tdclass="tdHeader1edge_L"rowspan="5"><p>上</p><p>午</p></td><tdclass="tdHeader3"><br/> ︴<br/></td><tdclass="tdHeader2">早<br/>自<br/>習<br/></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumnedge_R"></td></tr><tr><tdclass="tdHeader3">08:10<br> ︴<br/>09:00</br></td><tdclass="tdHeader2">第<br/>一<br/>節<br/></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumnedge_R"></td></tr><tr><tdclass="tdHeader3">09:10<br> ︴<br/>10:00</br></td><tdclass="tdHeader2">第<br/>二<br/>節<br/></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumnedge_R"></td></tr><tr><tdclass="tdHeader3">10:10<br> ︴<br/>11:00</br></td><tdclass="tdHeader2">第<br/>三<br/>節<br/></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumnedge_R"></td></tr><tr><tdclass="tdHeader3">11:10<br> ︴<br/>12:00</br></td><tdclass="tdHeader2">第<br/>四<br/>節<br/></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumnedge_R"></td></tr><tr><tdclass="edge_Ledge_Rseparator"colspan="9"style="background-color:#000033;height:15px;"></td></tr><tr><tdclass="tdHeader1edge_Ledge_B"rowspan="5"><p>下</p><p>午</p></td><tdclass="tdHeader3">13:00<br> ︴<br/>13:50</br></td><tdclass="tdHeader2">第<br/>五<br/>節<br/></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumnedge_R"></td></tr><tr><tdclass="tdHeader3">14:00<br> ︴<br/>14:50</br></td><tdclass="tdHeader2">第<br/>六<br/>節<br/></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumnedge_R"></td></tr><tr><tdclass="tdHeader3">15:10<br> ︴<br/>16:00</br></td><tdclass="tdHeader2">第<br/>七<br/>節<br/></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumnedge_R"></td></tr><tr><tdclass="tdHeader3">16:10<br> ︴<br/>17:00</br></td><tdclass="tdHeader2">第<br/>八<br/>節<br/></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumn"></td><tdclass="tdColumnedge_R"></td></tr><tr><tdclass="tdHeader3edge_B">17:10<br> ︴<br/>18:00</br></td><tdclass="tdHeader2edge_B">第<br/>九<br/>節<br/></td><tdclass="tdColumnedge_B"></td><tdclass="tdColumnedge_B"></td><tdclass="tdColumnedge_B"></td><tdclass="tdColumnedge_B"></td><tdclass="tdColumnedge_B"></td><tdclass="tdColumnedge_Bedge_R"></td></tr></table>'
#以上是dumb(爬到的課表)示例

#以下搭配爬蟲做迴圈

#dumb賦值為爬蟲內容，後為去空格
dumb=''.replace(' ','')
#dumb賦值為爬蟲內容，後為去空格

#避免反爬蟲導致格式不符
if len(dumb) > 1000:
#避免反爬蟲導致格式不符
  day=[[],[],[],[],[],[]]
  dumb = dumb[791:]
  dumb = dumb.split('</tr>')
  dumb.pop(5)
  dumb.pop(-1)
  dumb[5] = dumb[5][69:]
  for i in range(len(dumb)):
    dumb[i]=dumb[i][96:]
  dumb[9]=dumb[9][16:]
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
            dumb[i][j][k]=dumb[i][j][k][(len(dumb[i][j][k])-dumb[i][j][k].rfind('>')):]
        else:
          dumb[i][j]=''
        day[j].append(dumb[i][j])
  classtable[class_num]=day

#以上搭配爬蟲做迴圈

'''
從字典中以鍵找班級(鍵為int)，值
為一個list，此list的每一項對應週
一至週六，每一項也是一個list，此
時每一項對應第0~9節(早自習為0)
'''
