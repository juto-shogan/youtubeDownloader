# import tkinter as tk

# def on_button_click():
#     top = tk.Toplevel()
#     top.title("Pop-out Window")
#     button = tk.Button(top, text="Pop-out Button")
#     button.pack()

#     # Position the Toplevel window next to the main window
#     top.geometry("+%d+%d" % (root.winfo_x() + root.winfo_width(), root.winfo_y()))

# root = tk.Tk()
# button = tk.Button(root, text="Main Button", command=on_button_click)
# button.pack()

# root.mainloop()



# import tkinter as tk
# from tkinter import ttk

# def on_button_click():
#     button.configure(style="popped_out")

# root = tk.Tk()

# # Create styles
# style = ttk.Style()
# style.theme_use("default")
# style.configure("popped_out.TButton", padding=10, relief="raised", background="blue")

# button = ttk.Button(root, text="Button", command=on_button_click)
# button.pack()

# root.mainloop()




# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# # Create a style for all buttons
# style = ttk.Style()
# style.theme_use("default")
# style.configure("TButton", padding=10, relief="groove", background="blue", foreground="white")

# # Create a button using the style
# button = ttk.Button(root, text="Button")
# button.pack()

# root.mainloop()
# import tkinter as tk

# root = tk.Tk()

# button = tk.Button(root, text="Button", bg="blue", fg="white", font=("Arial", 12, "bold"))
# button.pack()

# root.mainloop()


import tkinter as tk

class CustomButton(tk.Button):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(bg="blue", fg="white", font=("Arial", 12, "bold"))

root = tk.Tk()

button = CustomButton(root, text="Button")
button.pack()

root.mainloop()