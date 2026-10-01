import customtkinter as ctk

ctk.set_appearance_mode("white")

app = ctk.CTk()
app.title("Login")
app.geometry("500x500")
app.resizable(True, True)

main_frame = ctk.CTkFrame(
    app,
    bg_color="black",
    corner_radius=0
)
main_frame.pack(fill="both", expand=True)

login_frame = ctk.CTkFrame(
    main_frame,
    fg_color="gray"
)
login_frame.pack(pady=80)

login_label = ctk.CTkLabel(
    login_frame,
    text="Login",
    font=("Arial", 32, "bold"),
    text_color="black"
)
login_label.pack(pady=(0, 35))


username_label = ctk.CTkLabel(
    login_frame,
    text="Username",
    font=("Arial", 14),
    text_color="black",
    anchor="w",
    width=300
)
username_label.pack(pady=(0, 5))

username_entry = ctk.CTkEntry(
    login_frame,
    width=300,
    height=45,
    placeholder_text="Enter username"
)
username_entry.pack(pady=(0, 20))


password_label = ctk.CTkLabel(
    login_frame,
    text="Password",
    font=("Arial", 14),
    text_color="black",
    anchor="w",
    width=300
)
password_label.pack(pady=(0, 5))


password_entry = ctk.CTkEntry(
    login_frame,
    width=300,
    height=45,
    placeholder_text="Enter password",
    show="*"
)
password_entry.pack(pady=(0, 25))

login_button = ctk.CTkButton(
    login_frame,
    text="Login",
    width=300,
    height=45,

)
login_button.pack()
text_color = "gray"

app.mainloop()


