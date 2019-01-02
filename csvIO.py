import csv

stu = ['Marry', 28, 'Changsha']
stu1 = ['Rom', 23, 'Chengdu']
#打开文件
out=open('stu_info.csv','a',newline='')
#设定打开模式
csv_write=csv.writer(out,dialect='excel')
#写入具体内容
csv_write.writerow(stu)
csv_write.writerow(stu1)
print("Over")

csv_file = csv.reader(open('stu_info.csv', 'r'))
for stu in csv_file:
    print(stu[0])

