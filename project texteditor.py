'''import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:
    # variables
    __root = Tk()

    # default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisviewMenu = Menu(__thisMenuBar, tearoff=0)

    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):
        # initialization

        # set icon
        try:
            self.__root.wm_iconbitmap("Notepad.ico")  # GOT TO FIX THIS ERROR (ICON)
        except:
            pass

        # set window size (the default is 300x300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # set the window text
        self.__root.title("TEXT EDITOR")

        # center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        # to make the textarea auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # add controls (widget)

        self.__thisTextArea.grid(sticky=N + E + S + W)

        self.__thisFileMenu.add_command(label="New", command=self.__newFile)
        self.__thisFileMenu.add_command(label="Open", command=self.__openFile)
        self.__thisFileMenu.add_command(label="Save", command=self.__saveFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit", command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)

        self.__thisEditMenu.add_command(label="Cut", command=self.__cut)
        self.__thisEditMenu.add_command(label="Copy", command=self.__copy)
        self.__thisEditMenu.add_command(label="Paste", command=self.__paste)
        self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)

        self.__thisviewMenu.add_command(label="fullscreen", command=self.__thisHeight)
        self.__thisMenuBar.add_cascade(label="view", menu=self.__thisviewMenu)

        self.__thisHelpMenu.add_command(label="About Notepad", command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="about", menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)



    def __quitApplication(self):
        self.__root.destroy()
        # exit()

    def __showAbout(self):
        showinfo("Notepad", "Created by: pardeep (pardeepsaini140@gmail.com)")

    def __openFile(self):

        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if self.__file == "":
            # no file to open
            self.__file = None
        else:
            # try to open the file
            # set the window title
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, "r")

            self.__thisTextArea.insert(1.0, file.read())

            file.close()

    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):

        if self.__file == None:
            # save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                # try to save the file
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()
                # change the window title
                self.__root.title(os.path.basename(self.__file) + " - Notepad")


        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    #def fullscreen(self):
        #self.__thisTextArea.("<<zoom>>")

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):


        # run main application
        self.__root.mainloop()


# run main application
notepad = Notepad(width=600, height=400)
notepad.run()'''

#PROJECT 


from tkinter import *
import os
import tkinter.filedialog
import tkinter.messagebox

root = Tk()
root.iconbitmap('icons/favicon.ico')


root.title("TEXT EDITOR")
#file_name = NONE
root.geometry('800x500')


# all codes goes here


# FILE MENU
def new_file(event=None):
    save_as()
    root.title("Untitled")
    #global file_name
    #file_name = None
    #content_text.delete(1.0, END)



def open_file(event=None):
    input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".txt",
                                                         filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"),
                                                                    ("HTML", "*.html"), ("CSS", "*.css"),
                                                                    ("JavaScript", "*.js")])







def save_as(event=None):
    input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".txt",
                                                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"),
                                                                      ("HTML", "*.html"), ("CSS", "*.css"),
                                                                      ("JavaScript", "*.js")])


def save(event=None):
   # global file_name
   input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".txt",
                                                          filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"),
                                                                     ("HTML", "*.html"), ("CSS", "*.css"),
                                                                     ("JavaScript", "*.js")])

# EDIT MENU
def cut():
    content_text.event_generate("<<Cut>>")




def copy():
    content_text.event_generate("<<Copy>>")



def paste():
    content_text.event_generate("<<Paste>>")



def undo():
    content_text.event_generate("<<Undo>>")



def redo(event=None):
    content_text.event_generate("<<Redo>>")



def selectall(event=None):
    content_text.tag_add('sel', '1.0', 'end')




# about menu
def display_about(event=None):
    tkinter.messagebox.showinfo(
        "About", PROGRAM_NAME + "\nA simple Text Editor made in Python with Tkinter\n -me")


def display_help(event=None):
    tkinter.messagebox.showinfo(
        "Help", "This Text Editor works similar to any other editors.",
        icon='question')


def exit_editor(event=None):
     if tkinter.messagebox.askokcancel("Exit", "Are you sure you want to Quit?"):
            root.destroy()



# adding Line Numbers Functionality
def get_line_numbers():
    output = ''
    if show_line_number.get():
        row, col = content_text.index("end").split('.')
        for i in range(1, int(row)):
            output += str(i) + '\n'
    return output


  #def on_content_changed(event=None):


'''    def toggle_highlight(event=None):
        if to_highlight_line.get():
            highlight_line()
        else:
            undo_highlight()'''


    # ICONS for the compound menu
