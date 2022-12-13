import tkinter as tk,urllib.request
root = tk.Tk()
with urllib.request.urlopen("https://muhammadiyah.or.id/sejarah-muhammadiyah/") as response:
    file = response.read()
label = tk.Label(root, text=file)
label.pack()
root.mainloop()
