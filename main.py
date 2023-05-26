import tkinter as tk
from tkinter import filedialog, Scrollbar
import os

current_file = None
def undo():
    text_editor.edit_undo()

def redo():
    text_editor.edit_redo()

def new_file():
    os.startfile("main.py")

def open_file():
    global current_file
    path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if path:
        with open(path, "r") as file:
            content = file.read()
            text_editor.insert('1.0', content)
            current_file = path
    window.title(f"Notepad Pro - {path}")

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            content = text_editor.get("1.0", tk.END)
            file.write(content)
    else:
        save_file_as()

def save_file_as():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            content = text_editor.get("1.0", tk.END)
            file.write(content)
        current_file = file_path
def cut():
    text_editor.event_generate("<<Cut>>")

def copy():
    text_editor.event_generate("<<Copy>>")

def paste():
    text_editor.event_generate("<<Paste>>")
# def find_text():
    # search_term = find_entry.get()
    # start_index = text_editor.index(tk.INSERT)
    # match_index = text_editor.search(search_term, start_index, stopindex=tk.END)
    # if match_index:
        # text_editor.tag_remove("highlight", "1.0", tk.END)
        # match_end = match_index + f"+{len(search_term)}c"
        # text_editor.tag_add("highlight", match_index, match_end)
        # text_editor.see(match_index)
        # text_editor.focus_set()
    # else:
        # tk.messagebox.showinfo("Find", "No match found.")



window = tk.Tk()
window.title("Notepad Pro")

menu_bar = tk.Menu(window)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_file_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)

edit_menu = tk.Menu(menu_bar, tearoff=1)
edit_menu.add_command(label="Undo",command=undo)
edit_menu.add_command(label="Redo",command=redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut",command=cut)
edit_menu.add_command(label="Copy",command=copy)
edit_menu.add_command(label="Paste",command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Find")
edit_menu.add_command(label="Replace")
menu_bar.add_cascade(label="Edit", menu=edit_menu)


text_editor = tk.Text(window)
text_editor.grid(row=0, column=0, sticky="nsew")

scrollbar = Scrollbar(window, command=text_editor.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

text_editor.config(yscrollcommand=scrollbar.set)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

window.mainloop()