import fitz
import logging
import base64
import os
import pyaes, pbkdf2, binascii, os, secrets
from python.prohibition_web_svc.config import Config

enc_password_salt = Config.ENCRYPT_KEY_SALT
enc_password = Config.ENCRYPT_KEY




def method2_encrypt(plaintext):
    logging.debug(f'salt: {enc_password_salt}')
    password = enc_password
    passwordsalt = bytes(enc_password_salt, 'utf-8')
    key = pbkdf2.PBKDF2(password, passwordsalt).read(32)
    iv = secrets.randbits(256)
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    ciphertext = aes.encrypt(plaintext)
    iv_encoded = base64.b64encode(iv.to_bytes((iv.bit_length() + 7) // 8, 'big')).decode('utf-8')
    return ciphertext,iv_encoded

def method2_decrypt(ciphertext,iv):
    password = enc_password
    passwordsalt = bytes(enc_password_salt, 'utf-8')
    key = pbkdf2.PBKDF2(password, passwordsalt).read(32)
    iv = int.from_bytes(base64.b64decode(iv), 'big')
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
    decrypted = aes.decrypt(ciphertext)
    # converrt bytes to string
    decrypted = decrypted.decode('utf-8')
    return decrypted


def encryptPdf_method1(pdfPath, password,outfile):
    doc = fitz.open(pdfPath)
    doc.save(outfile, encryption=fitz.PDF_ENCRYPT_AES_256, owner_pw=password, user_pw=password)
    doc.close()

def decryptPdf_method1(pdfPath, password,outfile):
    doc = fitz.open(pdfPath)
    if doc.authenticate(password):
        doc.save('decrypted.pdf')

        if doc.save:
            print("PDF decrypted")
    else:
        print('Incorrect Password')
    doc.close()