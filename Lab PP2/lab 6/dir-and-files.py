#ex 1
import os

def list_directories(path):
    dir = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return dir

def list_files(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files

def list_all(path):
    all = os.listdir(path)
    return all

def main():
    path = "/Users/Suleimmen/Desktop/PP 2 lab. works/lab 3/"
    print(f"Directories: {list_directories(path)}")
    print(f"Files: {list_files(path)}")
    print(f"All Directories and Files: {list_all(path)}")

if __name__ == "__main__":
    main()



#ex 2
import os

def check_access(path):
    access_info = {
        'existence': os.path.exists(path),
        'readability': os.access(path, os.R_OK),
        'writability': os.access(path, os.W_OK),
        'executability': os.access(path, os.X_OK)
    }
    return access_info

def main():
    path = "/Users/Suleimmen/Desktop/PP 2 lab. works/lab 3/"
    access_info = check_access(path)

    print(f"Existence: {access_info['existence']}")
    print(f"Readability: {access_info['readability']}")
    print(f"Writability: {access_info['writability']}")
    print(f"Executability: {access_info['executability']}")

if __name__ == "__main__":
    main()



#ex 3
import os

def test_path(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return True, filename, directory
    else:
        return False, None, None
    
def main():
    path = "/Users/Suleimmen/Desktop/PP 2 lab. works/lab 3/Classes.py"
    exists, filename, directory = test_path(path)

    if exists:
        print("Path exists.")
        print("Filename:", filename)
        print("Directory:", directory)
    else:
        print("Path does not exist.")

if __name__ == "__main__":
    main()



#ex 4
def file_length(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
print("Number of lines in the file: ", {file_length("/Users/Suleimmen/Desktop/PP 2 lab. works/lab 6/bultin-functions.py")})



