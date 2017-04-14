import shutil, os, datetime, time, sys

newFolderName = datetime.datetime.now()
newFolder = newFolderName.strftime('%m%d%Y')

src = ('E:\\COPY\\')
dst = ('D:\\COPY\\' +
           newFolderName.strftime('%d-%B-%y\\').upper())

shutil.copytree(src, dst)