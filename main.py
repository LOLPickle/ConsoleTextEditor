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


    name_file = input("\nInput name file -> ")

    while True:
        if os.path.exists(os.path.abspath(os.path.join(folder, name_file))):
            print(f"\nfile {name_file} , found")
            break
        else:
            print(f"\nfile {name_file} , NOT found")

            name_file = input("Input name file -> ")



    
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