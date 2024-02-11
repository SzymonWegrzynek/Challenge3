import sqlite3
import hashlib


def password_from_database(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT email, password FROM users")
    credentials = cursor.fetchall()
    conn.close()
    return credentials


def decrypt_password(password, wordlist):
    with open(wordlist, 'r', encoding='utf-8') as file:
        for line in file:
            password = line.strip()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if hashed_password == password:
                return password
    return None


def main():
    database = r'c:\Users\super\Downloads\users-challenge.db'
    wordlist = r'c:\Users\super\challenge#3\Challenge3\rockyou.txt'

    pass_from_db = password_from_database(database)
    
    for email, password in pass_from_db:
        decrypted_password = decrypt_password(password, wordlist)
        if decrypted_password:
            print(f"For {email} password is {decrypted_password}")
        else:
            print(f"Something went wrong here {email}")


if __name__ == "__main__":
    main()