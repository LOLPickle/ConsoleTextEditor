from pathlib import Path

import os


def main():
    print(
        "+--------------------+\n" 
        "|     Text Editor    |\n" 
        "+--------------------+\n" 
        "| q -> exit          |\n" 
        "| n -> new note      |\n" 
        "| p -> open note     |\n" 
        "+--------------------+\n"
    )

    answer = input(">>> ").lower()

    return answer

def new_note():
    print(
        "+--------------------+\n" \
        "|      New Note      |\n" \
        "+--------------------+\n"
    )

    name_note = input("Name: ")
    
    # Створюємо папку, якщо її немає
    os.makedirs('Files', exist_ok=True)
    
    # Формуємо шлях до файлу з введеним ім'ям
    file_path = os.path.join('Files', f"{name_note}.txt")
    
    # Відкриваємо файл для запису та записуємо вміст
    with open(file_path, 'w') as file:
        content = input("Enter your note: ")
        file.write(content)
    
    print(f"Note '{name_note}' saved successfully!\n")

def open_file():
    print(
        "+--------------------+\n" \
        "|      Open File     |\n" \
        "+--------------------+"
    )


    folder = "Files"
    for file in os.listdir(folder):
        print(file)


    name_file = input("\nInput name file\nq - exit\n>>> ")

    if name_file == 'q':
        main()
    else:
        name_file += '.txt'

        file_path = Path(os.path.abspath(os.path.join(folder, name_file)))

        while True:
            if os.path.exists(file_path):
                print(f"\nfile {name_file} , found")
                break
            else:
                print(f"\nfile {name_file} , NOT found")

                name_file = input("Input name file -> ")

        file_do = input("\nr - read\nw - rewrite\nq - out\n>>> ").lower()
        while True:
            if file_do == "r":
                content = file_path.read_text(encoding='utf-8')
                print("\n",content)
                file_do = input("\nr - read\nw - rewrite\nq - out\n>>> ").lower()
            elif file_do == "q":
                break
            elif file_do == "w":
                print("\nWrite a new text\n")
                text = input("")
                file_path.write_text(text, encoding='utf-8')
                print("file rewrited!")
                break
            else:
                print("Error, try again!")
                file_do = input("\nr - read\nw - rewrite\n>>> ").lower()

    
#---------PROCES-----------#

while True:
    answer = main()

    if answer == 'q':
        print("Exiting program...")
        break
    elif answer == 'n':
        new_note()
    elif answer == 'p':
        open_file()
    else:
        print("Invalid option...")