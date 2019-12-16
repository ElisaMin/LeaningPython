import os
from tkinter import *
from tkinter.filedialog import askopenfilename
def shell(cmd):  # 访问shell指令
    ret = os.popen(cmd).read()
    return ret
window =Tk()
window.title('LGUP_CMD')
'''tk Start'''
# Frame
frameTitle = Frame()
frameBody = Frame()
frameFooter = Frame()
# StringVar
stringVar0 = StringVar();stringVar0.set("LGUP")  # lgup
stringVar1 = StringVar();stringVar1.set("输入端口数字（如3、4等）")  # com
stringVar2 = StringVar();stringVar2.set("点击旁边的按钮选择DLL")  # dll
stringVar3 = StringVar();stringVar3.set("点击旁边的按钮选择KDZ")  # kdz
# Entry
entry0 = Entry(frameBody, textvariable=stringVar0)  # lgup
entry1 = Entry(frameBody, textvariable=stringVar1)  # com
entry2 = Entry(frameBody, textvariable=stringVar2)  # dll
entry3 = Entry(frameBody, textvariable=stringVar3)  # kdz
# Lable
lable = Label(window)
lable0 = Label(frameTitle, text="图形化LGUP_cmd", height="3")  # title
lable10 = Label(frameBody, text="LGUP", height="3")  # LGUP
lable1 = Label(frameBody, text="LGUP已找到，不需要手动输入。", height="3")  # LGUP
lable11 = Label(frameBody, text="端口",  height="3")  # com
lable12 = Label(frameBody, text="DLL",  height="3")  # dll
lable13 = Label(frameBody, text="KDZ", height="3")  # kdz
# Button
def btn0():  # Yes
    dll = stringVar2.get()
    kdz = stringVar3.get()
    com = stringVar1.get()
    lgup = stringVar0.get()
    cmd = lgup+"  com"+com+"  \""+dll+"\" \""+kdz+"\"";
    shell("start cmd /k \"echo off && echo "+cmd+" && "+cmd+"&& echo 按任意键结束 && set /p powerdbyheizi=\"")
button0 = Button(frameFooter,text="确认",command=btn0)
def btn01():  # Help
    shell("start https:\\\\g7.lge.fun\\guide\\cmdup.html")
button01 = Button(frameFooter,text="帮助",command=btn01)
def btn1():  # dll
    stringVar2.set(askopenfilename(title='选择DLL文件', filetypes=[('DLL', '*.dll'), ('所有文件', '*')],initialdir='%ProgramFiles(x86)%\\LG Electronics\\LGUP\\model\\Common'))
button1 = Button(frameBody,text="…",command=btn1)  # AskFile
def btn2():  # KDZ
    stringVar3.set(askopenfilename(title='选择KDZ文件', filetypes=[('KDZ', '*.KDZ'), ('所有文件', '*')]))
button2 = Button(frameBody,text="…",command=btn2)  # AskFile
def btn3():  # LGUP
    stringVar0.set(askopenfilename(title='选择LGUP文件', filetypes=[('LGUP', '*.exe'), ('所有文件', '*')]))
    print(stringVar0)
button3 = Button(frameBody,text="…",command=btn3)  # AskFile
# Place
frameTitle.grid()
frameBody.grid()
frameFooter.grid()
    #   Title
lable0.grid(row=0,column=0,columnspan=3)
    #   Body
lable11.grid(row=0,column=0);entry1.grid(row=0,column=1);lable.grid(row=0,column=2);lable.grid(row=0,column=3)
lable12.grid(row=1,column=0);entry2.grid(row=1,column=1);button1.grid(row=1,column=3);lable.grid(row=1,column=3)
lable13.grid(row=2,column=0);entry3.grid(row=2,column=1);button2.grid(row=2,column=3);lable.grid(row=2,column=3)
        # is LGUP exits
if os.popen("if exist \"%ProgramFiles(x86)%\\\LG Electronics\\LGUP\\LGUP_Cmd.exe\" echo true else echo false").read():
    stringVar0.set("\"%ProgramFiles(x86)%\\LG Electronics\\LGUP\\LGUP_Cmd.exe\"")
    lable1.grid(row=3,column=0,columnspan=3)
    print("done")
else:
    lable10.grid(row=3,column=0);entry0.grid(row=3,column=1);button3.grid(row=3,column=3);lable.grid(row=3,column=3)
    print("else done");
    #   Footer
button0.grid(row=0,column=0);button01.grid(row=0,column=1)
# mainloop
window.mainloop()
'''tk end'''
'''
powerdBy-Heizi 2019.12.17
'''
