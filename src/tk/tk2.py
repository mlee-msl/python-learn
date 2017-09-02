#!/usr/bin/python3
#-*- coding: utf-8 -*-

import tkinter
import tkinter.messagebox
import sys

def go():
	flag = tkinter.messagebox.askyesno("ask?", "心情好么？")
	if flag:
		tkinter.messagebox.showinfo("tip", "oops,猜对了!!!")
	else:
		tkinter.messagebox.showinfo("tip", "我的心情很好嘛...乱猜")

def exit():
	sys.exit(0)

if __name__ == "__main__":
	root = tkinter.Tk()
	root.title("MLee...")

	f = tkinter.Frame(root)
	f.pack()
	label = tkinter.Label(f, fg="red", text="你好啊\n_~-~_不好...")
	label.pack()
	button = tkinter.Button(f, text="心情?", command=go)
	button.pack()

	button2 = tkinter.Button(f, text="退出", command=exit)
	button2.pack()
	root.mainloop()
