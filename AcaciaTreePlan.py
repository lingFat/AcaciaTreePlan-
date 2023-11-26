import win32api,win32con
import os
import tkinter as tk
from tkinter import filedialog

# 实例化 获取文件路径前置
root = tk.Tk()
root.withdraw()


# 应当注意的星系 05R-7A*  5ZO-NZ*  7-UH4Z*  FS-RFL*  N-HSK0*  X97D-W*  Y0-BVN*   修改这里，将需要的星系名称添加替换进去
galaxies = [ "05R-7A", "5ZO-NZ",  "7-UH4Z",  "FS-RFL",  "N-HSK0",  "X97D-W",  "Y0-BVN" ]
# 已经激活次数
num = 0

# 文件大小
file_size = 0

#  预警频道文件位置
# 获取文件路径
f_path = filedialog.askopenfilename()
print('\n获取的文件地址：', f_path)

file_location = f_path
file_path = str(file_location)
# 开启文件
chatFile = open(file_path,"r",encoding='utf-16')
chatFile2 =open(file_path,"r",encoding='utf-16')

def checkOne():
    # 读取大小 如果一致就跳过
    global file_size
    if file_size == chatFile.seek(0,os.SEEK_END):
        return 
    file_size = chatFile.seek(0,os.SEEK_END)
    # 预警频道文件读取
    chatMessage = chatFile2.readline()
    while chatMessage :
        print(chatMessage)
        # 判断预警频道中，有无需要注意的星系出现
        for galaxy in galaxies :
            if galaxy in chatMessage :
                win32api.MessageBox(0, galaxy+"有敌方活动", "提醒",win32con.MB_ICONWARNING)                            
        chatMessage = chatFile2.readline()
    
while True:
    checkOne()






# while True:
#     # 本次查询到的激活次数
#     new_num = 0
#     # 读取大小 如果一致就跳过
#     if file_size == chatFile.seek(0,os.SEEK_END):
#         continue 
#     file_size = chatFile.seek(0,os.SEEK_END)
#     # 预警频道文件读取
#     chatMessage = chatFile2.readline()
#     while chatMessage :
#         print(chatMessage)
#         # 判断预警频道中，有无需要注意的星系出现
#         for galaxy in galaxies :
#             # print(chatMessage)
#             # print(galaxy in chatMessage)
#             if galaxy in chatMessage :
#                 win32api.MessageBox(0, "这是一个测试提醒OK消息框", "提醒",win32con.MB_OK)                            
#         chatMessage = chatFile2.readline()
    