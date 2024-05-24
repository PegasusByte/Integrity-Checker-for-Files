import hashlib

def calculate_hash(file_path):
    sha1_hash = hashlib.sha1()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha1_hash.update(chunk)
        return sha1_hash.hexdigest()
    except FileNotFoundError:
        print("Sorry, Can't find that file. Check your path and try again.")
        return None
    except PermissionError:
        print("It seems like you don't have permission to access that file.")
        return None
    except Exception as e:
        print(f"Something went wrong: {e}")
        return None

def check_integrity(file_path, original_hash):
    file_hash = calculate_hash(file_path)
    if file_hash is not None:
        if file_hash == original_hash:
            print("Integrity secured! Your file's untouched.")
        else:
            print("Uh-oh! Looks like your file's been tampered with.")

# Let's get interactive with file paths!
file_path = input("Where's your file hiding? Enter the path: ")
original_hash = calculate_hash(file_path)
if original_hash is not None:
    print(f"Original hash for {file_path}: {original_hash}")
    check_integrity(file_path, original_hash)
