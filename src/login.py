import user_registration

def log_in(username, password):
    information = user_registration.load_csv()
    hashed = user_registration.hash_password(password)
    for user in information:
        if user["username"] == username and user["password"] == hashed:
            return True
    return False