import tkinter as tk,urllib.request

root = tk.Tk()
root.geometry("1280x720")
root.title("Muhammadiyah")
root.configure(bg = "#227C70")
menu = tk.Menu(root)

class barMenu():
    def close():
        exit()


# home menubar
home = tk.Menu(menu, tearoff=0)
home.add_command(label="SignIn")
home.add_command(label="Login")
home.add_command(label="Exit",command=barMenu.close)
menu.add_cascade(label="Home",menu=home)

# settings menubar

helpmenu = tk.Menu(menu, tearoff=0)
helpmenu.add_command(label="Tips & Trick")
helpmenu.add_command(label="Documentation")
helpmenu.add_command(label="About")
menu.add_cascade(label="help", menu=helpmenu)

root.config(menu=menu)

# with urllib.request.urlopen("https://id.wikipedia.org/wiki/Muhammadiyah") as response:
#     file = response.read()
label = tk.Label(root,text= "Selamat datang di Muhammadiyah",font =("Roboto",16),bg="#227C70")
label.pack()
root.mainloop()
