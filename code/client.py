from server import StorageServer  # Ensure class name matches server.py
import os

server = StorageServer()

while True:
    print("\n-- Client Menu ---")
    print("1. Upload File")
    print("2. List Files on Server")
    print("3. Download File")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        file_path = input("Enter full path of the file to upload: ").strip('"').replace("\\", "/")

        if not os.path.exists(file_path):
            print("File doesn't exist")
            continue

        file_name = os.path.basename(file_path)

        # Read file in binary mode
        with open(file_path, 'rb') as f:
            content = f.read()

        print(server.save_file(file_name, content))

    elif choice == "2":
        files = server.list_files()
        print("Files on server:", files)

    elif choice == "3":
        file_name = input("Enter the name of the file to download: ")

        content = server.read_file(file_name)

        if isinstance(content, str) and "does not exist" in content:
            print(content)
        else:
            # Write file in binary mode
            with open(file_name, 'wb') as f:
                f.write(content)
            print(f"{file_name} downloaded successfully!")

    elif choice == "4":
        print("Exiting client...")
        break

    else:
        print("Invalid choice, please enter 1–4")


