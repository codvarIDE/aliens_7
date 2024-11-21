from cryptography.fernet import Fernet

def encrypt_text_with_keys(text):
    words = text.split()
    keys = []
    encrypted_words = []
    
    for word in words:
        key = Fernet.generate_key()  
        keys.append(key)           
        cipher = Fernet(key)
        encrypted_words.append(cipher.encrypt(word.encode()))
    
    return encrypted_words, keys 

def decrypt_text_with_keys(encrypted_words, keys):
    decrypted_words = []
    
    for encrypted_word, key in zip(encrypted_words, keys):
        cipher = Fernet(key)
        decrypted_words.append(cipher.decrypt(encrypted_word).decode())
    
    return ' '.join(decrypted_words)


