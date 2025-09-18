import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
def update_book_stock(book_id: int, new_stock: int):
    response = supabase.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute()
    if response.data:
        print(f" Stock updated successfully: {response.data[0]}")
    else:
        print(f" Failed to update stock for Book ID {book_id}")
if __name__ == "__main__":
    book_id = int(input("Enter Book ID: "))
    new_stock = int(input("Enter new stock quantity: "))
    update_book_stock(book_id, new_stock)
