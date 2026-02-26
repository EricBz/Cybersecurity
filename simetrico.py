from cryptography.fernet import Fernet

# Generar clave y crear objeto cifrador
key = Fernet.generate_key()
cipher = Fernet(key)

# Cifrar
texto = b"Mensaje confidencial"
token = cipher.encrypt(texto)

# Descifrar

decrypted_text = cipher.decrypt(token)

print(token)
print(decrypted_text)