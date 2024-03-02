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
        print("File deleted successfully.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")

def main():
    file_path = input("Enter the path of the file to delete: ")
    
    # Check access and existence of the file
    access_info = check_access_and_existence(file_path)
    
    # If the file exists and is accessible, delete it
    if access_info['existence'] and access_info['writability']:
        delete_file(file_path)
    else:
        print("File cannot be deleted. Check if the path exists and you have the necessary permissions.")

if __name__ == "__main__":
    main()
