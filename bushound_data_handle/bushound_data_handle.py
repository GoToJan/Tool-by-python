# -*- coding: cp936 -*-
import win32ui

#Ŀ���ļ�
tar_file="target.txt"

start = 0
end = 0
#�������ļ��Ի���
dlg = win32ui.CreateFileDialog(1)
dlg.SetOFNInitialDir('E:/Python')
dlg.DoModal()
filename = dlg.GetPathName()
#���ļ�
print "Open file:%s" %(filename)
try:
	source = open(filename,"r+")
except :
	source.close()
	exit()
#�ı�����
print "handle data"
while 1:
	str = source.readline()
	if len(str)==0:
#		print "break"
		break
	if str.find("Device  Phase  Data") == 0:
#                print "Find flag"
		start = str.find("Data")
		end = str.find("Description")
		source.readline()
		break
#print "start and end is:%d,%d" %(start,end)
target = ""
flag = 0
temp = ""
while 1:
	str = source.readline()
	
	if len(str)==0:
#		print "break"
		break

	if str.find("  OUT") != -1:
                if len(temp) !=0:
                        target = target +temp + "\n" + "\n"
                
                temp = "OUT:"+"\n"
                temp = temp + str[start:end]
                
        elif str.find("  IN") != -1:
                if len(temp) !=0:
                        target = target +temp + "\n" + "\n"

                temp = "IN:"+"\n"
                temp = temp + str[start:end]
                
        else:
                temp = temp + "\n" + str[start:end]


print "write file"
print len(target)
if len(target) !=0:
        print "handle success"
        try:
                tar = open(tar_file,"w")
                tar.write(target)
        except:
                tar.close()
        tar.close()
#�ر��ļ�	
source.close()

