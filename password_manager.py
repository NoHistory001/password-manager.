# password_manager.py

from cryptography.fernet import Fernet
import os

# Function to generate a Fernet key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt data
def encrypt_data(key, data):
    cipher = Fernet(key)
    encrypted_data = cipher.encrypt(data)
    return encrypted_data

# Function to decrypt data
def decrypt_data(key, encrypted_data):
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data

def main():
    master_password = input("Enter your master password: ").encode()
    key = generate_key()
    encrypted_master_password = encrypt_data(key, master_password)

    # Create the 'data' directory if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")

    print("Password Manager is ready.")
    while True:
        action = input("Enter 'add', 'get', 'exit': ")

        if action == 'add':
            service = input("Enter the service name: ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            data = f"Service: {service}\nUsername: {username}\nPassword: {password}"
            encrypted_data = encrypt_data(key, data.encode())  # Encode data before encryption
            with open(f"data/{service}.txt", 'wb') as file:
                file.write(encrypted_data)

        elif action == 'get':
            service = input("Enter the service name: ")
            try:
                with open(f"data/{service}.txt", 'rb') as file:
                    encrypted_data = file.read()
                    decrypted_data = decrypt_data(key, encrypted_data)
                    print(decrypted_data.decode())  # Decode data after decryption
            except FileNotFoundError:
                print("Service not found.")

        elif action == 'exit':
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()

