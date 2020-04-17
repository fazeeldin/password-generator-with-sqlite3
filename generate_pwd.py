from tkinter import *
import db
import string, random
def create_unique_password(pwd_len):
    pwd = ""
    list_chrs = []
    
    x = random.randint(0,25)
    list_chrs.append(string.ascii_uppercase[x])
    x = random.randint(0,25)
    list_chrs.append(string.ascii_lowercase[x])
    x = random.randint(62,95)
    list_chrs.append(string.printable[x])
    x = random.randint(0,9)
    list_chrs.append(string.digits[x])
        
    for n in range(pwd_len.get()-4):
        x = random.randint(0,95)
        list_chrs.append(string.printable[x])
        
    random.shuffle(list_chrs)
    pwd += pwd.join(list_chrs)
    return pwd
    

def database():
    conn = db.db_create_database()
    db.db_create_table(conn)
    pwd = create_unique_password(var)
    db.insert(conn, APPLICATION_NAME=applicationName.get(), EMAIL_ID=emailId.get(), PASSWORD=pwd)
    return pwd

def generate_pwd():
    screen_2 = Toplevel(main_screen)
    screen_2.title("Give inputs")
    screen_2.geometry("200x150")
    
    #pwd = StringVar()
    pwd = database()
    Label(screen_2, text="You password is: ").pack()
    Label(screen_2, text=pwd, bg='white', font=('Calibri',13)).pack()
    applicationEntry.delete(0, END)
    emailIdEntry.delete(0, END)

def main():
    global var
    global main_screen
    global applicationName, emailId, applicationEntry, emailIdEntry
    main_screen = Tk()
    main_screen.geometry("450x400")
    main_screen.title("Password Generator")
    Label(text="Password Generator", bg="grey", width="350", height="2", font=('Calibri',13)).pack()
    Label(text="Password Length: ", font=("Calibri", 13)).pack()
    var = IntVar()
    scale = Scale(main_screen, variable=var, from_ = 8, to_ = 21, font=("Calibri", 13),orient = HORIZONTAL, tickinterval=13).pack()
    Label(text="").pack()
    
    applicationName = StringVar()
    emailId = StringVar()
    Label(main_screen, text="Application Name: *", font=("Calibri", 13)).pack()
    applicationEntry = Entry(main_screen, textvariable=applicationName)
    applicationEntry.pack()
    Label(main_screen, text="Email Id: *", font=("Calibri", 13)).pack()
    emailIdEntry = Entry(main_screen, textvariable=emailId)
    emailIdEntry.pack()
    Label(text="").pack()
    
    Button(text="Generate Password", font=("Calibri", 13), height="2", width="30"
          ,command=generate_pwd).pack()
    
    main_screen.mainloop()

main()