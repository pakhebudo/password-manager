from pathlib import Path
from encryption_decryption import enc
from encryption_decryption import dec
import os
import json


def view(id):
    os.system("cls")
    if (id == "Prabesh Khatri"):
        path = "C:/Users/prabe/Desktop/study material/code/python/projects/build/password manager/101.json"

    elif (id == "Puspa Thapa Godar Khatri"):
        path = "C:/Users/prabe/Desktop/study material/code/python/projects/build/password manager/102.json"

        info = Path(path)

    if info.exists():
        contents = info.read_text()
        contents = dec(contents, 17)
        read_contents = json.loads(contents)

        i=1
        print(f"Here are your list of platforms:")
        for key in read_contents:
            print(f" - {key}")
            i += 1
        
        want = input(f"\nEnter the desired platform: ") 
        if (want in read_contents):
            os.system("cls")
            print(f"{want}:")
            for key1, value1 in read_contents[want].items():
                print(f"{key1} = {value1}")
    else: 
        print(f"Path does not exists")
        

def add(id):
    os.system("cls")
    if (id == "Prabesh Khatri"):
        path = "C:/Users/prabe/Desktop/study material/code/python/projects/build/password manager/101.json"

    elif (id == "Puspa Thapa Godar Khatri"):
        path = "C:/Users/prabe/Desktop/study material/code/python/projects/build/password manager/102.json"

    info = Path(path)
    if info.exists():
        contents = info.read_text()
        contents = dec(contents, 17)
        read_contents = json.loads(contents)

        i=1
        print(f"Here are your list of platforms:")
        for key in read_contents:
            print(f" - {key}")
            i += 1

        new_content = input("Enter the new platform: ")

        temp_dict = {}
        while exit not in temp_dict:
            key = input("Enter attribute: ")
            if key == 'exit':
                break
            temp_dict[key] = input("Enter value: ")

        read_contents[new_content] = temp_dict

        contents = json.dumps(read_contents)
        info.write_text(enc(contents, 17))

        os.system("cls")

        print("Your updated list: ")
        for key in read_contents:
            print(f" - {key}")
            i += 1

    else: 
        print(f"Path does not exists")


def update(id):
    if (id == "Prabesh Khatri"):
        path = "C:/Users/prabe/Desktop/study material/code/python/projects/build/password manager/101.json"

    elif (id == "Puspa Thapa Godar Khatri"):
        path = "C:/Users/prabe/Desktop/study material/code/python/projects/build/password manager/102.json"

    info = Path(path)
    if info.exists():
        contents = info.read_text()
        contents = dec(contents, 17)
        contents = json.loads(contents)

        print(f"Here are your list of platforms: ")
        for key in contents:
            print(f" - {key}")

        change = input(f"Enter the platform for which you want to change the info: ")
        
        for key1, items1 in contents[change].items():
            contents[change][key1] = input(f"Enter new {key1}: ")

        contents = json.dumps(contents)
        contents = enc(contents, 17)
        info.write_text(contents)

    else:
        print(f"Path does not exist.") 


def delete(id):
    if (id == "Prabesh Khatri"):
        path = "C:/Users/prabe/Desktop/study material/code/python/projects/build/password manager/101.json"

    elif (id == "Puspa Thapa Godar Khatri"):
        path = "C:/Users/prabe/Desktop/study material/code/python/projects/build/password manager/102.json"

    info = Path(path)
    if info.exists():
        contents = info.read_text()
        contents = dec(contents, 17)
        contents = json.loads(contents)

        print(f"Here are your list of platforms: ")
        for key in contents:
            print(f" - {key}")

        remove = input(f"Enter the platform of which you want to delete the info: ")

        if remove in contents:
            del contents[remove]
        else:
            print(f"Ain't nothing to see here mate.")

        contents = json.dumps(contents)
        contents = enc(contents, 17)
        info.write_text(contents)

    else:
        print(f"Path does not exist.")         


def operation_to_perform(id):
    os.system('cls')
    print(f"Hi {id}!")
    print(f"What service were you looking for?")
    print(" 1. View an existing id & password.")
    print(" 2. Add a new id & password.")
    print(" 3. Update an existing id & password.")
    print(" 4. Delete an existing id & password.")
    print(" 5. Nothing... Just passing by.....")

    number = input("\nSelect the appropriate number for the service you want: ")
    number = int(number)

    if (number == 1):
        view(id)

    elif (number == 2):
        add(id)

    elif (number == 3):
        update(id)

    elif (number == 4):
        delete(id)

    elif (number == 5):
        print("Noice... Urmmm...... Have a good day... i guess")


def main():
    os.system('cls')

    login_file = Path("C:/Users/prabe/Desktop/study material/code/python/projects/build/password manager/1.txt")

    print(f"--Enter your data to log in--\n")

    id = input("ID: ")
    password = input("Password: ")

    correct_info = dec(login_file.read_text(), 17)
    correct_info_list = correct_info.splitlines()

    logged_in = False

    for i in range(len(correct_info_list)):
        if id == correct_info_list[i] and password == correct_info_list[i+1]:
            logged_in = True
            operation_to_perform(id)

    if logged_in == False:
        print(f"Who da fuk are ya nigger?")

main()