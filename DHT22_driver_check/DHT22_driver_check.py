# -*- coding: cp936 -*-
from __future__ import division
import win32ui
#Ŀ���ļ�
tar_file="target.txt"

start = 0
end = 0
#�������ļ��Ի���
dlg = win32ui.CreateFileDialog(1)
dlg.SetOFNInitialDir('')
dlg.DoModal()
filename = dlg.GetPathName()
#��Դ�ļ�
print "Open file:%s" %(filename)
try:
	source = open(filename,"r+")
except :
	source.close()
	exit()
	
all = 0
error = 0
#��������
print "handle data"
for line in source:
	temp = line.strip('\n')
	tem = temp.split(",")
        if len(tem) <2:
                break
#        print tem[-1],tem[-2]
	if cmp(tem[-1],tem[-2]) != 0:
		error = error +1
	else:
                all =all +1
print "The result is:in %d item,%d error,the error rate is:%f" %(all,error,error / all)
#print "%d item" %all
#print "%d error" %error
#print "ERR is %f" %(error / all)
source.close()

