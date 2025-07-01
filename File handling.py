def create_note():
    note = input("Enter a new note: ")
    with open("notes.txt", "w") as file:
        file.write(note + "\n")
    print("New note created and saved to notes.txt")

def append_note():
    note = input("Enter a note to append: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note appended to notes.txt")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
            if content.strip() == "":
                print("No notes to display.")
            else:
                print("\n--- Saved Notes ---")
                print(content)
    except FileNotFoundError:
        print("No notes file found yet.")

# Menu
while True:
    print("\n--- Notes Manager ---")
    print("1. Create New Note (overwrite)")
    print("2. Append Note")
    print("3. View Notes")
    print("4. Exit")

    choice = input("Enter your choice (1–4): ")

    if choice == '1':
        create_note()
    elif choice == '2':
        append_note()
    elif choice == '3':
        view_notes()
    elif choice == '4':
        print("Exiting Notes Manager.")
        break
    else:
        print("Invalid choice. Please try again.")