new_file_icon = PhotoImage(file='icons/new_file.gif')
open_file_icon = PhotoImage(file='icons/open_file.gif')
save_file_icon = PhotoImage(file='icons/save.gif')
cut_icon = PhotoImage(file='icons/cut.gif')
copy_icon = PhotoImage(file='icons/copy.gif')
paste_icon = PhotoImage(file='icons/paste.gif')
undo_icon = PhotoImage(file='icons/undo.gif')
redo_icon = PhotoImage(file='icons/redo.gif')


    # MENU CODES GOES HERE
menu_bar = Menu(root)  # menu begins

file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label='New', accelerator='Ctrl+N', compound='left', image=new_file_icon, underline=0,
                          command=new_file)
file_menu.add_command(label='Open', accelerator='Ctrl+O', compound='left', image=open_file_icon, underline=0,
                          command=open_file)
file_menu.add_command(label="Save", accelerator='Ctrl+S', compound='left', image=save_file_icon, underline=0,
                          command=save)
file_menu.add_command(label="Save As", accelerator='Ctrl+Shift+S', compound='left', underline=0, command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", accelerator='Alt+F4', compound='left', underline=0, command=exit_editor)
menu_bar.add_cascade(label='File', menu=file_menu)
    # end of File Menu

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label='Undo', accelerator='Ctrl + Z', compound='left', image=undo_icon, underline=0,
                          command=undo)
edit_menu.add_command(label='Redo', accelerator='Ctrl+Y', compound='left', image=redo_icon, underline=0,
                          command=redo)
edit_menu.add_separator()
edit_menu.add_command(label='Cut', accelerator='Ctrl+X', compound='left', image=cut_icon, underline=0, command=cut)
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', compound='left', image=copy_icon, underline=0,
                          command=copy)
edit_menu.add_command(label='Paste', accelerator='Ctrl+V', compound='left', image=paste_icon, underline=0,
                          command=paste)
edit_menu.add_separator()
edit_menu.add_separator()
edit_menu.add_command(label='Select All', accelerator='Ctrl+A', compound='left', underline=0, command=selectall)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
    # end of Edit Menu

view_menu = Menu(menu_bar, tearoff=0)
show_line_number = IntVar()
show_line_number.set(1)
view_menu.add_checkbutton(label="Show Line Number", variable=show_line_number)
show_cursor_info = IntVar()
show_cursor_info.set(1)



menu_bar.add_cascade(label='View', menu=view_menu)

    # start of About Menu
about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='About', menu=about_menu)
about_menu.add_command(label='About', underline=0, command=display_about)
about_menu.add_command(label='Help', underline=0, command=display_help)
    # end of About Menu
root.config(menu=menu_bar)

    # adding top shortcut bar and left line number bar
shortcut_bar = Frame(root, height=25)
shortcut_bar.pack(expand='no', fill='x')

    # adding shortcut icons
icons = ('new_file', 'open_file', 'save', 'cut', 'copy', 'paste', 'undo', 'redo')
for i, icon in enumerate(icons):
        tool_bar_icon = PhotoImage(file='icons/{}.gif'.format(icon)).zoom(1, 1)
        cmd = eval(icon)
        tool_bar = Button(shortcut_bar, image=tool_bar_icon, height=35, width=35, command=cmd)
        tool_bar.image = tool_bar_icon
        tool_bar.pack(side='left')

line_number_bar = Text(root, width=4, padx=3, takefocus=0, fg='white', border=0, background='#282828',
                           state='disabled', wrap='none')
line_number_bar.pack(side='left', fill='y')

    # adding the main context Text widget and Scrollbar Widget
content_text = Text(root, wrap='word')
content_text.pack(expand='yes', fill='both')

scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')

    # addind cursor info label
cursor_info_bar = Label(content_text, text='Line: 1 | Column: 1')
cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')


    # handling binding

content_text.bind('<Control-N>', new_file)
content_text.bind('<Control-n>', new_file)
content_text.bind('<Control-O>', open_file)
content_text.bind('<Control-o>', open_file)
content_text.bind('<Control-S>', save)
content_text.bind('<Control-s>', save)
content_text.bind('<Control-Y>',redo )
content_text.bind('<Control-y>',redo )
content_text.bind('<Control-A>',selectall )
content_text.bind('<Control-a>',selectall )

# end
root.protocol('delete window',exit_editor)
root.mainloop()

