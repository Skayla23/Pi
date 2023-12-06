import customtkinter 

def enviar():
    pass

def login():
    login = customtkinter.CTkToplevel(fg_color = "lightpink")
    login.title("Login LookChic")
    login.geometry("400x300")
    login.grid_columnconfigure(0, weight=1)
    layout_login = customtkinter.CTkFrame(login, width= 1200, height = 1000, fg_color= "white").place(x=180,y=80)
    nome = customtkinter.CTkLabel(login, width = 1200, height = 1000, font_color = "white",font="Arial")
    entry = customtkinter.CTkEntry(login,width = 200, height = 100)
    entry.pack()
    button = customtkinter.CTkButton(login,width = 200, height = 100,command= enviar).pack(pady= 10)

app = customtkinter.CTk()

#window as a whole
app.title("LookChic")
app.geometry("400x300")
app.grid_columnconfigure(0, weight=1)
customtkinter.set_appearance_mode("set_pink_theme")


#button
button = customtkinter.CTkButton(app, text="Login", command=login)
button.grid(row=0, column=0, padx=80, pady=90, sticky="ew")
app.mainloop()