import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def btn1():
    h = txt1.get()


def btn2():
    o = txt2.get()


def enter():
    root.destroy()


root = tk.Tk()
root.title('行頭行末文字追加')
root.resizable(False, False)

lbl0 = tk.Label(text='文字を入力して右のボタンを押してください')
lbl0.grid(row=0, column=1)

lbl1 = tk.Label(text='行頭')
lbl1.grid(row=1, column=0)
txt1 = tk.Entry(width=35)
txt1.grid(row=1, column=1)
inbtn1 = ttk.Button(text='行頭追加', command=btn1())
inbtn1.grid(row=1, column=2)

lbl2 = tk.Label(text='行末')
lbl2.grid(row=2, column=0)
txt2 = tk.Entry(width=35)
txt2.grid(row=2, column=1)
inbtn2 = ttk.Button(text='行末追加', command=btn2())
inbtn2.grid(row=2, column=2)

enter_btn = ttk.Button(text='次へ', command=enter)
enter_btn.grid(row=3, column=2)

root.mainloop()

typ1 = [('テキストファイル', '*.txt')]
dir1 = 'C:/Users/Desktop'
inp_file = filedialog.askopenfilename(title='Input file', filetypes=typ1, initialdir=dir1)

out_file = filedialog.askopenfilename(title='Output file', filetypes=typ1, initialdir=dir1)

with open(inp_file) as f:
    lines = f.readlines()

i = 0
z = 0

while i < len(lines):
    lines[i] = lines[i].replace('\n', '')
    while lines[i] == '':
        z += 1

    else:
        lines[i] = h + lines[i] + o
    lines[i] = lines[i] + '\n'
    print(lines[i])
    i += 1

with open(out_file, 'w') as ff:
    ff.writelines(lines)

print('空白行:', z)
