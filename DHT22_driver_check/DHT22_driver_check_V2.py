# -*- coding: cp936 -*-
from __future__ import division
import win32ui
import csv
#Ŀ���ļ�
tar_file="target.txt"


#�������ļ��Ի���
dlg = win32ui.CreateFileDialog(1)
dlg.SetOFNInitialDir('')
dlg.DoModal()
filename = dlg.GetPathName()

if len(filename) ==0:
        print "file's name is ivilid"
        exit()
all = 0
error = 0
#��������
with open(filename,"r+") as f:
        source = csv.reader(f)
        for line in source:
                if len(line) <2:
                        break
                print line[-1],line[-2]
                if cmp(line[-1],line[-2]) != 0:
                        error = error +1
                all =all +1
                        
print "The result is:in %d item,%d error,the error rate is:%f" %(all,error,error / all)

f.close()

