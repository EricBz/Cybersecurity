import hashlib

with open(r"C:\Users\eric_\Documents\FTPserver\gato.jpg", "rb") as f:
    digest = hashlib.file_digest(f, "sha256")
print(digest.hexdigest())
