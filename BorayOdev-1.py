class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")

    def close_file(self):
        self.file.close()

    def __del__(self):
        self.close_file()

    def list_books(self):
        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        if not book_lines:
            print("The library is empty.")
            return

        for book_line in book_lines:
            book_info = book_line.split(',')
            book_name, author, release_date, num_pages = book_info
            print(f"Book: {book_name}, Author: {author}, Release Year: {release_date}, Pages: {num_pages}")

    def add_book(self):
        book_name = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{book_name},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        if self.file.tell() == 0:
            print("No books to remove. The library is empty.")
            return

        title_to_remove = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        book_lines = self.file.read().splitlines()

        updated_book_lines = [line for line in book_lines if title_to_remove not in line]

        if len(book_lines) == len(updated_book_lines):
            print(f"Book '{title_to_remove}' not found.")
            return

        self.file.truncate(0)
        self.file.seek(0)
        self.file.write('\n'.join(updated_book_lines))
        print(f"Book '{title_to_remove}' removed successfully.")

# Creating an object named "lib" with "Library" class
lib = Library()

# Create a menu to interact with the "lib" object
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit (press 'q' to exit)")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice.lower() == "4" or choice.lower() == "q":
        print("Exiting the program.")
        lib.close_file()  # Close the file before exiting
        break
    else:
        print("Invalid choice. Please enter a valid option.")
