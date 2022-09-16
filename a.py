from datetime import date, datetime, timedelta
import time
arr = ['11-12','r10-21']
for index, aim_date in enumerate(arr):
  if aim_date[0] == 'r':
    aim_date =  str(time.localtime(time.time())[0]) + aim_date.replace('r', '-')
    aim_date = str(datetime.strptime(aim_date,'%Y-%m-%d'))
    aim_date = aim_date[5:10]
  print(aim_date)
  print(type(aim_date))
# date1 = 'r10-21'
#   aim_date =  str(time.localtime(time.time())[0]) + date1.replace('r', '-')
# print('你好')
# print(type(time.localtime(time.time())[0]))
# print(type(date1))
# print(aim_date)

