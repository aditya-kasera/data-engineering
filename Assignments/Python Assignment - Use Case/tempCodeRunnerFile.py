y:
    with open(file_path, 'r') as read_file:
        data = json.load(read_file)
    print(data)
except FileNotFoundError:
    print("File not found.")
except json.JSONDecodeError:
    print