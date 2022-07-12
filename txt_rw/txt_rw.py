from tkinter import filedialog


typ1 = [('テキストファイル', '*.txt')]
dir1 = 'C:/Users/Desktop'
inp_file = filedialog.askopenfilename(title='Input file', filetypes=typ1, initialdir=dir1)
out_file = filedialog.askopenfilename(title='Output file', filetypes=typ1, initialdir=dir1)

with open(inp_file) as f:
    lines = f.readlines()

i = 0
h = input('行頭文字:')
o = input('行末文字:')

while i < len(lines):
    lines[i] = lines[i].replace('\n', '')
    lines[i] = h + lines[i] + o
    lines[i] = lines[i] + '\n'
    i += 1

with open(out_file, 'w') as ff:
    ff.writelines(lines)
