import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def show_member_details(member_id: int):
    member_resp = supabase.table("members").select("*").eq("member_id", member_id).execute()
    if not member_resp.data:
        print(f" Member with ID {member_id} not found.")
        return

    member = member_resp.data[0]
    print("\n👤 Member Details")
    print("-" * 40)
    print(f"ID: {member['member_id']}")
    print(f"Name: {member['name']}")
    print(f"Email: {member['email']}")
    print(f"Join Date: {member['join_date']}")
    borrow_resp = (
        supabase.table("borrow_records")
        .select("record_id, borrow_date, return_date, books(title, author)")
        .eq("member_id", member_id)
        .execute()
    )

    print("\n Borrowed Books")
    print("-" * 60)
    if not borrow_resp.data:
        print("No books borrowed.")
    else:
        for r in borrow_resp.data:
            status = " Returned" if r["return_date"] else " Not Returned"
            print(f"Record ID: {r['record_id']} | Title: {r['books']['title']} "
                  f"| Author: {r['books']['author']} | Borrowed: {r['borrow_date']} "
                  f"| Returned: {r['return_date']} | Status: {status}")

if __name__ == "__main__":
    member_id = int(input("Enter Member ID: "))
    show_member_details(member_id)
