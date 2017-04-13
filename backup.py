import shutil, os, datetime, time, sys

newFolderName = datetime.datetime.now()
newFolder = newFolderName.strftime('%m%d%Y')


src = ('E:\\COPY\\')
dst = ('D:\\COPY\\' +
           newFolderName.strftime('%d-%B-%y\\').upper())

for file in os.listdir(src):
    src_file = os.path.join(src, file)
    dst_file = os.path.join(dst, file)
    shutil.copytree(src, dst)