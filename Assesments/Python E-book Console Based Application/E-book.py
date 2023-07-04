# Import required modules
import os

# Define functions
def main_menu():
    print("1. Generate note")
    print("2. View note")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def sub_menu():
    print("1. Add note")
    print("2. View all notes")
    print("3. Back to main menu")
    choice = input("Enter your choice: ")
    return choice

def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    date = input("Enter note date: ")
    with open("notes.txt", "a") as f:
        f.write(title + "," + content + "," + date + "\n")
    print("Note added successfully.")

def view_all_notes():
    if not os.path.exists("notes.txt"):
        print("No notes found.")
    else:
        with open("notes.txt", "r") as f:
            notes = f.readlines()
            for note in notes:
                title, content, date = note.strip().split(",")
                print("Title:", title)
                print("Content:", content)
                print("Date:", date)
                print()

def view_note():
    if not os.path.exists("notes.txt"):
        print("No notes found.")
    else:
        title = input("Enter note title: ")
        with open("notes.txt", "r") as f:
            notes = f.readlines()
            found = False
            for note in notes:
                if title in note:
                    found = True
                    title, content, date = note.strip().split(",")
                    print("Title:", title)
                    print("Content:", content)
                    print("Date:", date)
                    print()
                    break
            if not found:
                print("Note not found.")

# Main program
while True:
    choice = main_menu()
    if choice == "1":
        while True:
            sub_choice = sub_menu()
            if sub_choice == "1":
                add_note()
            elif sub_choice == "2":
                view_all_notes()
            elif sub_choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")
    elif choice == "2":
        view_note