from cryptography.fernet import Fernet
# Fernet is not showing

master_pwd = input("What is the master password? ")

def write_key():
    key = Fernet.generate.key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()        

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", passw)


def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view/add) or press q to quit? ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invaild mode.")
        continue