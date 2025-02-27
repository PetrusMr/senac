from tkinter import *
from tkinter import ttk




root = Tk()

style = ttk.Style(root)
style.theme_use('clam')
style.configure("Treeview", background="black", 
                fieldbackground="black", foreground="white")


columns = ('first_name', 'last_name', 'email', 'a')

tree = ttk.Treeview(root, columns=columns, show='headings',)

tree.pack()

tree.heading('first_name', text='First Name', )
tree.heading('last_name', text='Last Name')
tree.heading('email', text='Email')



tree.column("first_name", width=70)



root.mainloop()