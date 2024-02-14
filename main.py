import sqlite3
import hashlib
import sys


sys.stdout.reconfigure(encoding='utf-8')


def database_connection():
    conn = sqlite3.connect(r'Challenge3\users-challenge.db')
    cursor = conn.cursor()
    cursor.execute("SELECT email, password FROM users")
    data = cursor.fetchall()
    conn.close()
    return data


def decrypt_password(hashed_password):
    with open(r'Challenge3\rockyou.txt', 'r', encoding='utf-8') as file:
        for line in file:
            password = line.strip()
            decryption = hashlib.sha256(password.encode()).hexdigest()
            if decryption == hashed_password:
                return password
    return None


def main():
    db = database_connection()
    
    for email, hashed_password in db:
        decrypted_password = decrypt_password(hashed_password)
        if decrypted_password:
            print(f"For {email} password is {decrypted_password} 👍")
        else:
            print(f"Something went wrong with {email} 👎")
    

if __name__ == "__main__":
    main()
