import customtkinter 

def enviar():
    pass

def login():
    login_window = customtkinter.CTkToplevel(fg_color="lightpink")
    login_window.title("Login LookChic")
    login_window.geometry("400x300")
    login_window.grid_columnconfigure(0, weight=1)
    
    layout_login = customtkinter.CTkFrame(login_window, width=1200, height=1000, fg_color="white")
    layout_login.place(x=180, y=80)
    
    nome = customtkinter.CTkLabel(layout_login, width=1200, height=100, font=("Arial", 12), fg_color="white")
    nome.pack()
    entry = customtkinter.CTkEntry(layout_login, width=200, height=100)
    entry.pack()

    button = customtkinter.CTkButton(layout_login, width=200, height=100, command=enviar)
    button.pack(pady=10)

app = customtkinter.CTk()

# window as a whole
app.title("LookChic")
app.geometry("400x300")
app.grid_columnconfigure(0, weight=1)
customtkinter.set_appearance_mode("set_pink_theme")

# button
button = customtkinter.CTkButton(app, text="Login", command=login)
button.grid(row=0, column=0, padx=80, pady=90, sticky="ew")

app.mainloop()
