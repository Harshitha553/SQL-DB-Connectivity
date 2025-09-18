import os
from datetime import datetime, timedelta
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def top_borrowed_books():
    records = supabase.table("borrow_records").select("book_id").execute()
    counts = {}
    for r in records.data:
        counts[r["book_id"]] = counts.get(r["book_id"], 0) + 1
    top5 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:5]
    print("🏆 Top 5 Most Borrowed Books")
    for book_id, times in top5:
        book = supabase.table("books").select("*").eq("book_id", book_id).execute().data[0]
        print(f"{book['title']} by {book['author']} — Borrowed {times} times")

def overdue_members(days=14):
    cutoff = datetime.now() - timedelta(days=days)
    records = supabase.table("borrow_records").select("member_id,borrow_date,members(*)") \
        .is_("return_date", None).execute()
    print(f"⏰ Members with overdue books (> {days} days)")
    for r in records.data:
        borrow_date = datetime.fromisoformat(r["borrow_date"])
        if borrow_date < cutoff:
            print(f"{r['members']['name']} — Borrowed on {borrow_date}")

def books_borrowed_per_member():
    records = supabase.table("borrow_records").select("member_id").execute()
    counts = {}
    for r in records.data:
        counts[r["member_id"]] = counts.get(r["member_id"], 0) + 1
    print("📊 Total Books Borrowed per Member")
    for member_id, total in counts.items():
        member = supabase.table("members").select("*").eq("member_id", member_id).execute().data[0]
        print(f"{member['name']} — {total} books")

if __name__ == "__main__":
    top_borrowed_books()
    print("\n")
    overdue_members()
    print("\n")
    books_borrowed_per_member()
