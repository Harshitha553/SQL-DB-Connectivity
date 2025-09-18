import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def update_book_title(book_id: int, new_title: str):
    response = supabase.table("books").update({"title": new_title}).eq("book_id", book_id).execute()
    if response.data:
        print(f" Book updated successfully: {response.data[0]}")
    else:
        print(f" Failed to update book with ID {book_id}")

if __name__ == "__main__":
    book_id = int(input("Enter Book ID: "))
    new_title = input("Enter new book title: ")
    update_book_title(book_id, new_title)
