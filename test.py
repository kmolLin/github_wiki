import datetime
import os 
os.environ['tz'] = 'Asia/Tapei'

#open the file 
op = open("2015wcm_g1.md","r+")

'''op.md 內容
40323101
1.about me
2.linkedin
3.wordpress
'''
data = []
for line in op.readlines():
    data.append(line)
    

op.close()

clas_number = data[0]

print(clas_number)
