'''
This module provides functions to interact with files, including reading and writing JSON files and checking file sizes.

'''

import os

def get_by_file_size(file_path, max_size_kb=1000):
    """
    Returns if file is accepted and the size of the file in kilobytes. Default is 1000 KB or 1 MB. 
    TODO: Remove file size output later after troubleshooting. Only keep the boolean value.
    
    Args:
        directory (str): file path to check.
        max_size_kb (int): Maximum file size to allow (in kilobytes). Default is 1000 KB or 1 MB.
    
    Returns:
        bool: True if file is less than or equal to max_size_kb, False otherwise.
        int: The maximum size in bytes.
    """
    max_size_bytes = max_size_kb * 1024
    accept_file = False
    file_size = os.path.getsize(file_path)
    try:
        if file_size <= max_size_bytes:
            accept_file = True


    except OSError as e:
        print(f"Error reading {file_path}: {e}, returning False")

    return accept_file, file_size * 1024

