import json

def main():
    book_data = {}

    while True:
        user_input = input("Enter an integer or 'done': ")

        if user_input.lower() == 'done':
            save_to_file(book_data)
            break
        try:
            book_id = int(user_input)
            if book_id in book_data:
                print("dup found")
                book_data[book_id]["dup"] += 1
            else:
                book_data[book_id] = {"value": book_id, "dup": 0}
        except ValueError:
            print("Invalid input. Please enter an integer or 'done'.")

def save_to_file(book_data):
    with open("books_seen.json", "w") as file:
        json.dump(list(book_data.values()), file, indent=2)
    print("Data saved to 'books_seen.json'.")

if __name__ == "__main__":
    main()
