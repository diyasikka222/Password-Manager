from cryptography.fernet import Fernet

def load_key():
    with open("key.key", "rb") as file:
        return file.read()

key = load_key()
fer = Fernet(key)

def encrypt_password(pwd):
    return fer.encrypt(pwd.encode()).decode()

def decrypt_password(encrypted_pwd):
    return fer.decrypt(encrypted_pwd.encode()).decode()

def add_password(account, pwd):
    with open('passwords.txt', 'a') as f:
        f.write(account + "|" + encrypt_password(pwd) + "\n")

def get_all_passwords():
    results = []
    try:
        with open('passwords.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if "|" in line:
                    user, encrypted = line.split("|")
                    decrypted = decrypt_password(encrypted)
                    results.append((user, decrypted))
    except Exception as e:
        print("Error:", e)
    return results
