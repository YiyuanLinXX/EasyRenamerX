import tkinter as tk
from tkinter import filedialog, messagebox, LabelFrame, Label
import os
import re
import shutil

def title_except_prepositions(name, prepositions):
    words = re.split('(_+)', name)
    new_words = []
    for word in words:
        if word.lower() not in prepositions and word.islower():
            new_words.append(word.capitalize())
        else:
            new_words.append(word)
    return ''.join(new_words)

def rename_files_and_folders(root_dir):
    prepositions = {'in', 'on', 'at', 'since', 'for', 'ago', 'before', 'to', 'past', 'till', 'until', 'by', 'under', 'below', 'over', 'above', 'across', 'through', 'into', 'towards', 'onto', 'from', 'of', 'off', 'about'}
    files_to_rename = []
    dirs_to_rename = []

    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        for filename in filenames:
            original_file_path = os.path.join(dirpath, filename)
            new_name = filename.replace(' ', '_')
            new_name = title_except_prepositions(new_name, prepositions)
            new_file_path = os.path.join(dirpath, new_name)
            files_to_rename.append((original_file_path, new_file_path))
        
        if dirpath != root_dir:
            new_dirname = os.path.basename(dirpath).replace(' ', '_')
            new_dirname = title_except_prepositions(new_dirname, prepositions)
            new_dirpath = os.path.join(os.path.dirname(dirpath), new_dirname)
            dirs_to_rename.append((dirpath, new_dirpath))

    for original_path, new_path in files_to_rename:
        shutil.move(original_path, new_path)

    for original_path, new_path in reversed(dirs_to_rename):
        shutil.move(original_path, new_path)

class EasyRenamerXGUI:
    def __init__(self, master):
        self.master = master
        master.title("EasyRenamerX")
        master.geometry("400x200")

        # Set the window icon
        self.set_window_icon(master)

        self.frame = LabelFrame(master, text="EasyRenamerX", padx=10, pady=10)
        self.frame.pack(padx=10, pady=10)

        self.label = tk.Label(self.frame, text="Simplify your file naming")
        self.label.pack()

        self.rename_button = tk.Button(self.frame, text="Choose Folder and Rename", command=self.rename_files_folders)
        self.rename_button.pack(pady=5)

        self.author_label = tk.Label(master, text="Created by Yiyuan Lin - yl3663@cornell.edu", font=("Arial", 8))
        self.author_label.pack(side="bottom")

    def set_window_icon(self, master):
        img = tk.PhotoImage(file='.\icon\EasyRenamerX.png ')
        master.tk.call('wm', 'iconphoto', master._w, img)

    def rename_files_folders(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            rename_files_and_folders(folder_path)
            messagebox.showinfo("Success", "Files and folders have been renamed!")

def main():
    root = tk.Tk()
    gui = EasyRenamerXGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()