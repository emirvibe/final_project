import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from exceptions import *
import join_logic

class TKWindow:

    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry('900x300')
        self.master.title('')
        self.file_names = []
        self.tree = ttk.Treeview(self.master)
        

    def choose_file(self):
        try:
            filename = askopenfilename()
            if filename in self.file_names:
                raise RecursionError()
            self.file_names.append(filename)
            self.refrash_tree()
        except RecursionError:
            messagebox.showerror('Recursion Error', 'You can select file only once')


    def save(self):
        try:
            file_name = self.fileNameEntry.get()
            join_logic.join(file_name=file_name, file_names=self.file_names)
            self.file_names.clear()
            messagebox.showinfo('OK!', 'OK!')
            for row in self.tree.get_children():
                self.tree.delete(row)
            self.file_names.clear()
            self.fileNameEntry.delete(0, tk.END)
            self.fileNameEntry.insert(0, '')
        except LengthError:
            messagebox.showerror("Length error",'The number of selected files must be greater than 1!!!')
        except NameErrorCustom:
            messagebox.showerror('Name Erroe', 'File name to save are not selected')


    def refrash_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in self.file_names:
            self.tree.insert(parent='', index='end', iid=row,text='', values=(row,), tag='orow')
        self.tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
        self.tree.grid(row=2, column=0, columnspan=5, rowspan=11, padx=10, pady=20)
        

    def clear(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.file_names.clear()


    def delete(self):
        try:
            row = self.tree.selection()[0]
            self.tree.delete(row)
            self.file_names.remove(row)
        except IndexError:
            messagebox.showerror('Error', 'Select item to delete')

    def main_loop(self):
        button_choose = Button(self.master, text='Choose file', command=self.choose_file)
        button_choose.grid(row=2, column=6)
        button_clear = Button(self.master, text='Clear', command=self.clear)
        button_clear.grid(row=4, column=6)
        button_delete = Button(self.master, text='Delete', command=self.delete)
        button_delete.grid(row=6, column=6)
        fileNameLabel = Label(self.master, text='File name to save:', width=15)
        fileNameLabel.grid(row=8, column=6)
        self.fileNameEntry = Entry(self.master, width=20)
        self.fileNameEntry.grid(row=9, column=6)
        button_save = Button(self.master, text='Join files', command=self.save)
        button_save.grid(row=11, column=6)
        self.tree['columns'] = ('path',)
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('path', anchor=W, width=600)
        self.tree.heading("path", text="path", anchor=W)
        self.refrash_tree()
        self.master.mainloop()


if __name__ == '__main__':
    tkwindow = TKWindow()
    tkwindow.main_loop()