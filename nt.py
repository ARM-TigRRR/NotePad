from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('NOTEBOOK')
root.geometry('900x650')

main_menu = Menu(root)
root.config(menu=main_menu)


def about_programm():
    messagebox.showinfo(title='About notepad', message='NotePad Version 0.0.1')


def nt_quit():
    answer = messagebox.askokcancel(title='Exit', message='Are you sure you want to close programm?')
    if answer:
        root.destroy()


def open_file():
    file_path = filedialog.askopenfilename(title='Choose file',
                                           filetypes=(('Text documents', '*/txt'), ('all files', '*.*')))
    if file_path:
        t.delete('1.0', END)
        t.insert('1.0', open(file_path, encoding='utf-8').read())


def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Text documents', '*/txt'), ('all files', '*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = t.get('1.0', END)
    f.write(text)
    f.close()


def change_theme(theme):
    t['bg'] = theme_colors[theme]['text_bg']
    t['fg'] = theme_colors[theme]['text_fg']
    t['insertbackground'] = theme_colors[theme]['cursor']
    t['selectbackground'] = theme_colors[theme]['select_bg']


file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=nt_quit)
main_menu.add_cascade(label='File', menu=file_menu)

theme_menu = Menu(main_menu, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label='Light', command=lambda: change_theme("light"))
theme_menu_sub.add_command(label='Dark', command=lambda: change_theme("dark"))
theme_menu.add_cascade(label='Decor', menu=theme_menu_sub)
theme_menu.add_command(label='About us', command=about_programm)
main_menu.add_cascade(label='Different', menu=theme_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

theme_colors = {
    'dark': {
        'text_bg': '#343D46', 'text_fg': '#fff', 'cursor': '#EDA756', 'select_bg': '#4E5A65'
    },
    'light': {
        'text_bg': '#fff', 'text_fg': '#000', 'cursor': '#8000FF', 'select_bg': '#777'
    }
}

t = Text(f_text, bg=theme_colors['light']['text_bg'], fg=theme_colors['light']['text_fg'],
         padx=5, pady=5, wrap=WORD, insertbackground=theme_colors['light']['cursor'],
         selectbackground=theme_colors['light']['select_bg'], width=30, spacing3=10,
         font=('Courier New', 11))
t.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)

root.mainloop()
