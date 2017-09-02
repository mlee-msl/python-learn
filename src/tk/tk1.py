#!/usr/bin/python3
#-*- coding: utf-8 -*-

import tkinter

def action():
	print("Hello, world")

if __name__ == "__main__":
	root = tkinter.Tk()
	root.title("MLee...")
	f = tkinter.Frame(root)
	f.pack()
	l = tkinter.Label(f, text="你好", fg="red")
	l.pack()
	b = tkinter.Button(f, text="打一下招呼", bg="blue", command=action)
	b.pack()
	root.mainloop()

