import os
from tkinter import *
arr = os.listdir('.')


def hide_all():
    my_file = open("hide.bat", 'a')
    for i in arr:
        if i != 'desktop.ini':
            my_file.write(f'attrib +h +s "{i}"\n')
        else:
            pass
    my_file.write('cls')
    my_file.close()
    os.system('hide.bat')
    os.system('del hide.bat')
    if var.get() == 1:
        root.quit()
    elif var.get() == 0:
        pass


def un_hide_all():
    my_file2 = open("un_hide.bat", 'a')
    for i in arr:
        if i != 'desktop.ini':
            my_file2.write(f'attrib -h -s "{i}"\n')
        else:
            pass
    my_file2.write('cls')
    my_file2.close()
    os.system('un_hide.bat')
    os.system('del un_hide.bat')
    if var.get() == 1:
        root.quit()
    elif var.get() == 0:
        pass


root = Tk()
root.title("Hide & Un_hide")
root.geometry("500x200")
fr1 = Frame(root)
fr1.pack()
hide_btn = Button(fr1, width="8", height="3", text="Hide", font=('Times New Roman', 12), bg='gold',
                  command=hide_all)
hide_btn.grid(row=1, column=1, padx=50, pady=30)
un_hide_btn = Button(fr1, width=8, height=3, text="Un_Hide", font=('Times New Roman', 12), bg='gold',
                     command=un_hide_all)
un_hide_btn.grid(row=1, column=2, padx=50, pady=30)
var = IntVar()
chk1 = Checkbutton(root, text="Close the window after action", font=('Consolas', 10), variable=var)
chk1.pack()
root.mainloop()
