import os
import sys

print("先设置环境变量 例： QTDIR C:\\xxxx\\5.15.1")

print("参数1 版本的环境变量:")
'''
print("----------------------------------------")
env_dist = os.environ
for key in env_dist:
    print(key + ' : ' + env_dist[key])
print("----------------------------------------")
'''
arg1_ = input()
arg1 = os.environ.get(arg1_)
print("参数2 pro文件名:")
arg2 = input()

test = arg1+"\\bin\\qmake.exe -tp vc "+arg2+".pro -o "+arg2+".vcxproj QMAKE_INCDIR_QT="+arg1+"\\include  QMAKE_LIBDIR="+arg1+"\\lib QMAKE_MOC="+arg1+"\\bin\\moc.exe QMAKE_QMAKE="+arg1+"\\bin\\qmake.exe"

print(test)
os.system(test)