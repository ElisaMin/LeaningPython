import tkinter as tk
import os 

def shell (cmd):
    return os.popen(cmd).read()

window = tk.Tk()
window.title('just for test')
window.geometry('500x800')

lable1 = tk.Label(window, text="lgup_cmd gui工具", width=15, height="3")
lable1.pack()
window.mainloop()
'''
if str(shell(if exist anyway (echo 0) else (echo 1)))==1 :
    print("找不到文件")
    print("退出或者留下")
    askopenfile 选择文件


帮助(LGE.FUN)
lgup_cmd助手
com:
dll:
kdz:
【刷入】
【二维码】
【责任声明】
'''
