# EVE频道预警系统
~~闲的蛋疼~~搓了一晚上搓出的python 脚本 ==不保证不封号== ，没研究过

## 使用说明
首先在 ==eve游戏  设定-->游戏内容-->聊天-->把聊天记录保存为文件==		选中
然后在电脑中 ==文档-->EVE-->logs-->Chatlogs==		找到以开头游戏内频道为命名的txt(文本文档)
(一般在==文件资源管理器左侧会显示==，没有可能在==c盘user/用户== 中)
(D:\小米云盘\文档\EVE\logs\Chatlogs)(我迁移到d盘的)

双击或者右键以管理员身分运行软件
启动后,会弹出窗口,==选择找到的文件==
如果对话中有 应当注意的星系(关键词)就会弹窗警告(有声音)
(默认为 "05R-7A", "5ZO-NZ",  "7-UH4Z",  "FS-RFL",  "N-HSK0",  "X97D-W",  "Y0-BVN"——BUG6-X星座所有星系)

## 源代码
```python
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


    
```

<!-- 原本是想着用HTML JS写的，但是发现web端不让读取指定路径的文件,必须要用户上传,Java好久没用了文档流完全忘光了,然后想起来python是正统的脚本语音,就想着不如用着之前积累的思想经验去百度python的代码,好在都不算太难,虽然花了一晚上但也折腾明白了这些 -->
<!-- 名字AcaciaTreePlan 就是是金合欢树计划,源自一种非洲的树,金合欢树,据说这种树在被长颈鹿啃的时候,会通过气味传递信息,让周围的金合欢树都开始分泌毒素变得难吃什么的 -->
<!-- 第一次写代码真正的拿出来用,也不知道会有多少我这边能用你那边不能用的问题-->