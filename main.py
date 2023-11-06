import tkinter as tk
from tkinter import ttk

from encrypter.encrypter import encrypt_file, decrypt_file


def main():
    # UI
    root = tk.Tk()
    root.title("Cifrador / Descifrador de archivos de texto")
    root.geometry("420x300")

    style = ttk.Style()
    style.configure("TButton", font=('Helvetica', 14), padding=(20, 10))
    encrypt_button = ttk.Button(root, text="Carga Archivo para cifrado", style="TButton", command=lambda: encrypt_file(root))
    encrypt_button.pack(expand=True,padx=10, pady=10)

    decrypt_button = ttk.Button(root, text="Carga Archivo a descrifrar.",  style="TButton", command=lambda: decrypt_file(root))
    decrypt_button.pack(expand=True, padx=10, pady=10)

    root.mainloop()


if __name__ == '__main__':
    main()
