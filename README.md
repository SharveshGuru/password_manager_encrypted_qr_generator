# Password Manager and an Encrypted QR Code Generator

Project Title: Password Manager and an Encrypted QR Code Generator.
Project Members: S Sharvesh Guru, Sheegan Sri G M, Vishwakanth P, Dharsan S.

## ABSTRACT:

We all know that passwords play an important role in today’s digital world. Without it you can forget about even accessing the internet. Situations may arise when there’s a need for you to share the password to a trusted one. You may trust the person you are sharing to but won’t trust the technology by means which you’re sharing. That’s why our team has come up with an idea to create a password manager and a QR code generator. The QR code will contains the credentials in an encrypted format which can only be decoded by the receiver. In this way, even if somehow your QR code is exposed outside, there would be no need for worrying as it is already encrypted and cannot be misused.

## Features

- Insert, display, and delete credentials for various websites.
- Generate and decode encrypted QR codes containing website credentials.
- Encrypt and decrypt credentials using the Fernet encryption scheme.

## Prerequisites

- Python 3.x
- Required libraries can be installed using the following command:
`pip install mysql-connector-python qrcode opencv-python-headless fuzzywuzzy cryptography`

## Getting Started

1. Clone this repository to your local machine.
    `git clone https://github.com/your-username/password-manager.git`
2. Install the required dependencies as mentioned in the prerequisites.
3. Ensure that you have a MySQL server running with the appropriate credentials and database name as specified in the code.
4. Create a fernet_key.txt file and save your Fernet encryption key in it.
5. Execute the main.py file to launch the program.

## Usage
Follow the on-screen instructions to navigate through the program:

1. View all credentials.
2. View credentials of a specific website.
3. Add new credentials.
4. Remove credentials.
5. Export credentials as an encrypted QR code.
6. Decrypt credentials from an encrypted QR code.

Note: Keep your Fernet key (fernet_key.txt) and database credentials secure.
