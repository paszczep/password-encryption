import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def _fernet(password: str = 'user', salt: str = 'password'):
    salt = bytes(f'{salt}_secret_salt'.encode())
    password = bytes(f'{password}_secret_password'.encode())
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000)
    key = base64.urlsafe_b64encode(kdf.derive(password))
    fernet = Fernet(key)
    return fernet


def encrypt(content: str):
    content = bytes(content.encode())
    encryptor = _fernet()
    token = encryptor.encrypt(content)
    return str(token.decode())


def decrypt(encrypted_content: str):
    decryptor = _fernet()
    decrypted_content = decryptor.decrypt(encrypted_content)
    return str(decrypted_content.decode())
