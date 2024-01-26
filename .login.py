import pyrebase
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys  # Import the sys module

class FirebaseChat:
    def __init__(self, config):
        self.firebase = pyrebase.initialize_app(config)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()

class UserAuthentication:
    def __init__(self, config):
        self.firebase_chat = FirebaseChat(config)

    def register_user(self, email, password):
        try:
            user = self.firebase_chat.auth.create_user_with_email_and_password(email, password)
            # You can add additional registration logic here, e.g., saving user data to the database
            return True
        except Exception as e:
            print(f"Error in registering user: {e}")
            return False

    def authenticate_user(self, email, password):
        try:
            user = self.firebase_chat.auth.sign_in_with_email_and_password(email, password)
            return True
        except Exception as e:
            print(f"Error in authenticating user: {e}")
            return False

class LoginGUI:
    def __init__(self, master, user_auth):
        self.master = master
        self.user_auth = user_auth
        self.register_mode = False

        master.title("M-TOOL - Login")
        master.configure(bg="black")

        self.email_label = tk.Label(master, text="Email:", fg="green", bg="black", font=("Helvetica", 14))
        self.email_label.pack()

        self.email_entry = tk.Entry(master, bg="black", fg="green", font=("Helvetica", 12), width=40)
        self.email_entry.pack(pady=20)

        self.password_label = tk.Label(master, text="Password:", fg="green", bg="black", font=("Helvetica", 14))
        self.password_label.pack()

        self.password_entry = tk.Entry(master, bg="black", fg="green", font=("Helvetica", 12), show="*", width=40)
        self.password_entry.pack(pady=20)

        self.login_button = tk.Button(master, text="Login", command=self.login, bg="green",
                                      fg="black", font=("Helvetica", 12, "bold"))
        self.login_button.pack()

        self.register_button = tk.Button(master, text="Register", command=self.toggle_register, bg="blue",
                                         fg="white", font=("Helvetica", 12, "bold"))
        self.register_button.pack()

    def toggle_register(self):
        if self.register_mode:
            self.register_mode = False
            self.master.title("VCHAT - Login")
            self.login_button.config(text="Login", bg="green")
            self.register_button.config(text="Register", bg="blue")
        else:
            self.register_mode = True
            self.master.title("VCHAT - Register")
            self.login_button.config(text="Register", bg="blue")
            self.register_button.config(text="Back to Login", bg="green")

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if email and password:
            if self.register_mode:
                if self.user_auth.register_user(email, password):
                    messagebox.showinfo("Success", "Registration successful!")
                    self.toggle_register()  # Switch back to login view after registration
                else:
                    messagebox.showinfo("Error", "Registration failed. Please try again.")
            else:
                if self.user_auth.authenticate_user(email, password):
                    self.master.destroy()
                    subprocess.run(["./.m-tool.sh", email])  # Launch vchat.py with email as an argument
                    sys.exit()  # Add this line to exit the program after vchat.py is closed
                else:
                    messagebox.showinfo("Error", "Invalid email or password.")
        else:
            messagebox.showinfo("Error", "Please enter a valid email and password.")

class ChatWindow:
    def __init__(self, email, firebase_chat):
        self.email = email
        self.firebase_chat = firebase_chat
        self.root = tk.Tk()

        # ... (rest of the ChatWindow code remains the same)

if __name__ == "__main__":
    try:
        firebase_config = {
            "apiKey": "AIzaSyDCXm8RE-8CVX5DTUPkU--MojXxae5jKCU",
            "authDomain": "weblogin-c8ced.firebaseapp.com",
            "databaseURL": "https://weblogin-c8ced-default-rtdb.firebaseio.com",
            "projectId": "weblogin-c8ced",
            "storageBucket": "weblogin-c8ced.appspot.com",
            "messagingSenderId": "615936979044",
            "appId": "1:615936979044:web:2bd4e006c5e974c46c6f71"
        }

        user_auth = UserAuthentication(firebase_config)

        root = tk.Tk()
        login_app = LoginGUI(root, user_auth)
        root.mainloop()

    except KeyboardInterrupt:
        print("Program interrupted by the user.")
    except Exception as e:
        print(f"Error in main: {e}")
