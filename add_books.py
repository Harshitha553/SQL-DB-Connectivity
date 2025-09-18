import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
def add_books(title: str, author: str, category: str, stock: int = 1):
    data = {"title": title, "author": author, "category": category, "stock": stock}
    response = supabase.table("books").insert(data).execute()

    if response.data:
        print(f" Book added successfully: {response.data[0]}")
    else:
        print(f" Failed to add book: {response}")

if __name__ == "__main__":
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    category = input("Enter category (optional): ")
    stock = input("Enter stock (default 1): ")
    stock = int(stock) if stock.strip() else 1
    add_books(title, author, category, stock)
