from pathlib import Path
from encryption_decryption import enc
from encryption_decryption import dec
import os

def operation_to_perform(id):
    os.system('cls')
    print(f"Hi {id}!")
    print(f"What service were you looking for?")
    print(" 1. View an existing id & password.")
    print(" 2. Add a new id & password.")
    print(" 3. Update an existing id & password.")
    print(" 4. Delete an existing id & password.")
    print(" 5. Nothing... Just passing by.....")

    number = input("\nEnter the service number mentioned above: ")
    print(number)

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