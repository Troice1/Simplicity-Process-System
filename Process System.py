import ttkbootstrap
from ttkbootstrap import Style
import tkinter
from tkinter import StringVar
from tkinter import messagebox
import os
import re




MainWindow = ttkbootstrap.Window()
MainWindow.geometry('500x500')
MainWindow.resizable(False, False)

style = Style()
print(style.theme_names())
style.theme_use("vapor")

MainListBox = tkinter.Listbox(MainWindow, width=70, height=20)
MainListBox.place(x=3, y=60)

li = []
def UpdataFunc():
    global li
    li_ = os.popen("tasklist").read()
    li = li_.splitlines()[1:]
    print(li)
    try:
        MainListBox.delete(0, tkinter.END)
    except:
        print("error")
    for i in li:
        MainListBox.insert("end", i)

UpdataFunc()

def EndProcess():
    global MainListBox, li
    # print(MainListBox.curselection()[0] - 1)
    ProcessID = re.findall(' (.*?)Console', li[MainListBox.curselection()[0]])
    if ProcessID == []:
        ProcessID = re.findall(' (.*?)Services', li[MainListBox.curselection()[0]])
    print("taskkill /pid " + str(ProcessID[0]).strip() + " -t")
    print(os.popen("taskkill /pid " + str(ProcessID[0]).strip() + " -f").read())
    tkinter.messagebox.showinfo("title", "已关闭PID为" + str(ProcessID[0]).strip() + "的进程")

EndButton = ttkbootstrap.Button(MainWindow, width=10, text="结束进程", bootstyle=("INFO", "OUTLINE"), command=EndProcess)
EndButton.place(x=20, y=430)


UpdataButton = ttkbootstrap.Button(MainWindow, width=10, text="刷新进程信息", bootstyle=("INFO", "OUTLINE"), command=UpdataFunc)
UpdataButton.place(x=200, y=430)

SearchText = StringVar()
SearchEntry = ttkbootstrap.Entry(MainWindow, textvariable=SearchText, width=50)
SearchEntry.place(x=10, y=10)


def SearchProcess():
    global li, SearchText, MainListBox
    UpdataFunc()
    SearchLi = []
    for i in li:
        if str(SearchText.get()).upper() in str(i).upper():
            SearchLi.append(i)
            print(i)
    li = SearchLi
    MainListBox.delete(0, tkinter.END)
    for j in li:
        MainListBox.insert("end", j)

SearchButton = ttkbootstrap.Button(MainWindow, text="搜索", bootstyle="link", command=SearchProcess)
SearchButton.place(x=400, y=9)

MainWindow.mainloop()
