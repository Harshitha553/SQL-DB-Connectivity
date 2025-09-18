import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
def search_books(query: str):
    response = supabase.table("books").select("*").or_(
        f"title.ilike.%{query}%,author.ilike.%{query}%,category.ilike.%{query}%"
    ).execute()
    if response.data:
        print(f"\n Search results for '{query}':")
        print("-" * 60)
        for b in response.data:
            print(f"ID: {b['book_id']} | Title: {b['title']} | Author: {b['author']} | "
                  f"Category: {b['category']} | Stock: {b['stock']}")
    else:
        print(f" No books found for '{query}'")

if __name__ == "__main__":
    q = input("Enter search term (title/author/category): ")
    search_books(q)
