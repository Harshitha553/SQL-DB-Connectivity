import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def delete_book(book_id: int):
    borrowed = supabase.table("borrow_records").select("*").eq("book_id", book_id).execute()
    if borrowed.data:
        print(f" Cannot delete. Book ID {book_id} is currently borrowed.")
        return
    response = supabase.table("books").delete().eq("book_id", book_id).execute()
    if response.data:
        print(f" Book deleted successfully: {response.data[0]}")
    else:
        print(f" Failed to delete book with ID {book_id}")

if __name__ == "__main__":
    book_id = int(input("Enter Book ID to delete: "))
    delete_book(book_id)
