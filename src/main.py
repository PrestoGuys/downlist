import subprocess

from tkinter import Menu
from tkinter import filedialog
from tkinter import ttk
from tkinter import Listbox
from tkinter import StringVar

from ttkthemes import ThemedTk

from threading import Thread

from PySmaz import compress, decompress

# CHECK VERSION: https://prestoguys.github.io/project-version-id-database/Versions/DownList.txt

def Axel_Download():
    progressbar.start()
    subprocess.run("./Assets/axel-2-17-11 https://ia800100.us.archive.org/28/items/test-image-1-for-download-list/Test.png", shell=True)
    progressbar.stop()



if __name__ == '__main__':



    def make_download_list_file():
        '''
        fi = open('listy.json', 'r')
        f = open('demofile3.downlist', 'w')
        f.write(compress(fi.read()))
        f.close()

        # open and read the file after the overwriting:
        f = open('demofile3.downlist', 'r')
        print(f.read())
        f.close()

        '''



    def open_download_list_file():
        file_types = [('DownList Files', '*.downlist')]
        file_path = filedialog.askopenfilename(filetypes=file_types)

        print('Path: ' + file_path)

        f = open(file_path, "r")
        print(decompress(f.read()))
        f.close()


    make_download_list_file()



    build_version = "1"
    version = "Beta 1"

    theme = "breeze" # elegance, keramik, clearlooks, aqua, breeze, breeze-dark, arc
    title = 'DownList ' + version + ' *UNSTABLE, DO NOT USE*'

    window_width = 1000
    window_height = 720


    window = ThemedTk(theme=theme)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    window.configure(bg='#EFF0F1')
    window.title(title)


    # create a menubar
    Menu_Bar = Menu(window, bg="#e4e6e8", fg="#030303", activebackground="#9AD4E9", activeforeground="#030303")
    window.config(menu=Menu_Bar)

    # create the file_menu
    file_menu = Menu(Menu_Bar, bg="#EFE7E7", fg="#030303", activebackground="#F6F1F1", activeforeground="#030303",tearoff=0)

    # add menu items to the File menu
    file_menu.add_command(label='Open List...', command=open_download_list_file)
    file_menu.add_command(label='Open...')
    file_menu.add_command(label='Exit')
    file_menu.add_separator()

    # add a submenu
    sub_menu = Menu(file_menu, tearoff=0)
    sub_menu.add_command(label='Keyboard Shortcuts')
    sub_menu.add_command(label='Color Themes')

    # add the File menu to the menubar
    file_menu.add_cascade(
        label="Preferences",
        menu=sub_menu
    )

    # add Exit menu item
    file_menu.add_separator()
    file_menu.add_command(
        label='Exit',
        command=window.destroy
    )

    Menu_Bar.add_cascade(
        label="File",
        menu=file_menu,
        underline=0
    )
    # create the Help menu
    help_menu = Menu(
        Menu_Bar, bg="#EFE7E7", fg="#030303", activebackground="#F6F1F1", activeforeground="#030303",
        tearoff=0
    )

    help_menu.add_command(label='Welcome')
    help_menu.add_command(label='About...')

    # add the Help menu to the menubar
    Menu_Bar.add_cascade(
        label="Help",
        menu=help_menu,
        underline=0
    )

    # subprocess.run("", shell=True)


    # progressbar
    progressbar = ttk.Progressbar(
        window,
        orient='horizontal',
        mode='indeterminate',
        length=950
    )

    # start button
    start_button = ttk.Button(
        window,
        text='Start',
        command=progressbar.start
    )

    stop_button = ttk.Button(
        window,
        text='Stop',
        command=progressbar.stop
    )


    def ffa():
        Thread(target=Axel_Download).start()


    ff = ttk.Button(
        window,
        text='Stop',
        command=ffa
    )

    label = ttk.Label(window, text='DownList Beta 1 *UNSTABLE, DO NOT USE* - PrestoGuys Software')

    var2 = StringVar()
    var2.set((1, 2, 3, 4))
    lb = Listbox(window, width=142, height=30, listvariable=var2) # font=('JetBrainsMono', 50)

    list_items = [11, 22, 33, 44]
    for item in list_items:
        lb.insert('end', item)
    lb.insert(1, 'first')
    lb.insert(2, 'second')
    lb.delete(2)
    lb.place(x=0, y=0)

    ttk.Button(window, text="Exit", command=window.destroy).place(x=900, y=682)
    start_button.pack()
    stop_button.pack()
    label.place(x=10, y=700)

    progressbar.place(x=20, y=460)

    ff.pack()

    window.mainloop()
