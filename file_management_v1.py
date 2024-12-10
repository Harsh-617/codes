import os
import shutil
from os.path import exists, join
import logging

# Base directory where files and directories will be created or deleted
base_dir = r"C:\Users\LENOVO-PC\demo_expm"

log_file = join(base_dir,"file_movements.log")
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s- %(message)s')

def make_unique(dest, name):
    # Ensure unique file names by appending a counter if a file with the same name exists
    base, extension = os.path.splitext(name)
    counter = 1
    new_name = name
    while exists(join(dest, new_name)):
        new_name = f"{base}_{counter}{extension}"
        counter += 1
    return new_name

def move_file(dest, entry, name):
    # Move file to the destination, ensuring unique names
    if name == "file_movements.log":
        return #skip moving the log file
    if exists(join(dest, name)):
        unique_name = make_unique(dest, name)
        new_name = join(dest, unique_name)
    else:
        new_name = join(dest, name)

    shutil.move(entry, new_name)  # Move the file
    logging.info(f"Moved '{name}' to '{new_name}'")
    print(f"Moved '{name}' to '{new_name}'")

def segregate_files_by_extension(source_dir):
    # Segregate files based on their extensions into subdirectories within base_dir
    os.makedirs(base_dir, exist_ok=True)  # Ensure the base_dir exists

    for file_name in os.listdir(source_dir):  # Iterate through all files in source_dir
        source_file = os.path.join(source_dir, file_name)         #construct file path

        if file_name == "file_movements.log":
            continue

        if os.path.isfile(source_file):
            file_extension = os.path.splitext(file_name)[1].lstrip('.')  # Extract file extension
            extension_dir = os.path.join(base_dir, file_extension)  # Subdirectory for the file extension

            if not os.path.exists(extension_dir):
                os.makedirs(extension_dir)  # Create the subdirectory if it doesn't exist

            move_file(extension_dir, source_file, file_name)
            logging.info(f"Moved '{file_name}' to '{extension_dir}'")
            print(f"Moved '{file_name}' to '{extension_dir}'")



def create_file_or_dir():
    # Create either a file or directory inside base_dir
    type = input("Enter 'file' to create File or 'dir' to create Directory:\n")

    if type == 'file':
        file_name = input("Enter the name of your file (without extension):\n")
        file_content = input("Enter the content of your file:\n")
        file_path = os.path.join(base_dir, f'{file_name}.txt')  # Full path of the new file

        with open(file_path, 'w') as file:     # Create the file and write content to it
            file.write(file_content)
        logging.info(f"File '{file_name}.txt' created in '{base_dir}'")
        print(f"File '{file_name}.txt' created in '{base_dir}'")

    elif type == 'dir':
        dir_name = input("Enter the name of your directory:\n")
        dir_path = os.path.join(base_dir, dir_name)  # Full path of the new directory

        os.makedirs(dir_path, exist_ok=True)
        logging.info(f"Directory '{dir_name}' created successfully in '{base_dir}'")
        print(f"Directory '{dir_name}' created successfully in '{base_dir}'")

def delete_file_or_dir():
    # Delete either a file or directory inside base_dir
    type = input("Enter 'file' to delete file or 'dir' to delete Directory:\n")

    if type == 'file':
        file_name = input("Enter the name of the file to delete (including extension):\n")
        file_path = os.path.join(base_dir, file_name)  # Construct the full path to the file

        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                logging.info(f"File '{file_name}' deleted successfully from '{base_dir}'")
                print(f"File '{file_name}' deleted successfully from '{base_dir}'")
            except FileNotFoundError:
                print("File not found.")
        else:
            print(f"File '{file_name}' not found in '{base_dir}'")

    elif type == 'dir':
        dir_name = input("Enter the name of the directory to delete:\n")
        dir_path = os.path.join(base_dir, dir_name)  # Construct the full path to the directory

        if os.path.isdir(dir_path):
            if os.listdir(dir_path):  # Check if the directory contains any files
                confirmation = input(
                    f"Directory '{dir_name}' contains files. Do you still want to delete it? Type 'yes' to delete or 'no':\n")
                if confirmation.lower() != 'yes':
                    print("Operation cancelled.")
                    return
            try:
                shutil.rmtree(dir_path)
                logging.info(f"Directory '{dir_name}' and its contents deleted successfully from '{base_dir}'")
                print(f"Directory '{dir_name}' and its contents deleted successfully from '{base_dir}'")
            except FileNotFoundError:
                print(f"Directory '{dir_name}' not found")
        else:
            print(f"Directory '{dir_name}' not found.")

while True:
    print("Enter '1' to create")
    print("Enter '2' to delete")
    print("Enter '3' to segregate")
    user_action = int(input())

    if user_action == 1:
        create_file_or_dir()
    elif user_action == 2:
        delete_file_or_dir()
    elif user_action == 3:
        segregate_files_by_extension(base_dir)
    else:
        print("Enter valid input")