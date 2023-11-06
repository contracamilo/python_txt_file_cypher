from tkinter import filedialog, simpledialog, messagebox
from encrypter.utils import get_encrypted_file_path, get_decrypted_file_path


# Cesar Cypher
def caesar_encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            stay_in_alphabet = ord(char) + shift
            if char.islower():
                if stay_in_alphabet > ord('z'):
                    stay_in_alphabet -= 26
                elif stay_in_alphabet < ord('a'):
                    stay_in_alphabet += 26
            elif char.isupper():
                if stay_in_alphabet > ord('Z'):
                    stay_in_alphabet -= 26
                elif stay_in_alphabet < ord('A'):
                    stay_in_alphabet += 26
            result += chr(stay_in_alphabet)
        else:
            result += char
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def encrypt_file(root):
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    shift = simpledialog.askinteger("Input", "Ingresa la complejidad de cifrado de 0 a 25", parent=root, minvalue=0, maxvalue=25)
    if shift is None:
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        encrypted_content = caesar_encrypt(file_content, shift)
        encrypted_file_path = get_encrypted_file_path(file_path)
        with open(encrypted_file_path, 'w', encoding='utf-8') as encrypted_file:
            encrypted_file.write(encrypted_content)
        messagebox.showinfo("Éxito", "Archivo cifrado con éxito.")
    except IOError as e:
        messagebox.showerror("Error", f"Se produjo un error al abrir el archivo: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error: {e}")


def decrypt_file(root):
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    shift = simpledialog.askinteger("Input", "¿Cuál es el la complejidad de cifrado de tu archivo?", parent=root,  minvalue=0, maxvalue=25)
    if shift is None:
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        decrypted_content = caesar_decrypt(file_content, shift)
        decrypted_file_path = get_decrypted_file_path(file_path)
        with open(decrypted_file_path, 'w', encoding='utf-8') as decrypted_file:
            decrypted_file.write(decrypted_content)
        messagebox.showinfo("Éxito", f"Archivo descifrado con éxito.\nGuardado como: {decrypted_file_path}")
    except IOError as e:
        messagebox.showerror("Error", f"Se produjo un error al abrir el archivo: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error: {e}")
