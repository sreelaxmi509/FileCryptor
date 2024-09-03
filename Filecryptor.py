import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import base64
from PIL import Image, ImageTk
from tkinter import Tk
from tkinter import PhotoImage
import io
import tempfile
import os
import pkg_resources
import smtplib
import webbrowser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Cryptodome.Random import get_random_bytes
from cryptography.fernet import Fernet, InvalidToken
import tempfile
import importlib.metadata as pkg_resources
# Example:
#Image to base 64 Conversion 
icon_path= 'image.jpg'
base64_icon ='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/nt+vJnz59Gk+YZWVTq1arenra1+Ddtra4Sxa9t+OpvY7d28xeYu1Tu4cJm/gQ8/jlxk8YnJmzu3uHzU8+nUeUavjj17vuittHv/vo47+PHkv4kvjz49tPPq27s3xv69/Pm24tO/jx+U/fz8+0++7l+AAkay34AGHjhIgQguGKCCDD6In4MQTviehBReiJ6FGG74nYYcflidhyCO2JyIJJ4onIkornibiiy++JqLMM5Imow03piZjTjuGJmOPP6YmI9ADhmYkEQeaZeRSC7JGoBMPrmYklBO+ZWUVF55lZVYbombk1x+2eRyYI7ZlpZknpmTmWiuGZOabL6Zkptw/s4Zkpx03pmRnXjuqZGXfP6Jk56ADjqQoIQe6o+hiC56l5+MPuqRopBOio6klF5qnqOYbmqdmJx+upCloI7ajKiknoqMqaiuypSmrL6ajqqwzkqLrLTe+oqtuO7qia68/pqJr8AOS4mwxB77iLHILquIssw+W4iz0E4r7bTPVmvtsthme+y23A7r7be/hivuruSWe+u56M6q7rqvtuvuqvDGe+q89I5q772f5qvvpvz2e+m/AE8q8MCPFmzwoggnfOjCDA/q8MN/RizxnhRXfOfFGM+p8cZvduzxmiCHfObIJI9p8slfpqzyliy3fOXLME8p88xP1mzzkjjnfOTO5TwP6fPPPwYt9I5EF33j0UjPyF3TTj8NddRST0111VZfjXXWWm/Ndddefw122GKPTXbZZp+Ndtpqr812226/DXfccs9Nd91234133nrvzXfffv8NeOCCD0544YYfjnjiii/OeOOOPw555JJPTnnlll+Oeeaab855555/Dnrooo9Oeummn4566qqvznrrrr8Oe+yyz0577bbfjnvuuu/Oe+++/w588MIPT3zxxh+PfPLKL898884/D3300k9PffXWX4999tpvz3333n8Pfvjij09++eafj3766q/Pfvvuvw9//PILEwgAIfkEBDIAAAAsygDsAGoBfwAAB/6AV4IvElWGVQCJiouMjY6PkJGSk5SVlpeYmZqbnJ2en6ChiYIxhwAcHT6Cq6ytrq+wsbKztLW2t7i5uru8vb6/wMHCqy6Gpz/DycrLzM3Oz9DR0qsyxlPT2Nna29zd3sHGVN/j5OXm5+i3iELp7e7v8PHCVRzy9vf4+e4AyPr+/wADKgMisKDBgwhd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'
icon_data = base64.b64decode(base64_icon)
root = tk.Tk()
icon_image = PhotoImage(data=icon_data)
root.iconphoto(True, icon_image)
root.title("File Encrypt Decrpyt")
root.geometry("600x500")
window_width = 600
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2)- (window_width / 2))
y = int((screen_height / 2)- (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg='black')
button_frame = tk.Frame(root, bg='black')
button_image = None

def project_info():
    html_code = """

    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    h1{
        color: brown;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h2{
        font-style: normal;
    }
    h3{
        color:black;
    }
    body{
        background-color: papayawhip;
    }
    table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}
th{
    background-color:#dddddd;

}

</style>
<body>
  
    <h1>Project Information</h1>
    <h2>This project was developed by team 3 as a part of Cyber Security Internship.This project is designed to secure the organizations in Real World from Cyber Frauds performed by Hackers</h2>

        <table>
            <tr>
              <th>Project Details</th>
              <th>Values</th>
          
            </tr>
            <tr>
              <td>Project Name</td>
              <td>File Cryptor</td>
           
            </tr>
            <tr>
              <td>Project Description</td>
              <td>Implementing Secured Encryption for files which contains Sensitive Data using SMTP Password</td>
             
            </tr>
            <tr>
              <td>Project Start Date</td>
              <td>18-DEC-2023</td>
            
            </tr>
            <tr>
              <td>Project End Date</td>
              <td>23-DEC-2023</td>
           
            </tr>
            <tr>
              <td>Project Status</td>
              <td>Completed</td>
          
            </tr>
            
          </table>
          <h3>Developer Details</h3>
          <table>
            <tr>
              <th>Name</th>
              <th>Email</th>
          
            </tr>
            <tr>
              <td>Sunchu Swamy</td>
              <td>swamisunchu95@gmail.com</td>
           
            </tr>
            <tr>
              <td>Rakshitha Pedduri</td>
              <td>akshipedduri07@gmail.com</td>
             
            </tr>
            <tr>
              <td>K Neeha Akhila Sri</td>
              <td>neeha8689@gmail.com/td>
            
            </tr>
            <tr>
              <td>Shreza Cheripally</td>
              <td>shrezacheripally@gmail.com</td>
           
            </tr>
            <tr>
              <td>Harshitha Vagicherla</td>
              <td>vasaviharshitha224@gmail.com</td>
          
            </tr>
            <tr>
              <td>Kassa Sree Laxmi</td>
              <td>ssrilaxmi561@gmail.com</td>
          
            </tr>

            
          </table>
    <table>
        <h3>Company Details</h3>
            <tr>
              <th>Company</th>
              <th>Contact Mail</th>
          
            </tr>
            <tr>
              <td>Supraja Technologies</td>
              <td>contact@suprajatechnologies.com</td>
           
            </tr>
            
            
          </table>
</body>
</html>
    """

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.html') as temp_file:
        temp_file.write(html_code)
        temp_file_path  = temp_file.name

    webbrowser.open('file://' +os.path.realpath(temp_file_path))


def button1_clicked():
    global file_window
    file_window = tk.Toplevel(root)
    file_window.geometry("560x200")
    file_window.title("Select File")

    filepath_label = tk.Label(file_window, text="file Path")
    email_label =tk.Label(file_window,text="Sender Email")
    smtp_label = tk.Label(file_window,text="SMTP Password")
    receiver_label = tk.Label(file_window,text="Receiver Email")

    filepath_entry = tk.Entry(file_window,width=60)
    email_entry = tk.Entry(file_window, width=60)
    smtp_entry = tk.Entry(file_window,width=60,show="*")
    receiver_entry = tk.Entry(file_window, width=60)


    def browse_file():
        file_path = filedialog.askopenfilename()
        filepath_entry.delete(0, tk.END)
        filepath_entry.insert(0, file_path)

    global button_image

    browse_button = tk.Button(file_window, text="Browse Files", command=browse_file)

    def encrypt_file():
        filepath = filepath_entry.get()
        sender_email = email_entry.get()
        receiver_email = receiver_entry.get()
        smtp_password = smtp_entry.get()
        if filepath == '':
            messagebox.showerror("Error", "Please select a file to encrypt.")
            return
        if not os.path.exists(filepath):
            messagebox.showerror("Error","Invalid file path.")
            return
        key = Fernet.generate_key()
        fernet = Fernet(key)
        
        if os.path.isfile(filepath):
            with open(filepath, 'rb') as file:
                data = file.read()

            encrypted_data = fernet.encrypt(data)

            with open(filepath, 'wb') as file:
                file.write(encrypted_data)

        sender_email = sender_email
        receiver_email = receiver_email
        subject = 'The Key for Encrypted file'
        message = 'The Key for Encrypted file' + filepath + ' is:\n'+str(key)
        
        #smtp server configuration
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = sender_email
        smtp_password = smtp_password
        
        # multipart message object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        #connect to smtp server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        try:
            server.login(smtp_username, smtp_password)
        except smtplib.SMTPAuthenticationError:
            messagebox.showerror("Error","Wrong SMTP Password")
            return
            
        server.send_message(msg)
        server.quit()
        messagebox.showinfo("Info","file encrypted successfully.")

    encrypt_button = tk.Button(file_window,text="Encrypt File", font=("Arial", 14 , "bold"),bg ="grey", fg="black",command=encrypt_file)

    #arrange the widgets using grid
    filepath_label.grid(row=0, column=0, sticky=tk.E)
    filepath_entry.grid(row=0,column=1)
    browse_button.grid(row=0, column=2)
    email_label.grid(row=1,column=0)
    email_entry.grid(row=1,column=1)
    smtp_label.grid(row=2, column=0)
    smtp_entry.grid(row=2,column=1)
    receiver_label.grid(row=3,column=0)
    receiver_entry.grid(row=3,column=1)
    encrypt_button.grid(row=4, column=1)

    #center the widgets
    file_window.grid_rowconfigure(0, weight=0)
    file_window.grid_columnconfigure(1, weight=10)
    filepath_label.grid(padx=10,sticky="e")
    filepath_entry.grid(pady=10,sticky="w")
    browse_button.grid(padx=10,pady=2, sticky="w")
    email_label.grid(padx=10,sticky="w")
    email_entry.grid(pady=10,sticky="w")
    smtp_label.grid(padx=10,sticky="w")
    smtp_entry.grid(pady=10,sticky="w")
    receiver_label.grid(padx=10,sticky="w")
    receiver_entry.grid(pady=10,sticky="w")
    encrypt_button.grid(padx=100,sticky="w")

    file_window.grab_set()
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Tk
from tkinter import PhotoImage
def button2_clicked():
    global file_window
    file_window = tk.Toplevel(root)
    file_window.geometry("560x200")
    file_window.title("Select File")

    filepath_label = tk.Label(file_window, text="file Path")
    password_label =tk.Label(file_window,text="Password")

    filepath_entry = tk.Entry(file_window,width=60)
    password_entry = tk.Entry(file_window,width=60,show="*")


    def browse_file():
        file_path = filedialog.askopenfilename()
        filepath_entry.delete(0, tk.END)
        filepath_entry.insert(0, file_path)

    global button_image

    browse_button = tk.Button(file_window, text="Browse Files", command=browse_file)


    def decrpyt_file():
        filepath = filepath_entry.get()
        password = password_entry.get()
        if filepath == '':
            messagebox.showerror("Error","Please select a file to encrypt")
            return
        if not os.path.exists(filepath):
            messagebox.showerror("Error", "Please Enter a password")
            return
        if password == '':
            messagebox.showerror("Error","Please Enter a Password")
            #loading_window.destroy()
            return
        try:
            key = bytes(password.encode())
            key = key[2:-1]
            try:
                fernet = Fernet(key)

                if os.path.isfile(filepath):
                    with open(filepath, 'rb') as file: 
                        encrypted_data =file.read()

                    decrpyted_file = fernet.decrypt(encrypted_data)

                    with open(filepath, 'wb') as file:
                         file.write(decrpyted_file)
                messagebox.showinfo("Info","file Decrypted Successfully.")
            except InvalidToken:
                messagebox.showerror("Error","Invalid Key. Decrypted failed")
                return
        except:
            messagebox.showinfo("info"," File Already Decrypted successfully.")
    decrpyt_button = tk.Button(file_window, text="Decrypt file", font=("Arial", 14, "bold"), bg="grey", fg="black",command=decrpyt_file)
    
    filepath_label.grid(row=0, column=0, sticky=tk.E)
    filepath_entry.grid(row=0,column=1)
    browse_button.grid(row=0, column=2)
    password_label.grid(row=1,column=0)
    password_entry.grid(row=1,column=1)
    decrpyt_button.grid(row=2,column=1)

    #center the widgets
    file_window.grid_rowconfigure(0, weight=0)
    file_window.grid_columnconfigure(1, weight=10)
    filepath_label.grid(padx=10,sticky="e")
    filepath_entry.grid(pady=10,sticky="w")
    browse_button.grid(padx=10,pady=2, sticky="w")
    password_label.grid(padx=10,sticky="e")
    password_entry.grid(pady=10,sticky="w")
    decrpyt_button.grid(padx=100,sticky="w")

    file_window.grab_set()

info_button = tk.Button(root, text="Project Info", font=("Arial", 14,"bold"),bg="grey", fg="black",command=project_info)
info_button.pack(pady=20)
project_label = tk.Label(root,text="File Encryption And Decrpytion", font=("Arial", 18,"bold"), bg="grey", fg="black")
project_label.pack(pady=25)

background_image_base64 ='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'
background_image_data = base64.b64decode(background_image_base64)
background_image = Image.open(io.BytesIO(background_image_data))
background_image = background_image.resize((200, 150), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image= background_photo)
background_label.pack()

button1 = tk.Button(button_frame, text ="Encrypt Files", font=("Arial", 14, "bold"), padx=10, pady=5,command=button1_clicked, bg="grey", fg="black")
button2 = tk.Button(button_frame, text="Decrypt Files", font=("Arial", 14, "bold"), padx=10, pady=5, command=button2_clicked,bg="grey", fg="black")

button1.pack(side="top", fill="x", padx=50, pady=10)
button2.pack(side="bottom", fill="x", padx=50, pady=10)

button_frame.pack(expand=True)

root.mainloop()
