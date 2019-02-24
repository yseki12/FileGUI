from tkinter import messagebox, filedialog,  simpledialog
from tkinter import *
import subprocess

class FileOpen:
    
    def __init__(self, master):
        
        self.file_path = StringVar()
        self.v = IntVar()
        self.msg_complete = StringVar()
        
        self.label_choosefile = Label(root, text = 'Please choose a file: ').grid(row = 0, column = 0)
        self.button_browser = Button(root, text = 'Browse', command = self.importFile).grid(row = 0, column = 1)
        self.label_filepath = Label(root, textvariable = self.file_path).grid(row=1, column =0, columnspan = 2, sticky = W+E)
        self.label_blank = Label(root, textvariable = self.msg_complete).grid(row=6, sticky = W)
        self.button_submit = Button(root, text = 'Submit', command = self.processFile).grid(row = 7, column = 1, sticky = E)
        self.button_exit = Button(root, text = 'Exit', command = master.destroy).grid(row = 7, column = 0, sticky = W)

        self.rb1 = Radiobutton(root, text="Action One", variable=self.v, value=1).grid(row = 2, sticky = W)
        self.rb2 = Radiobutton(root, text="Action Two", variable=self.v, value=2).grid(row = 3, sticky = W)
        self.rb3 = Radiobutton(root, text="Action Three", variable=self.v, value=3).grid(row = 4, sticky = W)
        self.rb4 = Radiobutton(root, text="Action Four", variable=self.v, value=4).grid(row = 5, sticky = W)
        self.rb5 = Radiobutton(root, text="Action Five", variable=self.v, value=5).grid(row = 2, column = 1, sticky = W)
        self.rb6 = Radiobutton(root, text="Action Six", variable=self.v, value=6).grid(row = 3,column = 1, sticky = W)
        self.rb7 = Radiobutton(root, text="Action Seven", variable=self.v, value=7).grid(row = 4, column = 1,sticky = W)
        self.rb8 = Radiobutton(root, text="Action Eight", variable=self.v, value=8).grid(row = 5, column = 1,sticky = W)
    
    def importFile(self):
        
        self.msg_complete.set('')
        
        global filename
 
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",
                                      filetypes = (("CSV files","*.csv"),("Excel files", "*.xlsx"), ("Text files", "*.txt"),
                                                   ("All Files","*.*")))
    
        self.file_path.set(filename.split('/')[-1])
    
    def processFile(self):
    
        rb_selection = self.v.get()
        
        if rb_selection == 1:
            if filename == '':
                messagebox.showerror("ERROR", "No File Chosen")
            else:
                subprocess.call(['python', 'hello.py', filename], cwd='./scripts')
                self.msg_complete.set('Finished!')
            
        if rb_selection == 2:
            name = simpledialog.askstring('Name', 'What is your name?')
            self.msg_complete.set('Hello ' + name)

root = Tk()

y = FileOpen(root)

root.mainloop()
