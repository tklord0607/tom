import os

def list_files(path):
    files = os.listdir(path)
    for file in files:
        print(file)

# 替换'your_path_here'为你想要列出文件的路径
os.path.exists(r'D:\python test\5130-20220712019-log')