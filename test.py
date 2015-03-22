import datetime
import os 
os.environ['tz'] = 'Asia/Tapei'

for x in range(1,18):
  #  a.append("2015wcm_g"+str(x))   array+1
    #print ("2015wcm_g"+str(x)+".md")   debug use 
 
#open the file 
    op = open("2015wcm.wiki/2015wcm_g"+str(x)+".md","r+",encoding = 'UTF-8')


#op.md 內容
#40323101
#1.about me
#2.linkedin
#3.wordpress

    while True :
        i = op.readline()
        if i =='':
            break
        print(i ,end='')

    op.close()

#ata = []
#or line in op.readlines():
  # data.append(line)
    

#p.close()

#las_number = data[0]

#rint(clas_number)
