import os

def get_encrypted_file_path(original_path):
    file_name, file_extension = os.path.splitext(original_path)
    encrypted_file_name = f"{file_name}.cph{file_extension}"
    return encrypted_file_name


def get_decrypted_file_path(encrypted_path):
    file_name, file_extension = os.path.splitext(encrypted_path)
    decrypted_file_name = f"{file_name}.dcph{file_extension}"
    return decrypted_file_name
