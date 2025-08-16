from pathlib import Path
import time
import os


def main():

    print("\033c", end="")  # ANSI escape code для очищення екрану

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

    print("\033c", end="")  # ANSI escape code для очищення екрану

    print(
        "+--------------------+\n" \
        "|      Open File     |\n" \
        "+--------------------+"
    )


    folder = "Files"
    for file in os.listdir(folder):
        print(file)


    name_file = input("\nInput name file\nq - exit\n>>> ")
    print("\033c", end="")  # ANSI escape code для очищення екрану

    if name_file == 'q':
        return
    else:
        while True:

            name_file += '.txt'

            file_path = Path(os.path.abspath(os.path.join(folder, name_file)))

            if os.path.exists(file_path):
                print(f"\nfile {name_file} , found")
                break
            else:
                print(
                    "+--------------------+\n" \
                    "|      Open File     |\n" \
                    "+--------------------+"
                )

                folder = "Files"
                for file in os.listdir(folder):
                    print(file)

                print(f"\nfile {name_file} , NOT found")

                name_file = input("\nInput name file\nq - exit\n>>> ").lower()
                print("\033c", end="")  # ANSI escape code для очищення екрану
                if name_file == 'q': 
                    return
        

        file_do = input("\nr - read\nw - rewrite\na - to add\nq - out\n>>> ").lower()
        print("\033c", end="")  # ANSI escape code для очищення екрану
        while True:
            if file_do == "r":
                content = file_path.read_text(encoding='utf-8')
                print("\n",content)
                file_do = input("\nr - read\nw - rewrite\na - to add\nq - out\n>>> ").lower()
            elif file_do == "q":
                break
            elif file_do == "w":
                print("\nWrite a new text\n")
                text = input("")
                file_path.write_text(text, encoding='utf-8')
                print("file rewrited!")
                time.sleep(1)
                break
            elif file_do == "a":
                content = file_path.read_text(encoding='utf-8')
                with open(file_path, 'w') as file:
                    content += input(content)
                    file.write(content)
                print("\nText Changed")
                time.sleep(1)
                break
            else:
                print("Error, try again!")
                file_do = input("\nr - read\nw - rewrite\na - to add\nq - out\n>>> ").lower()

    
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