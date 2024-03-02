import os

def check_access_and_existence(path):
    access_info = {
        'existence': os.path.exists(path),
        'readability': os.access(path, os.R_OK),
        'writability': os.access(path, os.W_OK)
    }
    return access_info

def delete_file(path):
    try:
        os.remove(path)
        print("File deleted.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")

def main():
    path = "/Users/Suleimmen/Desktop/PP 2 lab. works/lab 6/dir-and-files ex8/delete.py"
    access_info = check_access_and_existence(path)
    if access_info['existence'] and access_info['writability']:
        delete_file(path)
    else:
        print("File cannot be deleted.")

if __name__ == "__main__":
    main()
