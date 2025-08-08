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
    
    print(f"Note '{name_note}' saved successfully!")

def open_file():
    print(
        "+--------------------+\n" \
        "|      Open File     |\n" \
        "+--------------------+\n"
    )

    

    

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