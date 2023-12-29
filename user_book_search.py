import json

def search_books_by_number(user_input_str, catalog, missing_2022, missing_2015):
    found_books = []

    # Check if user wants to exit
    if user_input_str.lower() == 'done':
        return found_books

    # Convert user input to integer
    try:
        user_input = int(user_input_str)
    except ValueError:
        print("Invalid input. Please enter a valid integer or 'done'.")
        return found_books

    # Search in "Catalog" list
    for book in catalog:
        book_number = book.get("#")
        if book_number is not None and book_number == user_input:
            book['found'] = True
            found_books.append(book)

    # Search in "Missing, 2022" list
    for book in missing_2022:
        book_number = book.get("#")
        if book_number is not None and book_number == user_input:
            book['found'] = True
            found_books.append(book)

    # Search in "Missing, 2015" list
    for book in missing_2015:
        book_number = book.get("#")
        if book_number is not None and book_number == user_input:
            book['found'] = True
            found_books.append(book)

    return found_books

def main():
    # Load data from the JSON file
    try:
        with open('books_seen.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("JSON file not found.")
        return

    # Extract data from each section
    catalog = data.get('Catalog', [])
    missing_2022 = data.get('Missing, 2022', [])
    missing_2015 = data.get('Missing, 2015', [])

    while True:
        # Prompt the user for input
        user_input_str = input("Enter an integer number or 'done' to save and exit: ")

        # Search for books with the given input
        found_books = search_books_by_number(user_input_str, catalog, missing_2022, missing_2015)

        # Print the results
        if found_books:
            print("\nFound books:")
            for book in found_books:
                print(book)
        else:
            print(f"\nNo books found with the input {user_input_str}.")

        # Check if the user wants to exit
        if user_input_str.lower() == 'done':
            break

        # Print statistics
        print_statistics(catalog, missing_2022, missing_2015)

    # Update the JSON file with the marked found status
    save_state_to_json(data)

def print_statistics(catalog, missing_2022, missing_2015):
    total_books = len(catalog) + len(missing_2022) + len(missing_2015)
    found_books = [book for book in catalog + missing_2022 + missing_2015 if book.get('found', False)]
    not_found_books = [book for book in catalog + missing_2022 + missing_2015 if not book.get('found', False)]

    print(f"\nTotal Books: {total_books}")
    print(f"Books Found: {len(found_books)}")
    print(f"Books Not Yet Found: {len(not_found_books)}")

    if not_found_books:
        print("\nList of Books Not Yet Marked as Found:")
        for book in not_found_books:
            print(f"- {book.get('#', 'N/A')}: {book.get('title', 'N/A')}")

def save_state_to_json(data):
    with open('books_seen.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)
    print("\nCurrent state saved successfully.")

if __name__ == "__main__":
    main()
