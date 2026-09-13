import json
import hashlib
import os

FILE_NAME = "vault.json"

def hash_password(password):
    """Converts a password into a SHA-256 one-way hash."""
    return hashlib.sha256(password.encode()).hexdigest()

def load_vault():
    """Reads the JSON file and converts it to a Python dictionary."""
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_vault(data):
    """Converts the Python dictionary back to JSON and saves it."""
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# 1. INITIALIZATION: Create the file if it doesn't exist
if not os.path.exists(FILE_NAME):
    print("Welcome! Let's set up your vault.")
    master_pass = input("Create a Master Password: ")
    
    # Store the hash, NOT the actual password
    initial_data = {
        "master_hash": hash_password(master_pass),
        "passwords": {}
    }
    save_vault(initial_data)
    print("Vault created!\n")

# 2. LOGIN VERIFICATION: Check the hash
vault_data = load_vault()
login_attempt = input("Enter Master Password to unlock: ")

if hash_password(login_attempt) != vault_data["master_hash"]:
    print("Access Denied. Incorrect password.")
    exit()

print("Access Granted!\n")

# 3. MAIN MENU: File modification loop
while True:
    print("1. Add a Password  |  2. Get a Password  |  3. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        service = input("Service Name (e.g., Gmail): ")
        username = input("Username: ")
        password = input("Password: ")
        
        # Update the dictionary in memory
        vault_data["passwords"][service] = {"user": username, "pass": password}
        
        # Write the updated dictionary back to the JSON file
        save_vault(vault_data)
        print(f"Saved credentials for {service}.\n")

    elif choice == "2":
        service = input("Enter Service Name to lookup: ")
        
        # Search the dictionary
        if service in vault_data["passwords"]:
            creds = vault_data["passwords"][service]
            print(f"Username: {creds['user']} | Password: {creds['pass']}\n")
        else:
            print("Service not found.\n")

    elif choice == "3":
        print("Locking vault. Goodbye!")
        break
