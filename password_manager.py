import password_logic as pl

while True:
    mode = input("Add or view passwords? (add/view/q): ").lower()
    if mode == 'q':
        break
    elif mode == 'add':
        name = input("Account name: ")
        pwd = input("Password: ")
        pl.add_password(name, pwd)
    elif mode == 'view':
        for acc, pw in pl.get_all_passwords():
            print(f"Account: {acc} | Password: {pw}")
