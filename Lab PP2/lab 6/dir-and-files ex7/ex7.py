def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            destination.write(source.read())

def main():
    path1 = "/Users/Suleimmen/Desktop/PP 2 lab. works/lab 3/Classes.py"
    path2 = "/Users/Suleimmen/Desktop/PP 2 lab. works/lab 6/dir-and-files ex7/double.txt"
    copy_file(path1, path2)
    print("Contents of the source file have been copied to the destination file.")

if __name__ == "__main__":
    main()

