import os
from datetime import datetime
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def borrow_book(member_id: int, book_id: int):
    book_resp = supabase.table("books").select("*").eq("book_id", book_id).execute()
    if not book_resp.data:
        print(" Book not found.")
        return
    book = book_resp.data[0]
    if book["stock"] < 1:
        print(" Book not available.")
        return
    try:
        supabase.table("books").update({"stock": book["stock"] - 1}).eq("book_id", book_id).execute()
        supabase.table("borrow_records").insert({
            "member_id": member_id,
            "book_id": book_id,
            "borrow_date": datetime.now().isoformat()
        }).execute()
        print(" Book borrowed successfully.")
    except Exception as e:
        print(" Transaction failed:", e)

if __name__ == "__main__":
    member_id = int(input("Enter Member ID: "))
    book_id = int(input("Enter Book ID: "))
    borrow_book(member_id, book_id)
