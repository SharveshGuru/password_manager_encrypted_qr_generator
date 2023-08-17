from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Create a Fernet object with the key
fernet = Fernet(key)

# Get the password from the user
password = input("Enter your password: ")

# Convert the password to bytes
password_bytes = password.encode()

# Encrypt the password
encrypted_password = fernet.encrypt(password_bytes)
print("Encrypted password:", encrypted_password)

# Decrypt the password
decrypted_password = fernet.decrypt(encrypted_password)

# Convert the decrypted password back to a string
decrypted_password_str = decrypted_password.decode()
print("Decrypted password:", decrypted_password_str)
