import os
from datetime import datetime
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def return_book(member_id: int, book_id: int):
    record_resp = supabase.table("borrow_records").select("*") \
        .eq("member_id", member_id).eq("book_id", book_id).is_("return_date", None).execute()
    if not record_resp.data:
        print(" No active borrow record found.")
        return
    record_id = record_resp.data[0]["record_id"]
    try:
        supabase.table("borrow_records").update({"return_date": datetime.now().isoformat()}) \
            .eq("record_id", record_id).execute()
        book = supabase.table("books").select("*").eq("book_id", book_id).execute().data[0]
        supabase.table("books").update({"stock": book["stock"] + 1}).eq("book_id", book_id).execute()
        print(" Book returned successfully.")
    except Exception as e:
        print(" Transaction failed:", e)

if __name__ == "__main__":
    member_id = int(input("Enter Member ID: "))
    book_id = int(input("Enter Book ID: "))
    return_book(member_id, book_id)
