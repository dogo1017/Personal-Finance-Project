import hashlib
import csv
import os

def hash_password(password):
    mixer = hashlib.shake_128()
    mixer.update(password.encode("utf-8"))
    return mixer.hexdigest(4)

def register(users, password, username):
    hex_password = hash_password(password)
    users.append({"username": username, "password": hex_password})
    return users

def load_csv():
    os.makedirs("docs", exist_ok=True)
    if not os.path.exists("docs/users.csv"):
        with open("docs/users.csv", "w", newline="") as f:
            csv.writer(f).writerow(["username", "password"])
    with open("docs/users.csv", "r") as user_list:
        content = csv.reader(user_list)
        rows_raw = list(content)
    if len(rows_raw) <= 1:
        return []
    headers = rows_raw[0]
    rows = []
    for line in rows_raw[1:]:
        if len(line) >= 2:
            rows.append({headers[0]: line[0], headers[1]: line[1]})
    return rows

def username_exists(username):
    users = load_csv()
    for user in users:
        if user["username"] == username:
            return True
    return False

def save_changes(users):
    fieldnames = ["username", "password"]
    with open("docs/users.csv", "w", newline="") as user_list:
        writer = csv.DictWriter(user_list, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)

def init_user_folder(username):
    os.makedirs(f"docs/{username}", exist_ok=True)